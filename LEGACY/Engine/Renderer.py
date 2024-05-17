import math
from Engine.Display import *

class Frame(object):
    X: int
    Y: int
    id: str = "CANVAS"

class Render:
    class Line:
        def __init__(self, x1: int, y1: int, x2: int, y2: int, color: str="#", alpha: int=0):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2

            self.fill = Alpha(color, a=alpha)
        
        def walk(self, m, context: Buffer.Layer):
            start = [self.x1, self.y1]
            end = [self.x2, self.y2]

            amount_x_walk = 1/m
            floored_walk = math.floor(amount_x_walk)
            diff = floored_walk - amount_x_walk

            x_loc = 0

            for y_loc in range(self.y1-self.y2):
                for walk in range(floored_walk):
                    context.set(start[0]+x_loc, start[1]+y_loc, self.fill)
            
            return context

        
        def draw(self, context: Buffer.Layer) -> Buffer.Layer:
            m = (self.y1-self.y2) / (self.x1-self.x2)
            return self.walk(m, context)




    def __init__(self) -> None:
        pass
