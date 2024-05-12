import math
import time
import random

from Engine import *
import Internal
import Internal.Player


class Engine:
    def __init__(self, **kwargs):
        self.REGISTER = REGISTER
        self.TICKER = TICKER
        self.LANG = LANG
        self.DISPLAY = Display(self.TICKER)

        self.start_time = time.time()
        self.target_fps = 30
        
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def _getFps(self) -> int:
        return self.current_fps
    
    def _getTargetFps(self) -> int:
        return self.target_fps
    
    def _register(self, name, item):
        setattr(self, name, item)
    
    def start(self) -> None:
        self.current_fps = 0
        D = self.DISPLAY

        try:
            while True:
                #print("Tick", self.current_fps)
                D._writeToBuffer(random.randrange(1, 5), random.randrange(1, 5), b'A')
                D.render()

                self.current_fps = round(1/self.TICKER.tick(1/self.target_fps), 4)
        except KeyboardInterrupt:
            self.stop()
    
    def stop(self) -> None:
        print("Total Ticks:", self.TICKER.ticks)
        print("Tick Time:", self.current_fps)
        print("Render Time:", self.DISPLAY.render_time)
        print("Stopping...")