import math
import queue
import time
import random

from Engine import *
import Internal


class Engine:
    def __init__(self, **kwargs):
        self.REGISTER = REGISTER
        self.TICKER = TICKER
        self.LANG = LANG

        self.keyboard_callback = self.__void__
        self.mouse_callback = self.__void__

        self.start_time = time.time()
        self.target_fps = 30
        self.target_tickrate = 60
        
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __void__(self, *args):
        pass

    def set(self, key, value):
        setattr(self, key, value)
    
    def get(self, key):
        try:
            return getattr(self, key)
        except AttributeError:
            return None
    
    def _getFps(self) -> int:
        return self.current_fps
    
    def _getTargetFps(self) -> int:
        return self.target_fps
    
    def _register(self, name, item):
        setattr(self, name, item)
    
    def start(self) -> None:
        def tick_callback(*args):
            self.RThread.clear()
        self.current_fps = 0
        RenderQueue = queue.Queue()
        KQueue = queue.Queue()
        MQueue = queue.Queue()
        
        self.RThread = RenderThread(RenderQueue, self.target_fps)
        self.KThread = Keyboard(KQueue)
        self.RThread.start()
        self.KThread.start()
        if self.get("disable_mouse") == True:
            self.MThread = Mouse(MQueue)
            self.MThread.start()


        self.TICKER._register("reset_screen", 20, callback=tick_callback)
        

        try:
            while True:
                # Keyboard
                try:
                    self.current_key = KQueue.get_nowait()
                except Exception:
                    self.current_key = None
                # Mouse
                try:
                    self.current_mouse = MQueue.get_nowait()
                except Exception:
                    self.current_mouse = None
                
                # Updates
                self.get("keyboard_callback")(self.current_key)
                self.get("mouse_callback")(self.current_mouse)
                self.REGISTER.update()

                if self.get("show_render_time"):
                    RenderQueue.put([Render.Text, [1, self.RThread.screen_size[1], f"Render Time: {round(self.RThread.render_time, 4)} ms"], 0])
                
                for amount in range(100):
                    RenderQueue.put([Render.Point, [random.randrange(1, self.RThread.screen_size[0]), random.randrange(1, self.RThread.screen_size[1])], 0])


#                RenderQueue.put([Render.Text, [1, self.RThread.screen_size[1]-1, f"Target FPS: {self.target_fps}"], 0])
#                RenderQueue.put([Render.Text, [1, self.RThread.screen_size[1]-2, f"Total Ticks: {self.TICKER.proc_tick}"], 0])
#                RenderQueue.put([Render.Text, [1, self.RThread.screen_size[1]-3, f"Key: {self.current_mouse}"], 0])

                self.TICKER.tick(1/self.target_tickrate)
                self.RThread.target_fps = self.target_fps
        except KeyboardInterrupt:
            self.stop()
    
    def stop(self) -> None:
        print("Stopping...")