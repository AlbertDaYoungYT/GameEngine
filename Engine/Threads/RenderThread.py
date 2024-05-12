from queue import Queue
import os

class RenderThread:

    def __init__(self, queue, id):
        self.queue = queue
        self.id = id
        self.output = print
        self.term_size = [os.get_terminal_size().columns, os.get_terminal_size().lines]

        self.layers = 4

        # TODO: Create a system to check if the a buffer has changed based on the previous a buffer, and flush if it hasn't
        self.buffer_a      = [[b" " for x in range(self.term_size[0])] for y in range(self.term_size[1])]#*self.layers # A Buffer
        self.buffer_a_prev = [[b" " for x in range(self.term_size[0])] for y in range(self.term_size[1])]*self.layers # Cache Buffer
        self.buffer_b      = [[b" " for x in range(self.term_size[0])] for y in range(self.term_size[1])]             # Render Buffer
    
    def run(self):
        while True:
            pass