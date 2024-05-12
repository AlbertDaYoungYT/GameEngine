import math
import time
import random

import Internal
import Internal.Player
from Language import Languages
from Register import Register
from Time import Tick

global REGISTER
global TICKER
global LANG
TICKER = Tick()
LANG = Languages()
REGISTER = Register()

class Engine:
    def __init__(self, **kwargs):
        self.REGISTER = REGISTER
        self.TICKER = TICKER
        self.LANG = LANG

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

        self._register("items", )

        try:
            while True:
                print("Tick", self.current_fps)
                
                self.current_fps = round(1/self.TICKER.tick(1/self.target_fps), 4)
        except KeyboardInterrupt:
            self.stop()
    
    def stop(self) -> None:
        print("Total Ticks:", self.TICKER.ticks)
        print("Stopping...")