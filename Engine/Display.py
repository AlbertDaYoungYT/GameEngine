import os
import sys
import time

from Engine import Tick

class Display:

    def __init__(self, TICKER: Tick):
        self.TICKER = TICKER
        self.id = "Display"
        self.output = print
        self.term_size = [os.get_terminal_size().columns, os.get_terminal_size().lines]

        self.layers = 4

        # TODO: Create a system to check if the a buffer has changed based on the previous a buffer, and flush if it hasn't
        self.buffer_a      = [[b" " for x in range(self.term_size[0])] for y in range(self.term_size[1])]#*self.layers # A Buffer
        self.buffer_a_prev = [[b" " for x in range(self.term_size[0])] for y in range(self.term_size[1])]*self.layers # Cache Buffer
        self.buffer_b      = [[b" " for x in range(self.term_size[0])] for y in range(self.term_size[1])]             # Render Buffer
    
    def __str__(self) -> str:
        return self.id
    
    def _refresh(self):
        self.term_size = [os.get_terminal_size().columns, os.get_terminal_size().lines]
    
    def _flush(self):
        os.system("cls")
    
    def _switchBuffer(self) -> None:
        self.buffer_b[:] = []
        self.buffer_b = self.buffer_a[:]
        self.buffer_a[:] = [[b" " for x in range(self.term_size[0])] for y in range(self.term_size[1])]

    def _writeToBuffer(self, x: int, y: int, buffer: bytes) -> None:
        self.buffer_a[y][x] = buffer
    
    def _validateBuffer(self, x: int, y: int, buffer: bytes) -> None:
        return self.buffer_a[y][x] == buffer
    
    def clear(self) -> None:
        self._flush()
    
    def render(self) -> float:
        start = time.time()
        self._flush()
        self._switchBuffer()
        for y in self.buffer_b:
            self.output(b''.join(y).decode())

        self.render_time = time.time() - start

