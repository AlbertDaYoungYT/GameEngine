
from LEGACY.Engine.Time import Tick
from LEGACY.Engine.Display import Display
from Engine.Language import Language
from Engine.Register import Register

global REGISTER
global TICKER
global LANG
REGISTER = Register()
TICKER = Tick()
LANG = Language()


from Engine.Engine import Engine