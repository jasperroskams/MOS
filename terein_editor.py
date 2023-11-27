import pyxel

from terrein import *
lijst_met_terijnkleuren = [11, 3, 6, 13, 15, 4, 14]

PEN = 0
EMMER = 1
GESELECTEERT = pyxel.COLOR_BLACK
NIET_GESELECTEERT = pyxel.COLOR_ORANGE

class Terein_editor():
    def __init__(self):
        self.aan_het_editeren = True
        self.geselecterde_ondergrond = 0
        self.geselecterd_tekenvoorwerp = 0
        self.is_bezig = False

    def update(self, game):
        terrein = getTerrein()
        if game.aan_het_editeren:
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                if pyxel.mouse_x <= len(lijst_met_terijnkleuren) * 16 and pyxel.mouse_y >= game.hoogte - 16:
                    self.geselecterde_ondergrond = pyxel.mouse_x // 16
                if pyxel.mouse_x < 32 * 7 and pyxel.mouse_y < 32 * 7:
                    if self.geselecterd_tekenvoorwerp == PEN:
                        terrein[pyxel.mouse_y // 7][pyxel.mouse_x // 7] = self.geselecterde_ondergrond
                    elif self.geselecterd_tekenvoorwerp == EMMER:
                        self.is_bezig = True
                        # print("opvulleeeeeeen!!!!!!!!!!")
                        self.opvulen(pyxel.mouse_y // 7, pyxel.mouse_x // 7, terrein[pyxel.mouse_y // 7][pyxel.mouse_x // 7], terrein)
                        terrein[pyxel.mouse_y // 7][pyxel.mouse_x // 7] = self.geselecterde_ondergrond
                        # print('gedaan')
                        self.is_bezig = False
                if pyxel.mouse_x >= len(lijst_met_terijnkleuren) * 16 and pyxel.mouse_y >= game.hoogte - 16:
                    self.geselecterd_tekenvoorwerp = pyxel.mouse_x // 16 - (len(lijst_met_terijnkleuren))
            if pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT):
                self.geselecterde_ondergrond = terrein[pyxel.mouse_y // 7][pyxel.mouse_x // 7]



    def draw(self, game):
        if self.aan_het_editeren:
            pyxel.rect(0, 0, 256, 256, 0)
            terrein = getTerrein()
            for y, rij in enumerate(terrein):
                for x, blok in enumerate(rij):
                    pyxel.rect(x*7, y*7, 6, 6, lijst_met_terijnkleuren[blok])
            if self.geselecterd_tekenvoorwerp == PEN:
                pyxel.blt(len(lijst_met_terijnkleuren) * 16, game.hoogte - 16, 2, 96, 0, 16, 16, GESELECTEERT)
                pyxel.blt(len(lijst_met_terijnkleuren) * 16 + 16, game.hoogte - 16, 2, 112, 0, 16, 16, NIET_GESELECTEERT)
            elif self.geselecterd_tekenvoorwerp == EMMER:
                pyxel.blt(len(lijst_met_terijnkleuren) * 16, game.hoogte - 16, 2, 96, 0, 16, 16, NIET_GESELECTEERT)
                pyxel.blt(len(lijst_met_terijnkleuren) * 16 + 16, game.hoogte - 16, 2, 112, 0, 16, 16, GESELECTEERT)
        for i in range(0, len(lijst_met_terijnkleuren)):
            pyxel.rect(i * 16, game.hoogte - 16, 15, 15, lijst_met_terijnkleuren[i])
        game.highlight(self.geselecterde_ondergrond * 16, game.hoogte - 16)

    def opvulen(self, y, x, kleur, terrein):
        # print(y, x, self.is_bezig)
        if kleur != self.geselecterde_ondergrond:
            terrein[y][x] = self.geselecterde_ondergrond
            for iy in range(-1, 2):
                for ix in range(-1, 2):
                    if (ix == 0 or iy == 0) and (ix != 0 or iy != 0):
                        if 0 <= y + iy <= 31 and 0 <= x + ix <= 31:
                            if terrein[y + iy][x + ix] == kleur:
                                self.opvulen(y + iy, x + ix, kleur, terrein)
