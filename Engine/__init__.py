
from Engine.Time import *
from Engine.Display import *
from Engine.Language import *
from Engine.Register import *
from Engine.Renderer import *

global REGISTER
global TICKER
global LANG
REGISTER = Register()
TICKER = Tick()
LANG = Language()


from Engine.Engine import Engine