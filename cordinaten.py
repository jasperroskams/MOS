
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
    def __init__(self, x, y, Z):
        z = Z
        self.x = x
        self.y = y
        self.x_cord = self.x // z
        self.y_cord = self.y // z


    def naar_(self, richting):
        return GameCoordinaat(self.x + richting[richting[X]], self.y + richting[richting[Y]])