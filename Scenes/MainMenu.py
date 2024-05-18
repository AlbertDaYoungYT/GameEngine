import threading
from Engine import Renderer
from Internal import Types

class UI(object):

    class Variants(object):
        def __init__(self) -> None:
            self.BASE = Renderer.Render().Box(Types.UIPositions.CENTER[0] - 10, Types.UIPositions.CENTER[1] - 5, Types.UIPositions.CENTER[0] + 10, Types.UIPositions.CENTER[1] + 5)

    def __init__(self) -> None:
        pass

    def _render(self, *args, **kwargs):
        pass

class BackgroundThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(super)
        