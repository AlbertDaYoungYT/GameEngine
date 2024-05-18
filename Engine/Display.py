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
    def __init__(self, QUEUE: queue.Queue, target_fps):
        threading.Thread.__init__(self)
        self.id = "Display"
        self.QUEUE = QUEUE
        self.output = sys.stdout

        self.target_fps = target_fps

        self.buffer_a = {}
        self.screen_buffer = {}
        self.prev_screen_buffer = {}

        self.render_time = 0

        self.screen_size = [os.get_terminal_size()[0], os.get_terminal_size()[1]]
    
    def _refresh(self):
        self.screen_size = [os.get_terminal_size()[0], os.get_terminal_size()[1]]
    
    def _flush(self):
        self.output.flush()
    
    def _write(self, x, y, char):
        self.output.write("\x1b7\x1b[%d;%df%s\x1b8" % (int(y), int(x), char))
        self._flush()
    
    def changeDetected(self):
        if self.prev_screen_buffer != self.screen_buffer: return True
        return False

    
    def clear(self):
        self.buffer_a = {}
        self.screen_buffer = {}

        os.system("cls") if platform.system() == "Windows" else os.system("clear")
        self._flush()
#        for column in range(self.screen_size[0]):
#            for line in range(self.screen_size[1]):
#                self._write(column+1, line+1, " ")
    
    def addToBuffer(self, sequence):
        for key, value in sequence.items():
            self.buffer_a[key] = value
    
    def render(self, *args, **kwargs):
        for key, value in self.buffer_a.items():
            try:
                current = self.screen_buffer[key]
            except KeyError:
                current = Alpha(" ", a=0)
                
            self.screen_buffer[key] = value
        
        if kwargs.get("no_clear_buffer_a", False): return True
        self.buffer_a = {}
        return True
    
    def display(self, *args, **kwargs):
        for key, value in self.screen_buffer.items():
            x, y = key.split(":")
            self._write(x, y, value.c)
        
        self.prev_screen_buffer = self.screen_buffer.copy()

    
    def run(self):
        self.clear()
        while True:
            while not self.QUEUE.empty():
                work = self.QUEUE.get()
                work[0](*work[1]).draw(self)
            
            self.render()
        
            if self.changeDetected():
                self._refresh()
                start_time = time.time()
                self.display()

#                self.QUEUE.task_done()
                self.render_time = ms(time.time() - start_time)
            
            time.sleep(1/self.target_fps)