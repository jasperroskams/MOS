from typing import Any

from Jan.GC import GameCoordinate


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class TerreinType:
    pass

class Land(TerreinType):
    pass

class Water(TerreinType):
    pass

class Bouwsel(TerreinType):
    pass

class Rivier(Water, metaclass=Singleton):
    pass

class Meer(Water, metaclass=Singleton):
    pass

class Zee(Water, metaclass=Singleton):
    pass

class Weg(Land, metaclass=Singleton):
    pass

class Bos(Land, metaclass=Singleton):
    pass

class Gras(Land, metaclass=Singleton):
    pass

class Berg(Land, metaclass=Singleton):
    pass

class Gebouw(Bouwsel, metaclass=Singleton):
    pass

class Muur(Bouwsel, metaclass=Singleton):
    pass

class Poort(Bouwsel, metaclass=Singleton):
    pass


# class Tegel:
#     def __init__(self, type):
#         self.type = type
class Speelveld:
    def __init__(self, breedte, hoogte, default_veld=None):
        self.breedte = breedte
        self.hoogte = hoogte
        self.velden = []
        for _ in range(breedte):
            self.velden.append([default_veld] * hoogte)

    def __getitem__(self, gc: GameCoordinate):
        if self.isBinnenGrenzen(gc):
            return self.velden[gc.x][gc.y]
        else:
            raise IndexError


    def __setitem__(self, gc: GameCoordinate, value: Any):
        if self.isBinnenGrenzen(gc):
            self.velden[gc.x][gc.y] = value
        else:
            raise IndexError

    def isBinnenGrenzen(self, gc: GameCoordinate):
        if 0 <= gc.x < self.breedte and 0 <= gc.y < self.hoogte:
            return True
        else:
            return False





