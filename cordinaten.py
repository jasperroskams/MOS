


class Richting:
    def __init__(self, afstand_x, afstand_y):
        self.x = afstand_x
        self.y = afstand_y


class GameCoordinaat:
    """Converteert muis x en y naar game coordinaat (tegel index)"""
    def __init__(self, screen_x, screen_y, scale = 1):
        self.x = screen_x // scale
        self.y = screen_y // scale

    def naar_(self, richting: Richting):
        return GameCoordinaat(self.x + richting.x, self.y + richting.y)

    def __add__(self, richting: Richting):
        return GameCoordinaat(self.x + richting.x, self.y + richting.y)



BOVEN = Richting(0, -1)
RECHTS = Richting(1, 0)
ONDER = Richting(0, 1)
LINKS = Richting(-1, 0)


geklikte_tegel = GameCoordinaat(338, 189, 16)
tegel_boven = geklikte_tegel.naar_(BOVEN)

tegel_onder = geklikte_tegel + ONDER
