from game import Game



class GameCoordinaat():
    """Converteert muis x en y naar game coordinaat (tegel index)"""
    def __init__(self, x, y):
        z = Game.get_zoom_factor()
        self.x = x // z
        self.y = y // z


