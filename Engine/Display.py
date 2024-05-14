import os
import sys
import time
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


class Buffer(object):
    class Layer(object):
        class Line(object):
            def __init__(self, l) -> None:
                self.LINE = [Alpha(None, a=0)]*l
                self.length = l
            
            def __str__(self):
                return self.LINE
            
            def __eq__(self, other):
                if len(self.LINE) != len(other.LINE): return False
                return [ item==other.LINE[self.LINE.index(item)] for item in self.LINE ] == [True]*len(self.LINE)

            def __ne__(self, other):
                return not self.__eq__(other)
            
            def diff(self, other):
                res = []
                for i in self.LINE:
                    if i != other.LINE[self.LINE.index(i)]: res.append(self.LINE.index(i))
                return res
            

        def __init__(self, x, y) -> None:
            self.LAYER = [self.Line(x)]*y
            self.x = x
            self.y = y
        
        def set(self, x, y, value):
            self.LAYER[y].LINE[x] = value
        
        def merge(self, other):
            base_layer = self.LAYER
            layer2     = other.LAYER

            base_layer_diff = [ x.diff(layer2[base_layer.index(x)]) for x in base_layer]
            for line in base_layer_diff:
                pos_y = base_layer_diff.index(line)
                for diff in line:
                    diff1 = base_layer[pos_y].LINE[diff]
                    diff2 = layer2[pos_y].LINE[diff]
                    if diff1.isTransparent():
                        self.set(diff, pos_y, diff2)
                    if diff2.isTransparent():
                        self.set(diff, pos_y, diff1)
            
            return self.LAYER
        
        def __str__(self):
            return self.LAYER
        
        def __eq__(self, other):
            if self.x != other.x and self.y != other.y: return False
            return [ line==other.LAYER[self.LAYER.index(line)] for line in self.LAYER ] == [True]*self.y
        
        def __ne__(self, other):
            return not self.__eq__(other)


    def __init__(self, x: int, y: int, z: int = 1):
        self.layer_count = z
        self.BUFFER = [self.Layer(x, y)]*z
        self.x = x
        self.y = y
    
    def __str__(self):
        return self.BUFFER
    
    def __eq__(self, other):
        if self.x != other.x and self.y != other.y and self.layer_count != other.layer_count: return False
        return [ layer==other.BUFFER[self.BUFFER.index(layer)] for layer in self.BUFFER] == [True]*self.layer_count
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def addLayer(self, layer: Layer):
        self.BUFFER.append(layer)
        self.layer_count += 1

    def removeLayer(self, z: int):
        self.BUFFER.pop(z)
    
    def removeLayer(self, layer: Layer):
        self.BUFFER.remove(layer)
    
    def mergeLayer(self, z, layer: Layer):
        self.BUFFER[z].merge(layer)
        
    def flatten(self):
        buffer = self.BUFFER
        for layer_index in range(len(buffer)):
            self.mergeLayer(0, buffer[layer_index])
        return self.BUFFER

class RenderThread(threading.Thread):
    def __init__(self, TICKER: Tick, *args):
        threading.Thread.__init__(self)
        self.id = "RenderThread"
        self.output = print
        self.TICKER = TICKER
        self.tick = self.TICKER._register(self.id, 2, callback=self._tick_callback)
        self.term_size = [os.get_terminal_size().columns, os.get_terminal_size().lines]

        self.layers = 4

        # Buffers
        self.buffer_a = Buffer(self.term_size[0], self.term_size[1], z=self.layers) # A Buffer
        self.buffer_b = Buffer(self.term_size[0], self.term_size[1]) # Render Buffer
        self.v_buffer = self.buffer_b[:]
    
    def _tick_callback(self, _self, t, v):
        self._switchBuffer()
    
    
    def _compressBufferA(self):
        for layer in range(self.layers):
            self.buffer_v
    
    def _switchBuffer(self):
        

    
    def _refresh(self):
        self.term_size = [os.get_terminal_size().columns, os.get_terminal_size().lines]
    
    def flush(self):