import math

from Jan.GC import GameCoordinate
from typing import Type


from Jan.terrein import *


# Singleton pattern
class Eenheid():

    def __init__(self, gc: GameCoordinate, speler):
        self.gc: GameCoordinate = gc
        self.speler = speler
        self.kleur = speler.kleur
        self.inspanning = {}

    def getMoeiteVoorVooruitgangInTerrein(self, terrein: Type[Speelveld]):
        if terrein in self.inspanning:
            return self.inspanning[terrein]
        else:
            return math.inf


class LandmachtEenheid(Eenheid):
    def __init__(self, gc, speler):
        super().__init__(gc, speler)
        self.inspanning = {
            Gras: 10,
            Bos: 10,
            water: 20,
            Berg: 5,
            Weg: 1,

        }





class MarineEenheid(Eenheid):
    def __init__(self, gc, speler):
        super().__init__(gc, speler)
        self.inspanning = {
            Rivier: 1,
            Meer: 1,
            Zee: 1,
            Weg: 10,
            Bos: 3,
            Gras: 5,
            Berg: 2,
            Gebouw: 0,
            Muur: 0,
            Poort: 0
        }

class LuchtmachtEenheid(Eenheid):
    def __init__(self, gc, speler):
        super().__init__(gc, speler)
        self.inspanning = {
            Rivier: 1,
            Meer: 1,
            Zee: 1,
            Weg: 10,
            Bos: 3,
            Gras: 5,
            Berg: 2,
            Gebouw: 0,
            Muur: 0,
            Poort: 0
        }

class Speer(LandmachtEenheid):
    def __init__(self, gc, speler):
        super().__init__(gc, speler)
        self.inspanning = {
            Rivier: 1,
            Meer: 1,
            Zee: 1,
            Weg: 10,
            Bos: 3,
            Gras: 5,
            Berg: 2,
            Gebouw: 0,
            Muur: 0,
            Poort: 0
        }

class Kanon(LandmachtEenheid):
    def __init__(self, gc, speler):
        super().__init__(gc, speler)
        self.inspanning = {
            Rivier: 1,
            Meer: 1,
            Zee: 1,
            Weg: 10,
            Bos: 3,
            Gras: 5,
            Berg: 2,
            Gebouw: 0,
            Muur: 0,
            Poort: 0
        }



