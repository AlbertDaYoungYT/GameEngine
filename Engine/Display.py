import os
import sys
import time
import queue
import platform
import threading

from Engine import Tick
from Engine.Time import ms


class Alpha(object):
    def __init__(self, c, a=1):
        self.alpha = a
        self.c = c
    
    def __str__(self):
        if self.alpha == 1:
            return self.c
        else:
            return None
    
    def __eq__(self, other):
        return True if self.c == other.c and self.alpha == other.alpha else False
        
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def isTransparent(self):
        return self.alpha == 0


class RenderThread(threading.Thread):
    def __init__(self, QUEUE):
        threading.Thread.__init__(self)
        self.id = "Display"
        self.QUEUE = QUEUE
        self.output = sys.stdout

        self.buffer_a = {}
        self.screen_buffer = {}
        self.prev_screen_buffer = {}

        self.render_time = 0

        self.screen_size = [os.get_terminal_size()[0], os.get_terminal_size()[1]]
    
    def _flush(self):
        self.output.flush()
    
    def _write(self, x, y, char):
        self.output.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, char))
        self._flush()
    
    def _validate(self):
        screen_buffer_copy = self.screen_buffer.copy()
        for key, value in self.prev_screen_buffer.items():
            current = screen_buffer_copy[key]
            if current.isTransparent() and not value.isTransparent():
                screen_buffer_copy[key] = value
        
        if screen_buffer_copy == self.screen_buffer and self.buffer_a == {}: return True
        return False
    
    def clear(self):
        self.buffer_a = {}
        self.screen_buffer = {}

        for line in range(self.screen_size[1]):
            for column in range(self.screen_size[0]):
                self._write(line, column, " ")
    
    def addToBuffer(self, sequence):
        for key, value in sequence.items():
            self.buffer_a[key] = value
    
    def render(self, *args, **kwargs):
        for key, value in self.buffer_a.items():
            try:
                current = self.screen_buffer[key]
            except KeyError:
                current = Alpha(" ", a=0)
            if current.isTransparent() and not value.isTransparent():
                self.screen_buffer[key] = value
        
        for key, value in self.screen_buffer.items():
            x, y = key.split(":")
            self._write(x, y, value.c)
        
        self.prev_screen_buffer = self.screen_buffer
        
        if kwargs.get("no_clear_buffer_a", False): return True
        self.buffer_a = {}
        return True
    
    def run(self):
        self.clear()
        while True:
            try:
                work = self.QUEUE.get()
                if work[0] == "CLS":
                    self.clear()
            except queue.Empty:
                continue

            work[0](*work[1]).draw(self)
        
            if not self._validate():
                start_time = time.time()
                self.render()

                self.QUEUE.task_done()
                self.render_time = ms(time.time() - start_time)