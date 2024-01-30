import pyxel

from terrein import *
lijst_met_terijnkleuren = [11, 3, 6, 13, 15, 4, 14]

PEN = 0
EMMER = 1
VLAK = 2
GESELECTEERT = pyxel.COLOR_BLACK
NIET_GESELECTEERT = pyxel.COLOR_ORANGE

class Terein_editor():
    def __init__(self):
        self.aan_het_editeren = True
        self.geselecterde_ondergrond = 0
        self.geselecterd_tekenvoorwerp = 0
        self.is_bezig = False
        self.nog_op_te_vulen_tegels = []

    def update(self, game):
        terrein = getTerrein()
        if game.aan_het_editeren:
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or self.is_bezig:
                if self.is_bezig:
                    for tegel in self.nog_op_te_vulen_tegels:
                        self.opvulen(tegel[0], tegel[1], tegel[2], tegel[4])
                if pyxel.mouse_x <= len(lijst_met_terijnkleuren) * 16 and pyxel.mouse_y >= game.hoogte - 16:
                    self.geselecterde_ondergrond = pyxel.mouse_x // 16
                if pyxel.mouse_x < 32 * 7 and pyxel.mouse_y < 32 * 7:
                    if self.geselecterd_tekenvoorwerp == PEN:
                        if terrein[pyxel.mouse_y // 7][pyxel.mouse_x // 7] == 2 and self.geselecterde_ondergrond == 4:
                            terrein[pyxel.mouse_y // 7][pyxel.mouse_x // 7] = 5
                        elif terrein[pyxel.mouse_y // 7][pyxel.mouse_x // 7] == 4 and self.geselecterde_ondergrond == 2:
                            terrein[pyxel.mouse_y // 7][pyxel.mouse_x // 7] = 5
                        else:
                            if terrein[pyxel.mouse_y // 7][pyxel.mouse_x // 7] == 5 and (self.geselecterde_ondergrond == 4 or self.geselecterde_ondergrond == 2):
                                pass
                            else:
                                terrein[pyxel.mouse_y // 7][pyxel.mouse_x // 7] = self.geselecterde_ondergrond
                    elif self.geselecterd_tekenvoorwerp == EMMER:
                        self.is_bezig = True
                        # print("opvulleeeeeeen!!!!!!!!!!")
                        self.opvulen(pyxel.mouse_y // 7, pyxel.mouse_x // 7, terrein[pyxel.mouse_y // 7][pyxel.mouse_x // 7], terrein)
                        terrein[pyxel.mouse_y // 7][pyxel.mouse_x // 7] = self.geselecterde_ondergrond
                        # print('gedaan')
                        self.is_bezig = False
                    # elif self.geselecterd_tekenvoorwerp == VLAK:
                    #     self.vierkant()
                    #     pass
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
            else:
                pyxel.blt(len(lijst_met_terijnkleuren) * 16, game.hoogte - 16, 2, 96, 0, 16, 16, NIET_GESELECTEERT)
            if self.geselecterd_tekenvoorwerp == EMMER:
                pyxel.blt(len(lijst_met_terijnkleuren) * 16 + 16, game.hoogte - 16, 2, 112, 0, 16, 16, GESELECTEERT)
            else:
                pyxel.blt(len(lijst_met_terijnkleuren) * 16 + 16, game.hoogte - 16, 2, 112, 0, 16, 16, NIET_GESELECTEERT)
            if self.geselecterd_tekenvoorwerp == VLAK:
                pyxel.blt(len(lijst_met_terijnkleuren) * 16 + 32, game.hoogte - 16, 2, 128, 0, 16, 16, GESELECTEERT)
            else:
                pyxel.blt(len(lijst_met_terijnkleuren) * 16 + 32, game.hoogte - 16, 2, 128, 0, 16, 16, NIET_GESELECTEERT)
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
                                new_op_te_vulen_tegel = [y + iy, x + ix, kleur, terrein]
                                self.nog_op_te_vulen_tegels.append(new_op_te_vulen_tegel)
                                print(self.nog_op_te_vulen_tegels)


    def vierkant(self, beginX, beginY, eindX, eindY, kleur, terrein):
        for y in range(0, (beginY - eindY)):
            for x in range(0, (beginX - eindX)):
                terrein[beginY+y][beginX+x] = kleur


