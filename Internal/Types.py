import os
import math


class UIPositions(object):
    TOP_LEFT: list = [1, 1]
    BOTTOM_LEFT: list = [1, os.get_terminal_size()[1]]
    TOP_RIGHT: list = [os.get_terminal_size()[0], 1]
    BOTTOM_RIGHT: list = [os.get_terminal_size()[0], os.get_terminal_size()[1]]

    CENTER: list = [math.floor(os.get_terminal_size()[0]/2), math.floor(os.get_terminal_size()[1]/2)]
    LEFT_CENTER: list = [1, CENTER[1]]
    RIGHT_CENTER: list = [os.get_terminal_size()[0], CENTER[1]]
    TOP_CENTER: list = [CENTER[0], 1]
    BOTTOM_CENTER: list = [CENTER[0], os.get_terminal_size()[1]]
