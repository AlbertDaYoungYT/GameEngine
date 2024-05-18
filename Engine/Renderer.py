import math
from Engine.Display import *


class Render:
    class Line(object):
        def __init__(self, x1: int, y1: int, x2: int, y2: int, color: str="#", alpha: int=1):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2

            self.fill = Alpha(color, a=alpha)
                
        def draw(self, context: RenderThread):
            x = self.x1
            y = self.y1
            x_delta = self.x2 - self.x1
            y_delta = self.y2 - self.y1

            if x_delta == 0: x_delta = 1
            if y_delta == 0: y_delta = 1
            
            e = y_delta / x_delta - 0.5
            for i in range(1, x_delta+1):
                context.addToBuffer({f"{x}:{y}": self.fill})
                while e >= 0:
                    y += 1
                    e -= 1
                x += 1
                e += y_delta / x_delta
    
    class Point(object):
        def __init__(self, x, y, color: str="#", alpha: int=1):
            self.x = x  
            self.y = y

            self.fill = Alpha(color, a=alpha)
        
        def draw(self, context: RenderThread):
            context.addToBuffer({f"{self.x}:{self.y}": self.fill})
    
    class Text(object):
        def __init__(self, x, y, text: str, alpha: int=1):
            self.x = x
            self.y = y
            self.text = text
            self.alpha = alpha

        def draw(self, context: RenderThread):
            index = 0
            for char in self.text:
                context.addToBuffer({f"{self.x+index}:{self.y}": Alpha(char, a=self.alpha)})
                index += 1
    
    class Box(object):
        def __init__(self, x1, y1, x2, y2, color: str="#", alpha: int=1, fill=False) -> None:
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2

            self.fill_inside = fill
            self.fill = Alpha(color, a=alpha)
        
        def draw(self, context: RenderThread):
            for horizon in range(1, self.x2-self.x1 + 1):
                context.addToBuffer({f"{self.x1+horizon}:{self.y1}": self.fill})
                context.addToBuffer({f"{self.x1+horizon}:{self.y2}": self.fill})
            
            for vertical in range(1, self.y2-self.y1 + 1):
                context.addToBuffer({f"{self.x1}:{self.y1+vertical}": self.fill})
                context.addToBuffer({f"{self.x2}:{self.y1+vertical}": self.fill})


    class Flush(object):
        def __init__(self, x1, y1, x2, y2):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
        
        def draw(self, context: RenderThread):
            for y in range(1, self.y2-self.y1 +1):
                for x in range(1, self.x2-self.x1 +1):
                    context.addToBuffer({f"{self.x1+x}:{self.y1+y}": Alpha(" ", a=1)})
    
