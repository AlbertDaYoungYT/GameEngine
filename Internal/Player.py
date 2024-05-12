
from Internal.Entity import *

class Player(Entity):
    def __init__(self, name):
        self.name = name
        super(Entity, self).__init__()

    def __str__(self):
        return self.name

    def __repr__(self):
        return "" % (self.name,)