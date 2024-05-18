import queue
import threading
from pynput.keyboard import Key, Listener
from pynput.mouse import Listener

class Keyboard(threading.Thread):
    def __init__(self, QUEUE: queue.Queue) -> None:
        threading.Thread.__init__(self)
        self.QUEUE = QUEUE

    def on_press(self, key):
        self.QUEUE.put([key, "DOWN"])

    def on_release(self, key):
        self.QUEUE.put([key, "UP"])

    def run(self):
        with Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

class Mouse(threading.Thread):
    def __init__(self, QUEUE: queue.Queue) -> None:
        threading.Thread.__init__(self)
        self.QUEUE = QUEUE
    
    def on_move(self, x, y):
        self.QUEUE.put_nowait(["MOVE", [x, y]])

    def on_click(self, x, y, button, pressed):
        self.QUEUE.put_nowait(["CLICK", [x, y, button, pressed]])

    def on_scroll(self, x, y, dx, dy):
        self.QUEUE.put_nowait(["SCROLL", [x, y, dx, dy]])

    def run(self):
        with Listener(
                on_move=self.on_move,
                on_click=self.on_click,
                on_scroll=self.on_scroll) as listener:
            listener.join()