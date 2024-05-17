import math
from Engine.Display import *


class Render:
    class Line(object):
        def __init__(self, x1: int, y1: int, x2: int, y2: int, color: str="#", alpha: int=0):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2

            self.fill = Alpha(color, a=alpha)
        
        def _walk(self, m):
            res = {}
            start = [self.x1, self.y1]
            end = [self.x2, self.y2]

            amount_x_walk = 1/m
            floored_walk = math.floor(amount_x_walk)
            diff = floored_walk - amount_x_walk

            x_loc = 1

            for y_loc in range(self.y1-self.y2):
                if floored_walk < 0:
                    for neg_walk in range(abs(floored_walk)):
                        res[f"{start[0]+x_loc}:{start[1]-y_loc}"] = self.fill
                else:
                    for walk in range(floored_walk):
                        res[f"{start[0]+x_loc}:{start[1]+y_loc}"] = self.fill
            
            return res

        
        def draw(self, context: RenderThread):
            m = (self.y1-self.y2) / (self.x1-self.x2)
            buffer = self._walk(m)
            context.addToBuffer(buffer)