import pyxel


class Munitie():
    def __init__(self, eenheid, duur_schietanimatie, schietanimatie_x, schietanimatie_y, einde_schietanimatie_x, einde_schietanimatie_y, schietrichting_x, schietrichting_y):
        self.schietanimatie = 0
        self.duur_schietanimatie = duur_schietanimatie
        self.schietanimatie_x = schietanimatie_x
        self.schietanimatie_y = schietanimatie_y
        self.einde_schietanimatie_x = einde_schietanimatie_x
        self.einde_schietanimatie_y = einde_schietanimatie_y
        self.schietrichting_x = schietrichting_x
        self.schietrichting_y = schietrichting_y
        self.soort = 0
        if eenheid.boot == 1:
            if eenheid.T == 0:
                if eenheid.welk_type == 4:
                    self.soort = 0
                elif eenheid.welk_type == 3:
                    self.soort = 32
                else:
                    if eenheid.bereik > 1:
                        self.soort = 0
            else:
                if eenheid.welk_type != 3 and eenheid.welk_type != 5 and eenheid.munitie > 0:
                    self.soort = 16
                elif eenheid.welk_type == 3:
                    self.soort = 16
        else:
            if eenheid.munitie > 0:
                self.soort = 32
        self.duur_schietanimatie = duur_schietanimatie // (self.soort // 8 + 1)




    def update(self):
        if self.schietanimatie < self.duur_schietanimatie:
            if self.schietrichting_x > 0:
                if self.schietanimatie_x < self.einde_schietanimatie_x:
                    self.schietanimatie_x += 1 * self.schietrichting_x * (self.soort // 8 + 1)
            else:
                if self.schietanimatie_x > self.einde_schietanimatie_x:
                    self.schietanimatie_x += 1 * self.schietrichting_x * (self.soort // 8 + 1)
            if self.schietrichting_y > 0:
                if self.schietanimatie_y < self.einde_schietanimatie_y:
                    self.schietanimatie_y += 1 * self.schietrichting_y * (self.soort // 8 + 1)
            else:
                if self.schietanimatie_y > self.einde_schietanimatie_y:
                    self.schietanimatie_y += 1 * self.schietrichting_y * (self.soort // 8 + 1)
            self.schietanimatie += 1

        # self.schietanimatie = 0
        # if positiefx_verschil > positiefy_verschil:
        #     self.duur_schietanimatie = x_verschil * self.schietrichting_x
        # else:
        #     self.duur_schietanimatie = y_verschil * self.schietrichting_y
        # self.schietanimatie_x = self.geselecteerde_eenheid.x
        # self.einde_schietanimatie_x = self.aangepaste_x
        # self.schietanimatie_y = self.geselecteerde_eenheid.y
        # self.einde_schietanimatie_y = self.aangepaste_y



    def draw(self, game):
        if self.schietanimatie < self.duur_schietanimatie:
            pyxel.blt(self.schietanimatie_x + game.begin_teken_x * 16, self.schietanimatie_y + game.begin_teken_y * 16, 2, self.soort, 168, 16, 16, pyxel.COLOR_BLACK)



