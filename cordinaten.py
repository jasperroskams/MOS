from game import Game

BOVEN = 0
RECHTS = 1
ONDER = 2
LINKS = 3
Y = 0
X = 1

richtingen = [
    [ 0,-1],
    [ 1, 0],
    [ 0, 1],
    [-1, 0],
]

class GameCoordinaat():
    """Converteert muis x en y naar game coordinaat (tegel index)"""
    def __init__(self, x, y):
        z = Game.get_zoom_factor()
        self.x = x // z
        self.y = y // z


    def naar_(self, richting):
        return