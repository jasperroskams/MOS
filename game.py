import pyxel
from animatie import *
from blokken import *
import route
from eenheid import Eenheid, eenheden_sterren
from terrein import *
from route import kan_ik_tot_hier
# import AI
from munitie import *
punten = 0
terijn_namen = ['Gras', 'Bos', 'Water', 'Berg', 'Weg', 'Brug', 'Gebouw']
terijn_eigenschapen = [[], ['berijk - 2', 'zichtbaar + 3'], ['verdedigen - 20'], ['verdedigen + 5', 'berijk + 2', 'zicht + 4', 'zichtbaar - 2'], [], [], ['verdedigen + 5']]
bouwmogelijkheden = [['gracht', 'verspering', 'hek', 'weg'], ['omhaken', '', '', ''], ['brug', '', '', ''], ['toren', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
eenheid_namen = ['zwaard', 'speer ', 'paard ', 'kanon ', 'boog  ', 'ingenieur ']
uithouding_terugkrijgen_type = [1, 1, 2, 1, 1, 3]
uithouding_terugkrijgen_nivo = [1, 1.5, 2, 2.5]
uithouding_terijn = [1, 1.5, 3, 2, 0.5, 0.5, 1]

MENU = 0
DOEL = 1
BEGIN = 2
VERLOOP_EN_EINDE = 3
TERREIN = 4
EENHEDEN = 5
BOOTEN = 6
AANVALLEN = 7
MUNITIE = 8
UITHOUDING_EN_BEWEGEN = 9
ZICHT_EENHEDEN = 10
ZICHT_TERREIN = 11
KNOPPEN = 12
TERREININSTELLINGEN = 13




class Game():
    def __init__(self):
        self.breedte = 256 # globaal - grootte venster
        self.hoogte = 256 #
        pyxel.init(self.breedte, self.hoogte) #
        pyxel.load('tekeningen.pyxres') #
        # pyxel.playm(0, loop=True) #
        self.game_breedte = 512 # grootte kaart
        self.game_hoogte = 512 #
        self.eenheiden = [[], [], [], [], []] # eenheden - 1 per vakje. Max 5 spelers
        self.begin_eenheiden = [[], [], [], [], []] #
        self.dode_eenheiden = [[], [], [], [], []] #
        self.x = 0 # actieve coordinaat onder muispointer
        self.y = 0 #
        self.type = 0 #
        self.nivo = 0 #
        self.kleur = 0 #
        self.geselecterde_kleur = 0 #
        self.lijst_met_eenheidkleuren = [1, 2, 7, 8, 10] #
        self.lijst_met_terijnkleuren = [11, 3, 6, 13, 15, 4, 14, 13, 4] #
        self.begin_eenheiden_punten = [48, 48, 48, 48, 48] #
        self.eenheiden_punten = [48, 48, 48, 48, 48] #
        self.begin_max_aantal_eenheiden = [5, 2, 2, 1, 1, 1] #
        self.max_aantal_eenheiden = [5, 2, 2, 1, 1, 1] #
        self.begin_max_aantal_eenheiden_boot = [3, 9] #
        self.max_aantal_eenheiden_boot = [3, 9] #
        self.aantal_eenheiden_geplaatst = [0,  0,  0, 0, 0, 0] #
        self.begin_max_aantal_eenheiden_nivo = [8, 4,  1, 1] #
        self.max_aantal_eenheden_nivo = [8, 4, 1, 1] #
        self.aantal_eenheden_geplaatst_nivo = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] #
        self.begin_max_aantal_eenheden_geplaatst_punten = [
            [[6, 5, 5, 0, 2, 0], [8, 2, 3, 2, 2, 1], [6, 3, 4, 2, 2, 1], [6, 4, 5, 0, 2, 1], [3, 5, 6, 1, 2, 1]],
            [[6, 2, 6, 1, 2, 1], [5, 2, 5, 2, 2, 2], [9, 1, 4, 1, 2, 1], [6, 2, 5, 1, 3, 1], [3, 7, 5, 0, 2, 1]],
            [[8, 1, 5, 2, 1, 1], [6, 1, 5, 2, 2, 2], [6, 4, 5, 1, 1, 1], [8, 1, 5, 2, 1, 1], [4, 5, 4, 2, 2, 1]],
            [[3, 6, 4, 3, 1, 1], [1, 7, 4, 4, 1, 1], [9, 1, 4, 1, 2, 1], [4, 6, 4, 2, 1, 1], [3, 7, 5, 0, 2, 1]],
        ] #
        self.max_aantal_eenheiden_geplaatst_punten = [
            [[6, 5, 5, 0, 2, 0], [8, 2, 3, 2, 2, 1], [6, 3, 4, 2, 2, 1], [6, 4, 5, 0, 2, 1], [3, 5, 6, 1, 2, 1]],
            [[6, 2, 6, 1, 2, 1], [5, 2, 5, 2, 2, 2], [9, 1, 4, 1, 2, 1], [6, 2, 5, 1, 3, 1], [3, 7, 5, 0, 2, 1]],
            [[8, 1, 5, 2, 1, 1], [6, 1, 5, 2, 2, 2], [6, 4, 5, 1, 1, 1], [8, 1, 5, 2, 1, 1], [4, 5, 4, 2, 2, 1]],
            [[3, 6, 4, 3, 1, 1], [1, 5, 5, 5, 1, 1], [9, 1, 4, 1, 2, 1], [4, 6, 4, 2, 1, 1], [3, 7, 5, 0, 2, 1]],
        ] #
        self.aantal_eenheiden_geplaatst_punten = [[0,  0,   0, 0, 0, 0], [0,  0,  0, 0, 0, 0], [ 0,  0,  0, 0, 0, 0], [0,  0,  0, 0, 0, 0], [0,  0, 0, 0, 0, 0]] #
        self.eenheden_aan_het_plaatsen = True #
        self.is_gedaan = False #
        self.toon_kaart = True #
        self.begin_teken_x = 0 #
        self.begin_teken_y = 0 #
        self.grootte = 2 #
        self.ondergrond_zicht = [5, 9, 5, 0, 5, 5, 5] #
        self.geselecteerde_eenheid = None #
        self.schietanimatie = 1000 #
        self.duur_schietanimatie = 32 #
        self.schietanimatie_x = 160 #
        self.schietanimatie_y = 0 #
        self.schietrichting_x = 0 #
        self.schietrichting_y = 0 #
        self.einde_schietanimatie_x = 0 #
        self.einde_schietanimatie_y = 0 #
        self.team_1 = -1 #
        self.team_2 = -1 #
        self.balansen = [0, 0, 0, 0, 0] #
        self.volgende_beurt = False #
        self.toon_menu = False #
        self.toon_info = False #
        self.startgebied = False #
        self.lijst_met_blokcordinaten = [
            [[2, 13, 7], [3, 13, 7], [4, 13, 7], [5, 13, 7], [6, 13, 7], [7, 13, 7], [8, 13, 8], [9, 13, 8], [10, 13, 8], [11, 13, 8], [12, 13, 8], [13, 13, 8]],
            [[2, 12, 7], [13, 12, 8]],
            [[2, 11, 7], [3, 11, 7], [4, 11, 7], [5, 11, 7], [6, 11, 7], [7, 11, 7], [8, 11, 8], [9, 11, 8], [10, 11, 8], [11, 11, 8], [12, 11, 8], [13, 11, 8]],
            [[2, 10, 7], [13, 10, 8]],
            [[2, 9, 7], [3, 9, 7], [4, 9, 7], [5, 9, 7], [6, 9, 7], [7, 9, 7], [8, 9, 8], [9, 9, 8], [10, 9, 8], [11, 9, 8], [12, 9, 8], [13, 9, 8]],
            [[2, 6, 7], [3, 6, 7], [4, 6, 7], [5, 6, 7], [7, 6, 7], [8, 6, 8], [10, 6, 8], [11, 6, 8], [12, 6, 8], [13, 6, 8]],
            [[7, 5, 7], [8, 5, 8]],
            [[2, 4, 7], [3, 4, 7], [4, 4, 7], [5, 4, 7], [6, 4, 7], [7, 4, 7], [8, 4, 8], [9, 4, 8], [10, 4, 8], [11, 4, 8], [12, 4, 8], [13, 4, 8]],
            ] #
        self.aan_het_spelen = False #
        self.blokken = [] #
        for rij in self.lijst_met_blokcordinaten: #
            for cordinaten in rij: #
                newblok = Blok(cordinaten[0] * 16, cordinaten[1] * 16, cordinaten[2]) #
                self.blokken.append(newblok) #
        self.lijst_met_terijnblokken = [] #
        self.animatie = Animatie() #
        self.laats_geselekteerde_eenheid = -1 #
        self.T = 1 #
        self.menu_pagina = 0 #
        self.aantal_menu_paginas = 13 #
        self.rivier_kans = 4 #
        self.rivier_grote = 0 #
        self.weg_kans = 3 #
        self.weg_grote = 0 #
        self.bos_kans = 5 #
        self.bos_grote = 4 #
        self.berg_kans = 3 #
        self.berg_grote = 4 #
        self.gebouw_aantal = 5 #
        self.gebouw_grote = 4 #
        self.meer_kans = 3 #
        self.meer_grote = 4 #
        self.zee_kans = 1 #
        self.zee_grote = 4 #
        self.ai = 0 #
        self.boot = 0 #
        self.munieties = [] #
        self.aan_het_bouwen = False #
        self.bouwsels = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ] #
        self.bouwsel = 0 #
        self.aantal_gestorven = [0, 0] #


    def nieuw_eenheid(self, k, t, n, x, y, T, B):
        neweenheid = Eenheid(k, t, n, x, y, T, B)
        self.eenheiden[k].append(neweenheid)

    def balans(self, gew_team, ver_team, nivo):
        if self.balansen[gew_team] < 12:
            nivo += 1
            nivo /= 12
            self.balansen[gew_team] += nivo
            self.balansen[ver_team] -= nivo
            # print(self.balansen)

    def update(self):
        pyxel.fullscreen(True)
        if pyxel.btnp(pyxel.KEY_TAB):
            for i, eenheid in enumerate(self.eenheiden[self.geselecterde_kleur]):
                if not eenheid.is_geweest and i > self.laats_geselekteerde_eenheid:
                    for ii, eenheid2 in enumerate(self.eenheiden[self.geselecterde_kleur]):
                        eenheid2.is_geselecteerd = False
                    eenheid.is_geselecteerd = True
                    self.laats_geselekteerde_eenheid = i
                    # print(i, self.laats_geselekteerde_eenheid)
                    self.begin_teken_x = -eenheid.x // 16 + self.breedte // 32
                    self.begin_teken_y = -eenheid.y // 16 + self.breedte // 32
                    break
            if not self.eenheden_aan_het_plaatsen:
                if i + 1 >= len(self.eenheiden[self.geselecterde_kleur]):
                    self.laats_geselekteerde_eenheid = -1


        # if pyxel.btnp(pyxel.KEY_B):
        #     self.aan_het_spelen = not self.aan_het_spelen

        if pyxel.btnp(pyxel.KEY_SPACE):
            if self.geselecteerde_eenheid:
                self.geselecteerde_eenheid.is_geweest = True
                self.geselecteerde_eenheid.is_geselecteerd = False

        pyxel.mouse(True)
        # print(pyxel.mouse_x, ":" , pyxel.mouse_y)
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT):
            pyxel.mouse(False)
        else:
            pyxel.mouse(True)

        self.x = (pyxel.mouse_x // 16) * 16
        self.y = (pyxel.mouse_y // 16) * 16
        self.aangepaste_x = self.x + self.begin_teken_x * -16
        self.aangepaste_y = self.y + self.begin_teken_y * -16
        # print(self.x, self.y, self.aangepaste_x, self.aangepaste_y)

        self.terrein = getTerrein()

# menu
        if pyxel.btnp(pyxel.KEY_M):
            self.toon_menu = not self.toon_menu
        if self.toon_menu:
            if self.menu_pagina == MENU:
                if 0 < pyxel.mouse_x < 128 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    if  12 + DOEL * 10  < pyxel.mouse_y < 22 + DOEL * 10:
                        self.menu_pagina = DOEL
                    if  12 + BEGIN * 10 < pyxel.mouse_y <  22 + BEGIN * 10:
                        self.menu_pagina = BEGIN
                    if  12 + VERLOOP_EN_EINDE * 10 < pyxel.mouse_y <  22 + VERLOOP_EN_EINDE * 10:
                        self.menu_pagina = VERLOOP_EN_EINDE
                    if  12 + TERREIN * 10 < pyxel.mouse_y <  22 + TERREIN * 10:
                        self.menu_pagina = TERREIN
                    if  12 + EENHEDEN * 10 < pyxel.mouse_y <  22 + EENHEDEN * 10:
                        self.menu_pagina = EENHEDEN
                    if  12 + BOOTEN * 10 < pyxel.mouse_y <  22 + BOOTEN * 10:
                        self.menu_pagina = BOOTEN
                    if  12 + AANVALLEN * 10 < pyxel.mouse_y <  22 + AANVALLEN * 10:
                        self.menu_pagina = AANVALLEN
                    if  12 + MUNITIE * 10 < pyxel.mouse_y <  22 + MUNITIE * 10:
                        self.menu_pagina = MUNITIE
                    if  12 + UITHOUDING_EN_BEWEGEN * 10 < pyxel.mouse_y <  22 + UITHOUDING_EN_BEWEGEN * 10:
                        self.menu_pagina = UITHOUDING_EN_BEWEGEN
                    if  12 + ZICHT_EENHEDEN * 10 < pyxel.mouse_y < 22 + ZICHT_EENHEDEN * 10:
                        self.menu_pagina = ZICHT_EENHEDEN
                    if 12 + ZICHT_TERREIN * 10 < pyxel.mouse_y < 22 + ZICHT_TERREIN * 10:
                        self.menu_pagina = ZICHT_TERREIN
                    if 12 + KNOPPEN * 10 < pyxel.mouse_y < 22 + KNOPPEN * 10:
                        self.menu_pagina = KNOPPEN
                    if 12 + TERREININSTELLINGEN * 10 < pyxel.mouse_y < 22 + TERREININSTELLINGEN * 10:
                        self.menu_pagina = TERREININSTELLINGEN
            if 2 < pyxel.mouse_y < 12 and 0 < pyxel.mouse_x < 128 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.menu_pagina = MENU
            if self.menu_pagina == TERREININSTELLINGEN:
                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    #weg
                    if  78 <= pyxel.mouse_x <=  86 and 32 <= pyxel.mouse_y <= 40 and self.weg_kans > 0:
                        self.weg_kans -= 1
                    if  94 <= pyxel.mouse_x <= 102 and 32 <= pyxel.mouse_y <= 40 and self.weg_kans < 9:
                        self.weg_kans += 1
                    if 178 <= pyxel.mouse_x <= 186 and 32 <= pyxel.mouse_y <= 40 and self.weg_grote > 0:
                        self.weg_grote -= 1
                    if 194 <= pyxel.mouse_x <= 202 and 32 <= pyxel.mouse_y <= 40 and self.weg_grote < 9:
                        self.weg_grote += 1

                    #rivier
                    if  78 <= pyxel.mouse_x <=  86 and 42 <= pyxel.mouse_y <= 50 and self.rivier_kans > 0:
                        self.rivier_kans -= 1
                    if  94 <= pyxel.mouse_x <= 102 and 42 <= pyxel.mouse_y <= 50 and self.rivier_kans < 9:
                        self.rivier_kans += 1
                    if 178 <= pyxel.mouse_x <= 186 and 42 <= pyxel.mouse_y <= 50 and self.rivier_grote > 0:
                        self.rivier_grote -= 1
                    if 194 <= pyxel.mouse_x <= 202 and 42 <= pyxel.mouse_y <= 50 and self.rivier_grote < 9:
                        self.rivier_grote += 1

                    #bos
                    if  78 <= pyxel.mouse_x <=  86 and 52 <= pyxel.mouse_y <= 60 and self.bos_kans > 0:
                        self.bos_kans -= 1
                    if  94 <= pyxel.mouse_x <= 102 and 52 <= pyxel.mouse_y <= 60 and self.bos_kans < 9:
                        self.bos_kans += 1
                    if 178 <= pyxel.mouse_x <= 186 and 52 <= pyxel.mouse_y <= 60 and self.bos_grote > 0:
                        self.bos_grote -= 1
                    if 194 <= pyxel.mouse_x <= 202 and 52 <= pyxel.mouse_y <= 60 and self.bos_grote < 9:
                        self.bos_grote += 1

                    #berg
                    if  78 <= pyxel.mouse_x <=  86 and 62 <= pyxel.mouse_y <= 70 and self.berg_kans > 0:
                        self.berg_kans -= 1
                    if  94 <= pyxel.mouse_x <= 102 and 62 <= pyxel.mouse_y <= 70 and self.berg_kans < 9:
                        self.berg_kans += 1
                    if 178 <= pyxel.mouse_x <= 186 and 62 <= pyxel.mouse_y <= 70 and self.berg_grote > 0:
                        self.berg_grote -= 1
                    if 194 <= pyxel.mouse_x <= 202 and 62 <= pyxel.mouse_y <= 70 and self.berg_grote < 9:
                        self.berg_grote += 1

                    #meer
                    if  78 <= pyxel.mouse_x <=  86 and 72 <= pyxel.mouse_y <= 80 and self.meer_kans > 0:
                        self.meer_kans -= 1
                    if  94 <= pyxel.mouse_x <= 102 and 72 <= pyxel.mouse_y <= 80 and self.meer_kans < 9:
                        self.meer_kans += 1
                    if 178 <= pyxel.mouse_x <= 186 and 72 <= pyxel.mouse_y <= 80 and self.meer_grote > 0:
                        self.meer_grote -= 1
                    if 194 <= pyxel.mouse_x <= 202 and 72 <= pyxel.mouse_y <= 80 and self.meer_grote < 9:
                        self.meer_grote += 1

                    #zee
                    if  78 <= pyxel.mouse_x <=  86 and 82 <= pyxel.mouse_y <= 90 and self.zee_kans > 0:
                        self.zee_kans -= 1
                    if  94 <= pyxel.mouse_x <= 102 and 82 <= pyxel.mouse_y <= 90 and self.zee_kans < 9:
                        self.zee_kans += 1
                    if 178 <= pyxel.mouse_x <= 186 and 82 <= pyxel.mouse_y <= 90 and self.zee_grote > 0:
                        self.zee_grote -= 1
                    if 194 <= pyxel.mouse_x <= 202 and 82 <= pyxel.mouse_y <= 90 and self.zee_grote < 9:
                        self.zee_grote += 1

                    #gebouwen
                    if  78 <= pyxel.mouse_x <=  86 and 92 <= pyxel.mouse_y <= 100 and self.gebouw_aantal > 0:
                        self.gebouw_aantal -= 1
                    if  94 <= pyxel.mouse_x <= 102 and 92 <= pyxel.mouse_y <= 100 and self.gebouw_aantal < 9:
                        self.gebouw_aantal += 1
                    if 178 <= pyxel.mouse_x <= 186 and 92 <= pyxel.mouse_y <= 100 and self.gebouw_grote > 0:
                        self.gebouw_grote -= 1
                    if 194 <= pyxel.mouse_x <= 202 and 92 <= pyxel.mouse_y <= 100 and self.gebouw_grote < 9:
                        self.gebouw_grote += 1

            if pyxel.btnp(pyxel.KEY_LEFT) and self.menu_pagina != KNOPPEN:
                self.menu_pagina -= 1
                if self.menu_pagina < 0:
                    self.menu_pagina = self.aantal_menu_paginas
            if pyxel.btnp(pyxel.KEY_RIGHT) and self.menu_pagina != KNOPPEN:
                self.menu_pagina += 1
                if self.menu_pagina > self.aantal_menu_paginas:
                    self.menu_pagina = 0
            if pyxel.mouse_wheel > 0:
                self.menu_pagina -= 1
                if self.menu_pagina < 0:
                    self.menu_pagina = self.aantal_menu_paginas
            if pyxel.mouse_wheel < 0:
                self.menu_pagina += 1
                if self.menu_pagina > self.aantal_menu_paginas:
                    self.menu_pagina = 0


        if not self.toon_menu:
# info
            if pyxel.btnp(pyxel.KEY_I):
                self.toon_info = not self.toon_info
# scherm bewegen
            if self.x >= self.breedte:
                self.begin_teken_x -= 1
            if self.x <= -16:
                self.begin_teken_x += 1
            if self.y >= self.hoogte:
                self.begin_teken_y -= 1
            if self.y <= -16:
                self.begin_teken_y += 1

#terijn kleiner / grooter
            # if pyxel.btnp(pyxel.KEY_A):
            #     if self.grootte > 1:
            #         self.game_breedte -= 256
            #         self.game_hoogte -= 256
            #         self.grootte -= 1
            # if pyxel.btnp(pyxel.KEY_Z):
            #     if self.grootte < 16:
            #         self.game_breedte += 256
            #         self.game_hoogte += 256
            #         self.grootte += 1

# minder / meer punten
            if pyxel.btnp(pyxel.KEY_Q):
                for i in range(0, len(self.eenheiden_punten)):
                    if self.eenheiden_punten[i] > 12:
                        self.eenheiden_punten[i] -= 12
                        self.begin_eenheiden_punten[i] -= 12
            if pyxel.btnp(pyxel.KEY_S):
                mag_ik_exta_punten = True
                for kleur in (self.aantal_eenheden_geplaatst_nivo):
                    for ii in kleur:
                        if ii != 0:
                            mag_ik_exta_punten = False
                for i in range(0, len(self.eenheiden_punten)):
                    if self.eenheiden_punten[i] < 96 and mag_ik_exta_punten:
                        self.eenheiden_punten[i] += 12
                        self.begin_eenheiden_punten[i] += 12
            for i, tijd in enumerate(self.max_aantal_eenheiden_geplaatst_punten):
                for ii, kleur in enumerate(tijd):
                    for iii, type in enumerate(kleur):
                        self.max_aantal_eenheiden_geplaatst_punten[i][ii][iii] = self.begin_max_aantal_eenheden_geplaatst_punten[i][ii][iii] * self.begin_eenheiden_punten[0] // 12
            for i in range(0, len(self.max_aantal_eenheiden)):
                self.max_aantal_eenheiden[i] = self.begin_max_aantal_eenheiden[i] * self.begin_eenheiden_punten[0] // 12
            for i in range(0, len(self.max_aantal_eenheden_nivo)):
                self.max_aantal_eenheden_nivo[i] = self.begin_max_aantal_eenheiden_nivo[i] * self.begin_eenheiden_punten[0] // 12
            self.max_aantal_eenheden_nivo[3] = 1

# randomterijn
            if pyxel.btn(pyxel.KEY_R):
                randomterrein(self)

# kaart
            if pyxel.btnp(pyxel.KEY_K):
                self.toon_kaart = not self.toon_kaart

# volgende kleur
            if pyxel.btnp(pyxel.KEY_C):
                if self.kleur < 4:
                    self.kleur += 1
                else:
                    self.kleur = 0
                self.aantal_eenheiden_geplaatst = [0, 0, 0, 0, 0, 0]
                for eenheid in self.eenheiden[self.geselecterde_kleur]:
                    eenheid.is_geweest = False
                    eenheid.is_zichtbaar = False
                self.geselecterde_kleur += 1
                if self.geselecterde_kleur > 4:
                    self.geselecterde_kleur = 0


# eenheid veranderen
            if pyxel.btnp(pyxel.KEY_UP):
                if self.nivo < 3:
                    self.nivo += 1
                else:
                    self.nivo = 0
            if pyxel.btnp(pyxel.KEY_DOWN):
                if self.nivo > 0:
                    self.nivo -= 1
                else:
                    self.nivo = 3
            if pyxel.btnp(pyxel.KEY_RIGHT):
                if self.boot:
                    if self.type < 1:
                        self.type += 1
                    else:
                        self.type = 0
                else:
                    if self.type < 5:
                        self.type += 1
                    else:
                        self.type = 0
            if pyxel.btnp(pyxel.KEY_LEFT):
                if self.boot:
                    if self.type > 0:
                        self.type -= 1
                    else:
                        self.type = 1
                else:
                    if self.type > 0:
                        self.type -= 1
                    else:
                        self.type = 5

# aanvallen
            if pyxel.btnr(pyxel.MOUSE_BUTTON_RIGHT):
                self.val_aan()
                if self.eenheden_aan_het_plaatsen:
                    for i, kleur in enumerate(self.eenheiden):
                        for eenheid in kleur:
                            if eenheid.x == self.aangepaste_x and eenheid.y == self.aangepaste_y:
                                self.eenheiden[self.geselecterde_kleur].remove(eenheid)
                                self.eenheiden_punten[self.geselecterde_kleur] += eenheid.nivo + 1
                                self.aantal_eenheden_geplaatst_nivo[self.geselecterde_kleur][eenheid.nivo] -= 1
                                self.aantal_eenheiden_geplaatst_punten[self.geselecterde_kleur][eenheid.welk_type] -= eenheid.nivo + 1


            if self.eenheden_aan_het_plaatsen:
                if pyxel.btnp(pyxel.KEY_KP_0):
                    self.T = 0
                if pyxel.btnp(pyxel.KEY_KP_1):
                    self.T = 1
                if pyxel.btnp(pyxel.KEY_KP_2):
                    self.T = 2
                if pyxel.btnp(pyxel.KEY_KP_3):
                    self.T = 3
                for eenheid in self.eenheiden[self.geselecterde_kleur]:
                    eenheid.is_zichtbaar = True

            self.voorbeeldeenheid = Eenheid(self.kleur, self.type, self.nivo, 240, 0, self.T, self.boot)
            self.voorbeeldeenheid.is_zichtbaar = True
            if pyxel.btnp(pyxel.KEY_P):
                self.eenheden_aan_het_plaatsen = not self.eenheden_aan_het_plaatsen
                if not self.eenheden_aan_het_plaatsen:
                    for i, kleur in enumerate(self.eenheiden):
                        for eenheid in kleur:
                            self.begin_eenheiden[i].append(eenheid)

            for i, kleur in enumerate(self.eenheiden):
                for eenheid in kleur:
                    for bezige_eenheid in self.eenheiden[self.geselecterde_kleur]:
                        x_verchil = abs(eenheid.x - bezige_eenheid.x)
                        y_verchil = abs(eenheid.y - bezige_eenheid.y)
                        verchil = x_verchil + y_verchil
                        if (bezige_eenheid.zicht - verchil / 16) >= eenheid.zichtbaar and eenheid.kleur != bezige_eenheid.kleur:
                            eenheid.is_zichtbaar = True

#bouwen
            # print(f"x{pyxel.mouse_x}")
            # print(f"y{pyxel.mouse_y}")
            if pyxel.btnp(pyxel.MOUSE_BUTTON_MIDDLE) and self.aan_het_bouwen:
                self.aan_het_bouwen = False

            if self.geselecteerde_eenheid != None:
                self.vorig_geselecterde_eenhijd = self.geselecteerde_eenheid.kan_ik_bouwen == 1
                if self.aan_het_bouwen:
                    self.geselecteerde_eenheid.is_geselecteerd = False

                if pyxel.btnp(pyxel.MOUSE_BUTTON_MIDDLE):
                    if self.vorig_geselecterde_eenhijd == 1:
                        if not self.aan_het_bouwen:
                            self.x_geselecteerde_eenheid = self.geselecteerde_eenheid.x // 16
                            self.y_geselecteerde_eenheid = self.geselecteerde_eenheid.y // 16
                            self.geselecteerde_eenheid.is_geselecteerd = False
                        self.aan_het_bouwen = not self.aan_het_bouwen



            if self.aan_het_bouwen:
                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    vlakterijn = getTerrein()
                    if 88 <= pyxel.mouse_x <= 126 and 88 <= pyxel.mouse_y <= 126:
                        self.bouwsel += 1
                    if 129 <= pyxel.mouse_x <= 167 and 88 <= pyxel.mouse_y <= 126:
                        self.bouwsel += 2
                    if 88 <= pyxel.mouse_x <= 126 and 129 <= pyxel.mouse_y <= 167:
                        self.bouwsel += 3
                    if 129 <= pyxel.mouse_x <= 167 and 129 <= pyxel.mouse_y <= 167:
                        self.bouwsel += 4
                        #88, 88: 126, 126; 129, 88: 167, 126; 88, 129: 126, 167; 129, 129: 167, 167
                    self.bouwsel += self.terrein[self.y_geselecteerde_eenheid][self.x_geselecteerde_eenheid] * 4
                    self.bouwsels[self.y_geselecteerde_eenheid][self.x_geselecteerde_eenheid] = self.bouwsel
                    if vlakterijn[self.y_geselecteerde_eenheid][self.x_geselecteerde_eenheid] == 2 and self.bouwsel == 9:
                        vlakterijn[self.y_geselecteerde_eenheid][self.x_geselecteerde_eenheid] = 5
                    if vlakterijn[self.y_geselecteerde_eenheid][self.x_geselecteerde_eenheid] == 0 and self.bouwsel == 4:
                        vlakterijn[self.y_geselecteerde_eenheid][self.x_geselecteerde_eenheid] = 4
                    if vlakterijn[self.y_geselecteerde_eenheid][self.x_geselecteerde_eenheid] == 1 and self.bouwsel == 5:
                        vlakterijn[self.y_geselecteerde_eenheid][self.x_geselecteerde_eenheid] = 0
                    self.aan_het_bouwen = False
                print(self.bouwsel)
                self.bouwsel = 0




# volgende beurt
            if pyxel.btnp(pyxel.KEY_KP_ENTER) and not self.toon_menu:
                self.volgendebeurt()

# eenheid verplaatsen
            if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
                if self.aan_het_spelen:
                    # pyxel.play(5)
                    if self.toon_kaart:
                        # naar punt op kaart gaan
                        if pyxel.mouse_x <= self.grootte * 16 >= pyxel.mouse_y :
                            self.begin_teken_x = -pyxel.mouse_x + 8
                            self.begin_teken_y = -pyxel.mouse_y + 8
                        else:
                            self.eenheid_plaatsen_of_verplaatsen()
                    else:
                        self.eenheid_plaatsen_of_verplaatsen()

            for eenheid in self.eenheiden[self.geselecterde_kleur]:
                if eenheid.is_geselecteerd:
                    self.geselecteerde_eenheid = eenheid
                    break
                else:
                    self.geselecteerde_eenheid = None

            for i, kleur in enumerate(self.eenheiden):
                for eenheid in kleur:
                    eenheid.update(self)
                        # self.geselecterde_eenhuid_aanval = eenheid.aanvalen
                        # self.geselecterde_eenhuid_berijk = eenheid.berijk
                        # self.geselecterde_eenhuid_verschil = eenheid.vershil / 16
                        # self.geselecterde_eenhuid_moraalaanval = eenheid.aanvalen_moraal
                        # self.geselecterde_eenheid_x = eenheid.x
                        # self.geselecterde_eenheid_y = eenheid.y
                        # self.geselecterde_eenheid_bewegen = eenheid.bewegen
                    if eenheid.gezondheid <= 0 or eenheid.moraal <= 0:
                        self.dode_eenheiden[i].append(eenheid)
                        eenheid.is_zichtbaar = True
                        self.aantal_eenheden_geplaatst_nivo[i][eenheid.nivo] -= 1
                        self.eenheiden[i].remove(eenheid)
            aantal_beginkleuren = 0
            for i, kleur in enumerate(self.eenheiden):
                if len(self.begin_eenheiden[i]) > 0:
                    aantal_beginkleuren += 1
            aantal_kleuren = aantal_beginkleuren
            for i, kleur in enumerate(self.eenheiden):
                if len(kleur) == 0 and len(self.begin_eenheiden[i]) > 0:
                    aantal_kleuren -= 1
            if aantal_kleuren == 1:
                self.is_gedaan = True
                print(self.aantal_gestorven)
                # self.begin_teken_x = 0
                # self.begin_teken_y = 0
        if pyxel.btnp(pyxel.KEY_G):
            self.is_gedaan = True
        if self.breedte -16 == self.x and self.hoogte - 16 == self.y and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.toon_menu = not self.toon_menu
        if self.toon_menu:
            if (self.breedte // 2) - 16 == self.x and self.hoogte - 32 <= self.y <= self.hoogte - 16 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.menu_pagina -= 1
                if self.menu_pagina < 0:
                    self.menu_pagina = self.aantal_menu_paginas
            if (self.breedte // 2) == self.x  and self.hoogte - 32 <= self.y <= self.hoogte - 16 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.menu_pagina += 1
                if self.menu_pagina > self.aantal_menu_paginas:
                    self.menu_pagina = 0

        for munitie in self.munieties:
            munitie.update()


        if pyxel.btnp(pyxel.KEY_W):
            tegellijst = []
            for y, rij in enumerate(self.lijst_met_terijnblokken):
                for x, tegel in enumerate(rij):
                    tegellijst.append(tegel.ben_ik_zichtbaar)
                    tegellijst.append(self.terrein[y][x])
                print(tegellijst)
                tegellijst = []
            print('_______________________________________________________________________________________________________________________________________________________________________')


        # if pyxel.btnp(pyxel.KEY_K):
        #     self.ai = AI.AI(self.eenheiden[self.team_1])
        # if self.ai != 0:
        #     self.ai.update(self)

        if pyxel.btnp(pyxel.KEY_B):
            self.boot = not self.boot
            self.type = 0



    def draw(self):
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        pyxel.cls(0)

        if not self.aan_het_spelen:
            for blok in self.blokken:
                blok.start_animatie(self)
                self.terrein = getTerrein()
                # self.animatie.update()
        else:

            if self.eenheden_aan_het_plaatsen and not self.toon_menu:
                if not self.startgebied:
                    self.x_pos_start = abs((random.triangular(0, self.breedte) // 16) - self.breedte // 24)
                    self.y_pos_start = abs((random.triangular(0, self.hoogte) // 16))
                    self.startgebied = True
                if self.team_2 < 0 and self.team_1 < 0 or self.geselecterde_kleur == self.team_1:
                    pyxel.rect((self.x_pos_start * 16) - 1 + self.begin_teken_x * 16, (self.y_pos_start * 16) - 1 + self.begin_teken_y * 16, ((1 + self.grootte) * 16) + 1, (self.hoogte - (self.grootte * 6)) - 3, self.lijst_met_eenheidkleuren[self.geselecterde_kleur])
                    # pyxel.rect(self.x_pos_start * 16 + self.begin_teken_x * 16, self.y_pos_start * 16 + self.begin_teken_y * 16, (1 + self.groote) * 16 - 1, self.hoogte - (self.groote * 6) - 5, 0)
                else:
                    pyxel.rect((self.game_breedte - ((1 + self.grootte) * 16)) - ((self.x_pos_start * 16) + 1 - self.begin_teken_x * 16), (self.y_pos_start * 16) - 1 + self.begin_teken_y * 16, ((1 + self.grootte) * 16) + 1, (self.hoogte - (self.grootte * 6)) - 3, self.lijst_met_eenheidkleuren[self.geselecterde_kleur])
                    # pyxel.rect(self.game_breedte - (self.x_pos_start * 16 + self.begin_teken_x * 16), self.y_pos_start * 16 + self.begin_teken_y * 16, (1 + self.groote) * 16 - 1, self.hoogte - (self.groote * 6) - 5, 0)


# menu
            if self.toon_menu:
                pyxel.blt((self.breedte // 2) - 16, self.hoogte - 32, 2, 64, 0, 16, 16, pyxel.COLOR_BLACK)
                pyxel.blt((self.breedte // 2) + 0, self.hoogte - 32, 2, 80, 0, 16, 16, pyxel.COLOR_BLACK)
                pyxel.text((self.breedte // 2) - 32, self.hoogte - 8,f"pagina {self.menu_pagina + 1} van de {self.aantal_menu_paginas + 1}", 7)
                pyxel.text(2, 2, ' 1: menu', 7)

                if self.menu_pagina == MENU:
                    pyxel.text(2,  12, '                                                                ', 7)
                    pyxel.text(2,  22, ' 2: doel                                                        ', 7)
                    pyxel.text(2,  32, ' 3: begin                                                       ', 7),
                    pyxel.text(2,  42, ' 4: verloop en einde                                            ', 7)
                    pyxel.text(2,  52, ' 5: terrein                                                     ', 7),
                    pyxel.text(2,  62, ' 6: eenheden                                                    ', 7),
                    pyxel.text(2,  72, ' 7: boten                                                       ', 7),
                    pyxel.text(2,  82, ' 8: aanvallen                                                   ', 7)
                    pyxel.text(2,  92, ' 9: munitie                                                     ', 7)
                    pyxel.text(2, 102, '10: uithouding en bewegen                                       ', 7)
                    pyxel.text(2, 112, '11: zicht: eenheden                                             ', 7)
                    pyxel.text(2, 122, '12: zicht: terrein                                              ', 7)
                    pyxel.text(2, 132, '13: knoppen                                                     ', 7)
                    pyxel.text(2, 142, '14: terreininstellingen                                         ', 7)
                    pyxel.text(2, 152, '                                                                ', 7)
                    pyxel.text(2, 162, '                                                                ', 7)
                    pyxel.text(2, 172, '                                                                ', 7)
                    pyxel.text(2, 182, '                                                                ', 7)
                    pyxel.text(2, 192, '                                                                ', 7)
                    pyxel.text(2, 202, '                                                                ', 7)
                    pyxel.text(2, 212, '                                                                ', 7)
                if self.menu_pagina == DOEL:
                    pyxel.text(2,  12, 'Doel                                                            ', 7)
                    pyxel.text(2,  22, 'Het doel van het spel is om het leger van de vijand te verslaan ', 7)
                    pyxel.text(2,  32, 'Dit doe je door eenheden te plaatsen                            ', 7)
                    pyxel.text(2,  42, 'en je tegenstander aan te vallen                                ', 7)
                    pyxel.rect(0, 18, self.breedte, 1, 7)
                if self.menu_pagina == BEGIN:
                    pyxel.text(2,  12, 'Begin                                                           ', 7)
                    pyxel.text(2,  22, '  - Je hebt vanaf de start een terrein                          ', 7)
                    pyxel.text(2,  32, '       Wil je een ander random terrein? Druk op                 ', 7), pyxel.text(190, 32, '(R)', 10)
                    pyxel.text(2,  42, '  - Je kiest een budget.                                        ', 7)
                    pyxel.text(2,  52, '      Dit zie je naast de letter p in de rechterbovenhoek       ', 7),
                    pyxel.text(2,  62, '  - Je hebt de keuze tussen meer   of minder   punten           ', 7), pyxel.text(130, 62, '(S)', 10), pyxel.text(178, 62, '(q)', 10)
                    pyxel.text(2,  72, '      Het budget heb je nodig om eenheden te plaatsen           ', 7)
                    pyxel.text(2,  82, '  - Je kiest een kleur voor je eenheden                         ', 7), pyxel.text(158, 82, '(c)', 10)
                    pyxel.text(2,  92, 'Het aanpassen van punten,kleur,... doe je niet in het menu zelf ', 7)
                    pyxel.text(2, 102, 'Je plaatst je eenheden (linkermuisknop)                         ', 7)
                    pyxel.text(2, 112, 'hiervoor betaal je 1 punt per nivo                              ', 7)
                    pyxel.text(2, 122, 'Je eenheden verwijderen is via de rechtermuisknop               ', 7)
                    pyxel.text(2, 132, 'LET OP:                                                         ', 7)
                    pyxel.text(2, 142, 'je mag alleen een eenheid zetten als                            ', 7)
                    pyxel.text(2, 152, 'het vakje bij je muis geen kruis is                             ', 7)
                    pyxel.text(2, 162, 'Op welk nivo je jezelf bevindt (1-4)                            ', 7)
                    pyxel.text(2, 172, 'zie je aan de linkerkant van de eenheid                         ', 7)
                    pyxel.text(2, 182, 'PAS OP Je moet een generaal bij je eenheden hebben(zie eenheden)', 7)
                    pyxel.text(2, 192, 'Je kan van elk type/nivo, een beperkt aantal eenheden plaatsen  ', 7)
                    pyxel.text(2, 202, 'Als beide spelers hun eenheden hebben geplaatst                 ', 7)
                    pyxel.text(2, 212, 'druk je op   om te beginnen                                     ', 7), pyxel.text(42, 212, '(P)', 10)
                    pyxel.rect(0, 18, self.breedte, 1, 7)
                if self.menu_pagina == VERLOOP_EN_EINDE:
                    pyxel.text(2,  12, 'Verloop                                                         ', 7)
                    pyxel.text(2,  22, 'Wanneer je aan de beurt bent kan je eenheden selecteren en      ', 7)
                    pyxel.text(2,  32, 'verplaatsen of aanvallen, dit staat uitgelegd onder aanvallen   ', 7)
                    pyxel.text(2,  42, 'Om de informatie over je terrein te bekijken druk je op (i)     ', 7),pyxel.text(226, 42, '(i)', 6)
                    pyxel.text(2,  52, 'Als je een beurt wil overslaan met de geselecteerde eenheid     ', 7)
                    pyxel.text(2,  62, 'druk je op de  spatiebalk                                       ', 7), pyxel.text(62, 62, 'spatiebalk', 6)
                    pyxel.text(2,  72, 'Via  Tab  ga je naar de volgende eenheid die binnen diezelfde   ', 7), pyxel.text(22, 72, 'Tab', 6)
                    pyxel.text(2,  82, 'beurt nog niets gedaan heeft                                    ', 7)
                    pyxel.text(2,  92, 'Via enter begin of eindig je je beurt                           ', 7)
                    pyxel.text(2, 102, 'Je plaatst je eenheden (linkermuisknop)                         ', 7), pyxel.text(94, 102, '(linkermuisknop)', 6)
                    pyxel.text(2, 112, 'Selecteren en verplaatsen, doe je via de linkermuisknop         ', 7), pyxel.text(166, 112, 'linkermuisknop', 6)
                    pyxel.text(2, 122, 'Aanvallen doe je via de rechtermuisknop.                        ', 7), pyxel.text(98, 122, 'rechtermuisknop', 6)
                    pyxel.text(2, 132, 'Via de middelste muisknop kan je bouwen(acties van de ingenieur)', 7), pyxel.text(30, 132, 'middelste muisknop', 6)
                    pyxel.text(2, 142, 'Deze staan verder uitgelegd bij de eenheden                     ', 7)
                    pyxel.text(2, 152, '                                                                ', 7)
                    pyxel.text(2, 162, '                                                                ', 7)
                    pyxel.text(2, 172, 'Einde                                                           ', 7)
                    pyxel.text(2, 182, 'Als alle eenheden van een kleur verslagen zijn                  ', 7)
                    pyxel.text(2, 192, 'is het spel gedaan                                              ', 7)
                    pyxel.text(2, 202, '                                                                ', 7)
                    pyxel.text(2, 212, '                                                                ', 7)
                    pyxel.text(2, 172, '                                                                ', 7)
                    pyxel.text(2, 182, '                                                                ', 7)
                    pyxel.text(2, 192, '                                                                ', 7)
                    pyxel.text(2, 202, '                                                                ', 7)
                    pyxel.text(2, 212, '                                                                ', 7)
                    pyxel.rect(0, 18, self.breedte, 1, 7)
                    pyxel.rect(0, 178, self.breedte, 1, 7)
                if self.menu_pagina == TERREIN:
                    pyxel.text(2,  12, 'Terrein                                                         ', 7)
                    pyxel.text(2,  22, 'Er zijn 7 soorten terrein,                                      ', 7)
                    pyxel.text(2,  32, 'deze zijn te zien aan de verschillende kleuren                  ', 7)
                    pyxel.text(2,  42, '1: Gras: standaard, er verandert niets                          ', 11)
                    pyxel.text(2,  52, '2: Bos: 2 vakjes minder bereik zichtbaarheid gaat omhoog met 3  ', 3),
                    pyxel.text(2,  62, '   hierdoor kan je moeilijker gezien worden                     ', 3),
                    pyxel.text(2,  72, '3: Water: Je kan minder goed verdedigen (-20)                   ', 6)
                    pyxel.text(2,  82, '4: Berg: je kan beter verdedigen + 5,                           ', 13)
                    pyxel.text(2,  92, '   je bereik gaat omhoog (+ 2 vakjes),                          ', 13)
                    pyxel.text(2, 102, '   je zicht wordt beter waardoor je verder kan zien (+4)        ', 13)
                    pyxel.text(2, 112, '   je zichtbaarheid daalt -2, je word makkelijker gezien        ', 13)
                    pyxel.text(2, 122, '5: Weg: Je kan verder lopen                                     ', 15)
                    pyxel.text(2, 132, '6: Brug: Je kan verder lopen                                    ', 4)
                    pyxel.text(2, 142, '7: Gebouw: je kan je beter verdedigen (+5)                      ', 14)
                    pyxel.text(2, 152, '   je zichtbaarheid gaat omhoog +2, je word moeilijker gezien   ', 14)
                    pyxel.text(2, 162, '   maar je zicht daalt waardoor je minder ver kan zien (-1)     ', 14)
                    pyxel.text(2, 172, '                                                                ', 7)
                    pyxel.text(2, 182, '                                                                ', 7)
                    pyxel.text(2, 192, '                                                                ', 7)
                    pyxel.text(2, 202, '                                                                ', 7)
                    pyxel.text(2, 212, '                                                                ', 7)
                    pyxel.text(2, 172, '                                                                ', 7)
                    pyxel.text(2, 182, '                                                                ', 7)
                    pyxel.text(2, 192, '                                                                ', 7)
                    pyxel.text(2, 202, '                                                                ', 7)
                    pyxel.text(2, 212, '                                                                ', 7)
                    pyxel.rect(0, 18, self.breedte, 1, 7)
                if self.menu_pagina == EENHEDEN:
                    pyxel.text(2,  12, 'Eenheden                                                        ', 7)
                    pyxel.text(2,  22, 'Nivo I = Soldaat                                                ', 7)
                    pyxel.text(2,  32, 'Nivo II = Sergeant                                              ', 7)
                    pyxel.text(2,  42, 'Nivo III = Kapitein                                             ', 7)
                    pyxel.text(2,  52, 'Nivo IV = Generaal                                              ', 7)
                    pyxel.text(2,  62, 'Hieronder vind je de eigenschappen van de verschillende eenheden', 7),
                    pyxel.text(2,  72, '   Deze kwaliteiten zijn niet afhankelijk van de kleur          ', 7)
                    pyxel.text(2,  82, '            Zwaard| Speer| Paard| Kanon| Boogschutter| Ingenieur', 7)
                    pyxel.text(2,  92, 'Aanvallen  |+     |-     |+     |+     |             |-         ', 7)
                    pyxel.text(2, 102, 'Verdedigen |+     |++    |      |-     |-            |-         ', 7)
                    pyxel.text(2, 112, 'Bewegen    |      |      |++    |-     |nivoI+       |          ', 7)
                    pyxel.text(2, 122, 'Bereik     |      |      |      |++    |             |          ', 7)
                    pyxel.text(2, 132, 'Zicht      |      |      |nivoI+|      |             |          ', 7)
                    pyxel.text(2, 142, 'Extra      |      |      |      |      |             |bouwen    ', 7)
                    pyxel.text(2, 152, 'De waarde van je eenheden zie je rechts onderaan in dit kader   ', 7)
                    pyxel.text(2, 162, 'Let op: per kleur kan dit verschillen                           ', 7)
                    pyxel.text(2, 172, 'Ook kan je de sterkte herkennen aan de sterren rechts bovenaan  ', 7)
                    pyxel.text(2, 182, 'Extra                                                           ', 7)
                    pyxel.text(2, 192, 'Enkel de ingenieur kan ‘bouwen’                                 ', 7)
                    pyxel.text(2, 202, '   Dit betekent dat hij volgende veranderingen kan doen:        ', 7)
                    pyxel.text(2, 212, 'Bos --> gras                                                    ', 7)
                    pyxel.text(2, 222, 'Gras --> weg                                                    ', 7)
                    pyxel.text(2, 232, 'Water --> brug                                                  ', 7)
                    pyxel.rect(0, 18, self.breedte, 1, 7)
                if self.menu_pagina == BOOTEN:
                    pyxel.text(2,  12, 'Boten                                                           ', 7)
                    pyxel.text(2,  22, 'druk op   om boten te kunnen plaatsen                           ', 7),pyxel.text(30, 22, '(b)', 10)
                    pyxel.text(2,  32, 'boten kunnen alleen op water bewegen                            ', 7)
                    pyxel.text(2,  42, 'bij transportboten is het net als of er een weg onder is        ', 7)
                    pyxel.text(2,  52, 'hierdoor kunnen eenheden gemakelijker een rivier over           ', 7)
                    pyxel.text(2,  62, 'LET OP                                                          ', 7),
                    pyxel.text(2,  72, 'je kunt de eenheden niet op de boot zeten                       ', 7)
                    pyxel.text(2,  82, '                                                                ', 7)
                    pyxel.text(2,  92, '                                                                ', 7)
                    pyxel.text(2, 102, '                                                                ', 7)
                    pyxel.text(2, 112, '                                                                ', 7)
                    pyxel.text(2, 122, '                                                                ', 7)
                    pyxel.text(2, 132, '                                                                ', 7)
                    pyxel.text(2, 142, '                                                                ', 7)
                    pyxel.text(2, 152, '                                                                ', 7)
                    pyxel.text(2, 162, '                                                                ', 7)
                    pyxel.text(2, 172, '                                                                ', 7)
                    pyxel.text(2, 182, '                                                                ', 7)
                    pyxel.text(2, 192, '                                                                ', 7)
                    pyxel.text(2, 202, '                                                                ', 7)
                    pyxel.text(2, 212, '                                                                ', 7)
                    pyxel.text(2, 222, '                                                                ', 7)
                    pyxel.text(2, 232, '                                                                ', 7)
                    pyxel.rect(0, 18, self.breedte, 1, 7)
                if self.menu_pagina == AANVALLEN:
                    pyxel.text(2,  12, 'Aanvallen                                                       ', 7)
                    pyxel.text(2,  22, 'Je valt een vijand aan door op je rechtermuisknop te klikken    ', 7)
                    pyxel.text(2,  32, 'Je klikt hiervoor op de eenheid van de andere kleur             ', 7)
                    pyxel.text(2,  42, '1: algemene aanval                                              ', 7)
                    pyxel.text(2,  52, 'Om een vijand aan te vallen moet hij binnen je bereik zijn      ', 7)
                    pyxel.text(2,  62, 'Dit wil zeggen dat je naast je vijand moet staan                ', 7),
                    pyxel.text(2,  72, 'of in een rechte lijn naar je vijand moet kunnen bewegen        ', 7)
                    pyxel.text(2,  82, 'Een aanval op je vijand zorgt ervoor                            ', 7)
                    pyxel.text(2,  92, 'dat hij moraal en gezondheid verliest                           ', 7)
                    pyxel.text(2, 102, 'Tip: Een aanval met een aanloop bezorgt je vijand meer schade   ', 7)
                    pyxel.text(2, 112, 'Hoe groter de aanloop, hoe meer schade                          ', 7)
                    pyxel.text(2, 122, 'Wanneer je aanvalt is er de mogelijkheid                        ', 7)
                    pyxel.text(2, 132, 'dat de eenheid van je vijand verplaatst naar achteren           ', 7)
                    pyxel.text(2, 142, '                                                                ', 7)
                    pyxel.text(2, 152, '2 Schieten                                                      ', 7)
                    pyxel.text(2, 162, 'Om een vijand aan te vallen moet hij binnen je bereik zijn      ', 7)
                    pyxel.text(2, 172, 'Je kan op de vijand schieten wanneer er een doelwit op staat    ', 7)
                    pyxel.text(2, 182, '                                                                ', 7)
                    pyxel.text(2, 192, '                                                                ', 7)
                    pyxel.text(2, 202, '                                                                ', 7)
                    pyxel.text(2, 212, '                                                                ', 7)
                    pyxel.rect(0, 18, self.breedte, 1, 7)
                if self.menu_pagina == MUNITIE:
                    pyxel.text(2,  12, 'munitie                                                         ', 7)
                    pyxel.text(2,  22, 'de munitie van een eenheid is                                   ', 7)
                    pyxel.text(2,  32, 'het aantal keren dat het kan schieten                           ', 7)
                    pyxel.text(2,  42, 'als dit bij een boogschuter of kanon op 0 graakt                ', 7)
                    pyxel.text(2,  52, 'veranderd deze eenheid in een zwaardvechter van dat nivo        ', 7)
                    pyxel.text(2,  62, '                                                                ', 7),
                    pyxel.text(2,  72, '                                                                ', 7)
                    pyxel.text(2,  82, '                                                                ', 7)
                    pyxel.text(2,  92, '                                                                ', 7)
                    pyxel.text(2, 102, '                                                                ', 7)
                    pyxel.text(2, 112, '                                                                ', 7)
                    pyxel.text(2, 122, '                                                                ', 7)
                    pyxel.text(2, 132, '                                                                ', 7)
                    pyxel.text(2, 142, '                                                                ', 7)
                    pyxel.text(2, 152, '                                                                ', 7)
                    pyxel.text(2, 162, '                                                                ', 7)
                    pyxel.text(2, 172, '                                                                ', 7)
                    pyxel.text(2, 182, '                                                                ', 7)
                    pyxel.text(2, 192, '                                                                ', 7)
                    pyxel.text(2, 202, '                                                                ', 7)
                    pyxel.text(2, 212, '                                                                ', 7)
                    pyxel.rect(0, 18, self.breedte, 1, 7)
                if self.menu_pagina == UITHOUDING_EN_BEWEGEN:
                    pyxel.text(2,  12, 'Uithouding                                                      ', 7)
                    pyxel.text(2,  22, 'Verliezen                                                       ', 7)
                    pyxel.text(2,  32, 'Je verliest uithouding bij bewegingen                           ', 7)
                    pyxel.text(2,  42, 'De hoeveelheid hangt af van de ondergrond waarover je beweegt   ', 7)
                    pyxel.text(2,  52, '(Staat aangegeven bij de terreininformatie)                     ', 7)
                    pyxel.text(2,  62, '                                                                ', 7),
                    pyxel.text(2,  72, 'Bijkrijgen                                                      ', 7)
                    pyxel.text(2,  82, 'Je uithouding gaat terug omhoog na iedere beurt,                ', 7)
                    pyxel.text(2,  92, 'de hoeveelheid uithouding is afhankelijk van je type en nivo    ', 7)
                    pyxel.text(2, 102, '                                                                ', 7)
                    pyxel.text(2, 112, '                                                                ', 7)
                    pyxel.text(2, 122, 'Bewegen                                                         ', 7)
                    pyxel.text(2, 132, 'Als je een eenheid hebt geselecteerd die je wil verplaatsen,    ', 7)
                    pyxel.text(2, 142, 'kan je met je muis naar een vakje bewegen waar je naartoe wil   ', 7)
                    pyxel.text(2, 152, 'Wanneer dit oplicht kan je je naar dat vakje verplaatsen        ', 7)
                    pyxel.text(2, 162, '                                                                ', 7)
                    pyxel.text(2, 172, '                                                                ', 7)
                    pyxel.text(2, 182, '                                                                ', 7)
                    pyxel.text(2, 192, '                                                                ', 7)
                    pyxel.text(2, 202, '                                                                ', 7)
                    pyxel.text(2, 212, '                                                                ', 7)
                    pyxel.rect(0, 18, self.breedte, 1, 7)
                    pyxel.rect(0, 128, self.breedte, 1, 7)
                if self.menu_pagina == ZICHT_EENHEDEN:
                    pyxel.text(2,  12, 'Zicht                                                           ', 7)
                    pyxel.text(2,  22, 'Eenheden                                                        ', 7)
                    pyxel.text(2,  32, 'Je kan zien wanneer je het zicht van je eenheid                 ', 7)
                    pyxel.text(2,  42, 'min de zichtbaarheid van je vijand                              ', 7)
                    pyxel.text(2,  52, 'min het aantal vakjes verschil doet en dit groter is dan 0      ', 7)
                    pyxel.text(2,  62, 'Bijvoorbeeld                                                    ', 7),
                    pyxel.text(2,  72, 'Zicht eigen eenheid - zichtbaarheid vijand - vakjes verschil >0 ', 7)
                    pyxel.text(2,  82, '8 - 4 - 1 = 3                                                   ', 7)
                    pyxel.text(2,  92, 'Zicht eigen eenheid                                             ', 7)
                    pyxel.text(2, 102, 'Je zicht is standaard 8 maar kan veranderen met terrein         ', 7)
                    pyxel.text(2, 112, 'Het zicht is ook afhankelijk van welke eenheid je gebruikt      ', 7)
                    pyxel.text(2, 122, 'Zichtbaarheid vijand                                            ', 7)
                    pyxel.text(2, 132, 'De zichtbaarheid van je vijand is standaard 4                   ', 7)
                    pyxel.text(2, 142, 'maar kan veranderen met terrein (bos, berg, …)                  ', 7)
                    pyxel.text(2, 152, 'Aantal vakjes verschil                                          ', 7)
                    pyxel.text(2, 162, 'Het aantal vakjes dat aanwezig is tussen                        ', 7)
                    pyxel.text(2, 172, 'jouw eenheid en die van de vijand                               ', 7)
                    pyxel.text(2, 182, 'Het vakje waarop je tegenstander staat telt ook mee als 1       ', 7)
                    pyxel.text(2, 192, 'DUS 2 vakjes tussen jou en je vijand wordt geteld als 3 vakjes  ', 7)
                    pyxel.text(2, 202, '                                                                ', 7)
                    pyxel.text(2, 212, '                                                                ', 7)
                    pyxel.rect(0,  18, self.breedte, 1, 7)
                    pyxel.rect(0,  28, self.breedte / 1.35, 1, 7)
                    pyxel.rect(0,  98, self.breedte / 2.8, 1, 7)
                    pyxel.rect(0, 128, self.breedte / 2.8, 1, 7)
                    pyxel.rect(0, 158, self.breedte / 2.8, 1, 7)
                if self.menu_pagina == ZICHT_TERREIN:
                    pyxel.text(2,  12, 'Zicht                                                           ', 7)
                    pyxel.text(2,  22, 'Terrein                                                         ', 7)
                    pyxel.text(2,  32, 'Je kan zien wanneer je het zicht van je eenheid                 ', 7)
                    pyxel.text(2,  42, 'min de zichtbaarheid van het terrein                            ', 7)
                    pyxel.text(2,  52, 'min het aantal vakjes verschil doet en dit groter is dan 0      ', 7)
                    pyxel.text(2,  62, 'Bijvoorbeeld                                                    ', 7),
                    pyxel.text(2,  72, 'Zicht eigen eenheid - zichtbaarheid terrein - vakjes verschil >0', 7)
                    pyxel.text(2,  82, '8 - 4 - 1 = 3                                                   ', 7)
                    pyxel.text(2,  92, 'Zicht eigen eenheid                                             ', 7)
                    pyxel.text(2, 102, 'Je zicht is standaard 8 maar kan veranderen met terrein         ', 7)
                    pyxel.text(2, 112, 'Het zicht is ook afhankelijk van welke eenheid je gebruikt      ', 7)
                    pyxel.text(2, 122, 'Zichtbaarheid terrein                                           ', 7)
                    pyxel.text(2, 132, 'De zichtbaarheid is terug te vinden bij de terrein info         ', 7)
                    pyxel.text(2, 142, 'Een berg kan je van verder zien                                 ', 7)
                    pyxel.text(2, 152, 'Aantal vakjes verschil                                          ', 7)
                    pyxel.text(2, 162, 'Het aantal vakjes dat aanwezig is tussen                        ', 7)
                    pyxel.text(2, 172, 'jouw eenheid en het terrein                                     ', 7)
                    pyxel.text(2, 182, '                                                                ', 7)
                    pyxel.text(2, 192, '                                                                ', 7)
                    pyxel.text(2, 202, '                                                                ', 7)
                    pyxel.text(2, 212, '                                                                ', 7)
                    pyxel.rect(0,  18, self.breedte, 1, 7)
                    pyxel.rect(0,  28, self.breedte / 1.35, 1, 7)
                    pyxel.rect(0,  98, self.breedte / 2.8, 1, 7)
                    pyxel.rect(0, 128, self.breedte / 2.8, 1, 7)
                    pyxel.rect(0, 158, self.breedte / 2.8, 1, 7)
                if self.menu_pagina == KNOPPEN:
                    begin_y = 180
                    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                        pyxel.rect(65, 65, 60, 79, 9)
                    if pyxel.btn(pyxel.MOUSE_BUTTON_MIDDLE):
                        pyxel.rect(125, 81, 6, 54, 9)
                    if pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT):
                        pyxel.rect(131, 65, 60, 79, 9)
                    if pyxel.btn(pyxel.KEY_TAB):
                        pyxel.rect(51, begin_y, 14, 7, 9)
                        pyxel.text(86, begin_y - 30, 'volgende eenheid', 7)
                    # if pyxel.btn(pyxel.KEY_A):
                    #     pyxel.rect(66, 196, 7, 7, 9)
                    #     pyxel.text(86, 166, 'kleiner terrein', 7)
                    # if pyxel.btn(pyxel.KEY_Z):
                    #     pyxel.rect(74, 196, 7, 7, 9)
                    #     pyxel.text(86, 166, 'groter terrein', 7)
                    if pyxel.btn(pyxel.KEY_Q):
                        pyxel.rect(69, begin_y + 8, 7, 7, 9)
                        pyxel.text(86, begin_y - 30, 'minder punten', 7)
                    if pyxel.btn(pyxel.KEY_S):
                        pyxel.rect(77, begin_y + 8, 7, 7, 9)
                        pyxel.text(86, begin_y - 30, 'meer punten', 7)
                    if pyxel.btn(pyxel.KEY_R):
                        pyxel.rect(90, begin_y, 7, 7, 9)
                        pyxel.text(86, begin_y - 30, 'random terrein', 7)
                    if pyxel.btn(pyxel.KEY_C):
                        pyxel.rect(88, begin_y + 16, 7, 7, 9)
                        pyxel.text(86, begin_y - 30, 'volgende kleur', 7)
                    if pyxel.btn(pyxel.KEY_B):
                        pyxel.rect(104, begin_y + 16, 7, 7, 9)
                        pyxel.text(86, begin_y - 30, 'veranderen tussen boten en eenheden', 7)
                    if pyxel.btn(pyxel.KEY_I):
                        pyxel.rect(122, begin_y, 7, 7, 9)
                        pyxel.text(86, begin_y - 30, 'terrein info', 7)
                    if pyxel.btn(pyxel.KEY_SPACE):
                        pyxel.rect(88, begin_y + 24, 40, 7, 9)
                        pyxel.text(86, begin_y - 30, 'geselecteerde eenheid beurt overslaan', 7)
                    if pyxel.btn(pyxel.KEY_P):
                        pyxel.rect(138, begin_y, 7, 7, 9)
                        pyxel.text(86, begin_y - 30, 'begingen spelen', 7)
                    if pyxel.btn(pyxel.KEY_M):
                        pyxel.rect(141, begin_y + 8, 7, 7, 9)
                        pyxel.text(86, begin_y - 30, 'menu', 7)
                    if pyxel.btn(pyxel.KEY_LEFT):
                        pyxel.rect(153, begin_y + 16, 7, 7, 9)
                        pyxel.text(86, begin_y - 30, 'vorig type', 7)
                    if pyxel.btn(pyxel.KEY_UP):
                        pyxel.rect(161, begin_y + 8, 7, 7, 9)
                        pyxel.text(86, begin_y - 30, 'hoger nivo', 7)
                    if pyxel.btn(pyxel.KEY_DOWN):
                        pyxel.rect(161, begin_y + 16, 7, 7, 9)
                        pyxel.text(86, begin_y - 30, 'lager nivo', 7)
                    if pyxel.btn(pyxel.KEY_RIGHT):
                        pyxel.rect(169, begin_y + 16, 7, 7, 9)
                        pyxel.text(86, begin_y - 30, 'volgend type', 7)
                    if pyxel.btn(pyxel.KEY_KP_ENTER):
                        pyxel.rect(184, begin_y + 8, 7, 15, 9)
                        pyxel.text(86, begin_y - 30, 'begin / einde beurt', 7)
                    pyxel.blt(64, 64, 2, 0, 24, 128, 80, pyxel.COLOR_GRAY)
                    pyxel.blt(48, begin_y - 2, 2, 0, 104, 144, 40, pyxel.COLOR_BLACK)
                if self.menu_pagina == TERREININSTELLINGEN:
                    pyxel.text(2,  12, 'terreininstellingen                                             ', 7)
                    pyxel.text(2,  22, '                    kans                    grootte             ', 7)
                    pyxel.text(2,  32, 'weg                                                             ', 7),pyxel.text(89, 33, str(self.weg_kans), 7),pyxel.text(189, 33, str(self.weg_grote), 7)
                    pyxel.text(2,  42, 'rivier                                                          ', 7),pyxel.text(89, 43, str(self.rivier_kans), 7),pyxel.text(189, 43, str(self.rivier_grote), 7)
                    pyxel.text(2,  52, 'bos                                                             ', 7),pyxel.text(89, 53, str(self.bos_kans), 7),pyxel.text(189, 53, str(self.bos_grote), 7)
                    pyxel.text(2,  62, 'berg                                                            ', 7),pyxel.text(89, 63, str(self.berg_kans), 7),pyxel.text(189, 63, str(self.berg_grote), 7)
                    pyxel.text(2,  72, 'meer                                                            ', 7),pyxel.text(89, 73, str(self.meer_kans), 7),pyxel.text(189, 73, str(self.meer_grote), 7)
                    pyxel.text(2,  82, 'zee                                                             ', 7),pyxel.text(89, 83, str(self.zee_kans), 7),pyxel.text(189, 83, str(self.zee_grote), 7)
                    pyxel.text(2,  92, 'gebouw                                                          ', 7),pyxel.text(89, 93, str(self.gebouw_aantal), 7),pyxel.text(189, 93, str(self.gebouw_grote), 7)
                    pyxel.text(2, 102, '                                                                ', 7)
                    pyxel.text(2, 112, '                                                                ', 7)
                    pyxel.text(2, 122, '                                                                ', 7)
                    pyxel.text(2, 132, '                                                                ', 7)
                    pyxel.text(2, 142, '                                                                ', 7)
                    pyxel.text(2, 152, '                                                                ', 7)
                    pyxel.text(2, 162, '                                                                ', 7)
                    pyxel.text(2, 172, '                                                                ', 7)
                    pyxel.text(2, 182, '                                                                ', 7)
                    pyxel.text(2, 192, '                                                                ', 7)
                    pyxel.text(2, 202, '                                                                ', 7)
                    pyxel.text(2, 212, '                                                                ', 7)
                    pyxel.text(2, 172, '                                                                ', 7)
                    pyxel.text(2, 182, '                                                                ', 7)
                    pyxel.text(2, 192, '                                                                ', 7)
                    pyxel.text(2, 202, '                                                                ', 7)
                    pyxel.text(2, 212, '                                                                ', 7)
                    pyxel.rect(0, 18, self.breedte, 1, 7)
                    pyxel.blt( 78, 32, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt( 94, 32, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt(178, 32, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt(194, 32, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)

                    pyxel.blt( 78, 42, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt( 94, 42, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt(178, 42, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt(194, 42, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)

                    pyxel.blt( 78, 52, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt( 94, 52, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt(178, 52, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt(194, 52, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)

                    pyxel.blt( 78, 62, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt( 94, 62, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt(178, 62, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt(194, 62, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)

                    pyxel.blt( 78, 72, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt( 94, 72, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt(178, 72, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt(194, 72, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)

                    pyxel.blt( 78, 82, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt( 94, 82, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt(178, 82, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt(194, 82, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)

                    pyxel.blt( 78, 92, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt( 94, 92, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt(178, 92, 2, 64, 16, 8, 8, pyxel.COLOR_BLACK)
                    pyxel.blt(194, 92, 2, 72, 16, 8, 8, pyxel.COLOR_BLACK)


# terijn
            for y, rij in enumerate(self.lijst_met_terijnblokken):
                for x, tegel in enumerate(rij):
                    self.lijst_met_terijnblokken[y][x].update(self)

            if not self.volgende_beurt and not self.toon_menu:
                if not self.is_gedaan:
                    vlakterijn = getTerrein()

                    for y, rij in enumerate(vlakterijn):
                        for x, tegel in enumerate(rij):
                            if self.eenheden_aan_het_plaatsen:
                                newblok = Blok(x * 16 + 8, y * 16 + 8, self.lijst_met_terijnkleuren[tegel])
                                if y >= len(self.lijst_met_terijnblokken):
                                    self.lijst_met_terijnblokken.append([])
                                if x >= len(self.lijst_met_terijnblokken[y]):
                                    self.lijst_met_terijnblokken[y].append(None)
                                if self.lijst_met_terijnblokken[y][x] != newblok:
                                    self.lijst_met_terijnblokken[y][x] = newblok
                                pyxel.blt((self.begin_teken_x + x) * 16, (self.begin_teken_y + y) * 16, 2, tegel * 16, 144, 16, 16,pyxel.COLOR_BLACK)
                            else:
                                for bezige_eenheid in self.eenheiden[self.geselecterde_kleur]:
                                    x_verchil = abs(x * 16 - bezige_eenheid.x)
                                    y_verchil = abs(y * 16 - bezige_eenheid.y)
                                    verchil = x_verchil + y_verchil
                                    if (bezige_eenheid.zicht - verchil / 16) + 4 >= self.ondergrond_zicht[vlakterijn[y][x]]:
                                        self.lijst_met_terijnblokken[y][x].ben_ik_zichtbaar = True

# bouwen

                    for y, rij in enumerate(self.bouwsels):
                        for x, bouwsel in enumerate(rij):
                            if bouwsel != 0 and bouwsel != 4 and bouwsel != 5 and bouwsel != 9:
                                if self.lijst_met_terijnblokken[y][x].ben_ik_voledig_zichtbaar:
                                    pyxel.blt(x * 16 + self.begin_teken_x * 16,
                                              y * 16 + self.begin_teken_y * 16, 2,
                                              (bouwsel % 4 - 1) * 16, 184 + bouwsel // 4 * 16, 16, 16)
                    if self.aan_het_bouwen:
                        pyxel.blt(88, 88, 2, 128, 24, 80, 80, pyxel.COLOR_RED)
                        x = 93
                        y = 120
                        for bouwsel in bouwmogelijkheden[
                            self.terrein[self.y_geselecteerde_eenheid][self.x_geselecteerde_eenheid]]:
                            pyxel.text(x, y, str(bouwsel), 9)
                            if x < 100:
                                x = 130
                            else:
                                x = 93
                                y = 130


# kaart
                    if self.toon_kaart:
                        if not self.is_gedaan:
                            for kleur in self.eenheiden:
                                for eenheid in kleur:
                                    eenheid.draw(self, False)
                        for y, rij in enumerate(vlakterijn):
                            for x in range(1, len(rij) + 1):
                                pyxel.rect(x, y + 1, 1, 1, 0)
                            for x, tegel in enumerate(rij):
                                if self.eenheden_aan_het_plaatsen:
                                    pyxel.rect(x, y, 1, 1, self.lijst_met_terijnkleuren[tegel])
                                else:
                                    for bezige_eenheid in self.eenheiden[self.geselecterde_kleur]:
                                        x_verchil = abs(x * 16 - bezige_eenheid.x)
                                        y_verchil = abs(y * 16 - bezige_eenheid.y)
                                        verchil = x_verchil + y_verchil
                                        if (bezige_eenheid.zicht - verchil / 16) + 4 >= self.ondergrond_zicht[vlakterijn[y][x]]:
                                            pyxel.rect(x, y, 1, 1, self.lijst_met_terijnkleuren[tegel])
                                            # pyxel.blt((self.begin_teken_x + x) * 16, (self.begin_teken_y + y) * 16, 2, tegel * 16, 144, 16, 16, pyxel.COLOR_BLACK)

                        for x in range(0, 16):
                            pyxel.rect(self.begin_teken_x * -1 + x, (self.begin_teken_y * -1) - 1, 1, 1, 9)
                        for x in range(0, 16):
                            pyxel.rect(self.begin_teken_x * -1 + x, (self.begin_teken_y * -1) + 16, 1, 1, 9)
                        for y in range(0, 16):
                            pyxel.rect(self.begin_teken_x * -1 - 1, (self.begin_teken_y * -1) + y, 1, 1, 9)
                        for y in range(0, 16):
                            pyxel.rect(self.begin_teken_x * -1 + 16, (self.begin_teken_y * -1) + y, 1, 1, 9)
                        for i, kleur in enumerate(self.eenheiden):
                            for eenheid in kleur:
                                if eenheid.is_zichtbaar:
                                    pyxel.rect(eenheid.x / 16, eenheid.y / 16, 1, 1, self.lijst_met_eenheidkleuren[eenheid.kleur])
                                if eenheid.is_geselecteerd:
                                    pyxel.rect(eenheid.x / 16, eenheid.y / 16, 1, 1, 9)




                    # for kleur in self.eenheiden:
                    #     for eenheid in kleur:
                    #         if eenheid.kleur != self.geselecterde_kleur and self.geselecteerde_eenheid:
                    #             if eenheid.x == self.aangepaste_x and eenheid.y == self.aangepaste_y and self.geselecteerde_eenheid.berijk >= self.geselecteerde_eenheid.vershil / 16:
                    #                 pyxel.blt(self.x, self.y, 0, 16, 160, 16, 16, pyxel.COLOR_BLACK)
                    if self.geselecteerde_eenheid:
                        if self.geselecteerde_eenheid.bereik >= self.geselecteerde_eenheid.verschil / 16:
                            pyxel.blt(self.x, self.y, 0, 16, 160, 16, 16, pyxel.COLOR_BLACK)


#dode
                if self.is_gedaan:
                    dode_x = -16
                    dode_y = 0
                    for kleur in self.dode_eenheiden:
                        dode_x += 48
                        dode_y = 0

                        for eenheid in kleur:
                            eenheid.x = dode_x
                            eenheid.y = dode_y
                            pyxel.text(dode_x + 16 + self.begin_teken_x * 16, dode_y + self.begin_teken_y * 16, str(int(eenheid.schade_gekregen)), self.lijst_met_eenheidkleuren[eenheid.kleur])
                            pyxel.text(dode_x + 16 + self.begin_teken_x * 16, dode_y + 8 + self.begin_teken_y * 16, str(int(eenheid.schade_gedaan)), self.lijst_met_eenheidkleuren[eenheid.kleur])
                            pyxel.text(dode_x + 32 + self.begin_teken_x * 16, dode_y + self.begin_teken_y * 16, str(int(eenheid.eenheden_gedood)), self.lijst_met_eenheidkleuren[eenheid.kleur])
                            pyxel.text(dode_x + 32 + self.begin_teken_x * 16, dode_y + 8+ self.begin_teken_y * 16, str(int(eenheid.ervaring)), self.lijst_met_eenheidkleuren[eenheid.kleur])
                            eenheid.draw(self, False)
                            dode_y += 16
                            if dode_y == self.game_hoogte:
                                dode_y = 0
                                dode_x += 48
                    for kleur in self.eenheiden:
                        for eenheid in kleur:
                            eenheid.x = dode_x
                            eenheid.y = dode_y
                            pyxel.text(dode_x + 16 + self.begin_teken_x * 16, dode_y + self.begin_teken_y * 16, str(int(eenheid.schade_gekregen)), self.lijst_met_eenheidkleuren[eenheid.kleur])
                            pyxel.text(dode_x + 16 + self.begin_teken_x * 16, dode_y + 8 + self.begin_teken_y * 16, str(int(eenheid.schade_gedaan)), self.lijst_met_eenheidkleuren[eenheid.kleur])
                            pyxel.text(dode_x + 32 + self.begin_teken_x * 16, dode_y + self.begin_teken_y * 16, str(int(eenheid.eenheden_gedood)), self.lijst_met_eenheidkleuren[eenheid.kleur])
                            pyxel.text(dode_x + 32 + self.begin_teken_x * 16, dode_y + 8+ self.begin_teken_y * 16, str(int(eenheid.ervaring)), self.lijst_met_eenheidkleuren[eenheid.kleur])
                            eenheid.draw(self, False)
                            dode_y += 16
                            if dode_y == self.game_hoogte:
                                dode_y = 0
                                dode_x += 48



#eenheiden aan het plaatsen
                if self.eenheden_aan_het_plaatsen:
                    if self.voorbeeldeenheid.gezondheid > 0:
                        beginx = 74
                        pyxel.rect(self.breedte - 81, self.hoogte - beginx, beginx + 6, 57, 7)
                        pyxel.rect(self.breedte - 80, self.hoogte - beginx + 1, beginx + 4, 55, 0)
                        pyxel.text(self.breedte - 11 - 4 * len("gezondheid:"), self.hoogte - beginx + 2, "gezondheid:" + str(self.voorbeeldeenheid.gezondheid), 7)
                        pyxel.text(self.breedte - 11 - 4 * len("moraal:"), self.hoogte - beginx + 8, "moraal:" + str(self.voorbeeldeenheid.moraal), 7)
                        pyxel.text(self.breedte - 11 - 4 * len("bewegen:"), self.hoogte - beginx + 14, "bewegen:" + str(self.voorbeeldeenheid.bewegen), 7)
                        pyxel.text(self.breedte - 11 - 4 * len("bereik:"), self.hoogte - beginx + 20, "bereik:" + str(self.voorbeeldeenheid.bereik), 7)
                        pyxel.text(self.breedte - 11 - 4 * len("verdedigen:"), self.hoogte - beginx + 26, "verdedigen:" + str(self.voorbeeldeenheid.verdedigen), 7)
                        pyxel.text(self.breedte - 11 - 4 * len("aanval:"), self.hoogte - beginx + 32, "aanval:" + str(self.voorbeeldeenheid.aanvallen), 7)
                        pyxel.text(self.breedte - 11 - 4 * len("aanvallen moraal:"), self.hoogte - beginx + 38, "aanvallen moraal:" + str(self.voorbeeldeenheid.aanvallen_moraal), 7)
                        pyxel.text(self.breedte - 11 - 4 * len("vermoeidheid:"), self.hoogte - beginx + 44, "vermoeidheid:" + str(self.voorbeeldeenheid.uithouding), 7)
                        pyxel.text(self.breedte - 11 - 4 * len("munitie:"), self.hoogte - beginx + 50, "munitie:" + str(self.voorbeeldeenheid.munitie), 7)



                    pyxel.text(self.breedte - 14, 33, f"P{self.eenheiden_punten[self.kleur]}", self.lijst_met_eenheidkleuren[self.kleur])
                    pyxel.text(self.breedte - 29, 7, f"T{self.max_aantal_eenheiden_geplaatst_punten[self.T][self.geselecterde_kleur][self.type] - self.aantal_eenheiden_geplaatst_punten[self.geselecterde_kleur][self.type]}", self.lijst_met_eenheidkleuren[self.geselecterde_kleur])
                    pyxel.text(self.breedte - 29, 1, f"N{self.max_aantal_eenheden_nivo[self.nivo] - self.aantal_eenheden_geplaatst_nivo[self.geselecterde_kleur][self.nivo]}", self.lijst_met_eenheidkleuren[self.geselecterde_kleur])
                    if self.max_aantal_eenheiden_geplaatst_punten[self.T][self.kleur][self.type] <= self.aantal_eenheiden_geplaatst_punten[self.kleur][self.type] or self.max_aantal_eenheden_nivo[self.nivo] <= self.aantal_eenheden_geplaatst_nivo[self.kleur][self.nivo]:
                        pyxel.blt(self.x, self.y, 0, 64, self.kleur * 16 + 80, 16, 16, pyxel.COLOR_BLACK)
                    else:
                        self.voorbeeldeenheid.draw(self, True)
                        if self.team_2 < 0 and self.team_1 < 0 or self.geselecterde_kleur == self.team_1:
                            kant = self.x_pos_start * 16
                        else:
                            kant = self.game_breedte - (self.x_pos_start + self.grootte + 1) * 16
                        if kant <= self.aangepaste_x < kant + (self.grootte + 1) * 16 and self.y_pos_start * 16 <= self.aangepaste_y <= self.y_pos_start * 16 + (self.hoogte - (self.grootte * 16)):
                            self.voorbeeldeenheid.x = self.x
                            self.voorbeeldeenheid.y = self.y
                            self.voorbeeldeenheid.draw(self, True)
                        else:
                            pyxel.blt(self.x, self.y, 0, 64, self.kleur * 16 + 80, 16, 16, pyxel.COLOR_BLACK)

                        # pyxel.blt(self.breedte - eenheden_sterren[self.voorbeeldeenheid.T][self.voorbeeldeenheid.kleur][self.voorbeeldeenheid.welk_type][self.voorbeeldeenheid.nivo], 17, 2, 16, 8, -eenheden_sterren[self.voorbeeldeenheid.T][self.voorbeeldeenheid.kleur][self.voorbeeldeenheid.welk_type][self.voorbeeldeenheid.nivo], 8, pyxel.COLOR_BLACK)

                if not self.eenheden_aan_het_plaatsen:
                    pyxel.rect(self.breedte - 5, 0, 4, 4, self.lijst_met_eenheidkleuren[self.geselecterde_kleur])

                if self.geselecteerde_eenheid:
                    self.highlight(self.geselecteerde_eenheid.x + self.begin_teken_x * 16, self.geselecteerde_eenheid.y + self.begin_teken_y * 16)
                    self.kortste_weg = kan_ik_tot_hier(self.x // 16 - self.begin_teken_x, self.y // 16 - self.begin_teken_y, self, self.geselecteerde_eenheid)
                    if self.kortste_weg != False:
                        self.highlight(self.x, self.y)
                for munitie in self.munieties:
                    munitie.draw(self)
                # print(self.schietanimatie)
                # if self.schietanimatie < self.duur_schietanimatie:
                #     pyxel.blt(self.schietanimatie_x + self.begin_teken_x * 16, self.schietanimatie_y + self.begin_teken_y * 16, 2, 0, 0, 16, 16, pyxel.COLOR_BLACK)
                #     if self.schietrichting_x > 0:
                #         if self.schietanimatie_x < self.einde_schietanimatie_x:
                #             self.schietanimatie_x += 1 * self.schietrichting_x
                #     else:
                #         if self.schietanimatie_x > self.einde_schietanimatie_x:
                #             self.schietanimatie_x += 1 * self.schietrichting_x
                #     if self.schietrichting_y > 0:
                #         if self.schietanimatie_y < self.einde_schietanimatie_y:
                #             self.schietanimatie_y += 1 * self.schietrichting_y
                #     else:
                #         if self.schietanimatie_y > self.einde_schietanimatie_y:
                #             self.schietanimatie_y += 1 * self.schietrichting_y
                #     self.schietanimatie += 1

                pyxel.rect(0, self.hoogte - 6, 25, 6, 0)
                pyxel.rect(0, self.hoogte - 5, 24, 4, self.lijst_met_eenheidkleuren[self.team_1])
                pyxel.rect(12 - self.balansen[self.team_2] * 3, self.hoogte - 5, 12 + self.balansen[self.team_2] * 3, 4, self.lijst_met_eenheidkleuren[self.team_2])
                pyxel.rect(11, self.hoogte - 5, 2, 1, 0)
                pyxel.rect(11, self.hoogte - 2, 2, 1, 0)

#eenheid info
                if self.geselecteerde_eenheid != None:
                    beginx = 80
                    pyxel.rect(self.breedte - 81, self.hoogte - beginx, 80, 63, 7)
                    pyxel.rect(self.breedte - 80, self.hoogte - beginx + 1, 78, 61, 0)
                    pyxel.text(self.breedte - 11 - 4 * len("gezondheid:"), self.hoogte - beginx + 2, "gezondheid:" + str(int(self.geselecteerde_eenheid.gezondheid)), 7)
                    pyxel.text(self.breedte - 11 - 4 * len("moraal:"), self.hoogte - beginx + 8, "moraal:" + str(int(self.geselecteerde_eenheid.moraal)), 7)
                    pyxel.text(self.breedte - 11 - 4 * len("bewegen:"), self.hoogte - beginx + 14, "bewegen:" + str(int(self.geselecteerde_eenheid.bewegen)), 7)
                    pyxel.text(self.breedte - 11 - 4 * len("bereik:"), self.hoogte - beginx + 20, "bereik:" + str(int(self.geselecteerde_eenheid.bereik)), 7)
                    pyxel.text(self.breedte - 11 - 4 * len("verdedigen:"), self.hoogte - beginx + 26, "verdedigen:" + str(int(self.geselecteerde_eenheid.verdedigen)), 7)
                    pyxel.text(self.breedte - 11 - 4 * len("aanval:"), self.hoogte - beginx + 32, "aanval:" + str(int(self.geselecteerde_eenheid.aanvallen)), 7)
                    pyxel.text(self.breedte - 11 - 4 * len("aanvallen moraal:"), self.hoogte - beginx + 38, "aanvallen moraal:" + str(int(self.geselecteerde_eenheid.aanvallen_moraal)), 7)
                    pyxel.text(self.breedte - 11 - 4 * len("vermoeidheid:"), self.hoogte - beginx + 44, "vermoeidheid:" + str(int(self.geselecteerde_eenheid.uithouding)), 7)
                    pyxel.text(self.breedte - 11 - 4 * len("ervaring:"), self.hoogte - beginx + 50, "ervaring:" + str(int(self.geselecteerde_eenheid.ervaring_nivo)), 7)
                    pyxel.text(self.breedte - 11 - 4 * len("munitie:"), self.hoogte - beginx + 56, "munitie:" + str(self.geselecteerde_eenheid.munitie), 7)
                    pyxel.rect(self.breedte - 65, self.hoogte - 18, 50, 1, pyxel.COLOR_BLACK)
                    pyxel.rect(self.breedte - 65, self.hoogte - 18, self.geselecteerde_eenheid.ervaring - self.geselecteerde_eenheid.ervaring_nivo * 50, 1, self.lijst_met_eenheidkleuren[self.geselecteerde_eenheid.kleur])

                    tegestander_info_namen = ["gezondheid:", "moraal:", "bereik:", "verdedigen:", "aanval:", "aanvallen moraal:"]

                    for kleur in self.eenheiden:
                        for eenheid in kleur:
                            if eenheid.x == self.aangepaste_x and eenheid.y == self.aangepaste_y and eenheid.kleur != self.geselecterde_kleur and eenheid.is_zichtbaar:
                                beginx = len(tegestander_info_namen) * 6 + 10
                                tegestander_info = [str(int(eenheid.gezondheid)), str(int(eenheid.moraal)), str(int(eenheid.bereik)), str(int(eenheid.verdedigen)), str(int(eenheid.aanvallen)), str(int(eenheid.aanvallen_moraal))]
                                pyxel.rect(0, self.hoogte - beginx, 75, beginx - 6, 7)
                                pyxel.rect(1, self.hoogte - beginx + 1, 73, beginx - 8, 0)
                                extra_x = 2
                                for i, eigenschap in enumerate(tegestander_info):
                                    pyxel.text(66 - 4 * len(tegestander_info_namen[i]), self.hoogte - beginx + extra_x, tegestander_info_namen[i] + eigenschap, 7)
                                    extra_x += 6
                                pyxel.rect(13, self.hoogte - beginx + extra_x + 1, 50, 1, pyxel.COLOR_BLACK)
                                pyxel.rect(13, self.hoogte - beginx + extra_x + 1, eenheid.ervaring - eenheid.ervaring_nivo * 50, 1, self.lijst_met_eenheidkleuren[eenheid.kleur])

#terijn info
                if self.toon_info:
                    x = self.aangepaste_x // 16
                    y = self.aangepaste_y // 16
                    if 0 <= x < self.game_breedte // 16 and 0 <= y < self.game_hoogte // 16:
                        vlakterijn = getTerrein()
                        i = vlakterijn[y][x]
                        extra_y = len(terijn_eigenschapen[i]) * 6 + 25
                        pyxel.rect(self.breedte // 2 - 34, self.hoogte - extra_y - 2, 68, extra_y + 2, 7)
                        pyxel.rect(self.breedte // 2 - 33, self.hoogte - extra_y - 1, 66, extra_y, 0)
                        pyxel.text(145 - 4 * len(terijn_namen[i]), self.hoogte - extra_y, terijn_namen[i], 7)
                        extra_y -= 6
                        pyxel.text(149 - 4 * len("bewegen:"), self.hoogte - extra_y, "bewegen:" + str(route.ondergrond_impact[i]),7)
                        extra_y -= 6
                        pyxel.text(149 - 4 * len("zicht:"), self.hoogte - extra_y, "zicht:" + str(self.ondergrond_zicht[i]), 7)
                        extra_y -= 6
                        pyxel.text(149 - 4 * len("vermoeidheid:"), self.hoogte - extra_y, "vermoeidheid:" + str(uithouding_terijn[i]), 7)
                        for eigenschap in (terijn_eigenschapen[i]):
                            extra_y -= 6
                            pyxel.text(149 - 4 * (len(eigenschap) - 1), self.hoogte - extra_y, eigenschap, 7)

            pyxel.blt(self.breedte - 16, self.hoogte - 16, 0, 48, 160, 16, 16, pyxel.COLOR_BLACK)
        # if pyxel.btn(pyxel.KEY_N):
        #     pyxel.blt(0, 0, 1, 0, 0, 256, 256)



    def eenheid_plaatsen_of_verplaatsen(self):
        vlakterijn = getTerrein()
        self.kan_ik_verplaatsen = True
        # for i, kleur in enumerate(self.eenheiden):
        #     for eenheid in kleur:
        #         if eenheid.x == self.aangepaste_x and eenheid.y == self.aangepaste_y:
        #             self.kan_ik_verplaatsen = False
        # if self.eenheiden_aan_het_plaatsen and self.max_aantal_eenheiden[self.type] > self.aantal_eenheiden_geplaatst[self.type] and self.eenheiden_punten[self.kleur] > self.nivo and self.max_aantal_eenheiden_nivo[self.nivo] > self.aantal_eenheiden_geplaatst_nivo[self.kleur][self.nivo]:
        if self.eenheden_aan_het_plaatsen:
            if self.max_aantal_eenheiden_geplaatst_punten[self.T][self.kleur][self.type] > self.aantal_eenheiden_geplaatst_punten[self.kleur][self.type] + self.nivo or self.boot:
                if self.max_aantal_eenheden_nivo[self.nivo] > self.aantal_eenheden_geplaatst_nivo[self.kleur][self.nivo] and self.eenheiden_punten[self.geselecterde_kleur] - self.nivo >= 0:
                    if self.breedte - 16 != self.x or self.hoogte - 16 != self.y:
                        # print(f"{self.max_aantal_eenheiden_geplaatst_punten[self.kleur][self.type]} : {self.aantal_eenheiden_geplaatst_punten[self.kleur][self.type]}")
                        self.nieuw_eenheid(self.kleur, self.type, self.nivo, self.aangepaste_x, self.aangepaste_y, self.T, self.boot)
                        self.eenheiden_punten[self.kleur] -= self.nivo + 1
                        self.aantal_eenheiden_geplaatst[self.type] += 1
                        self.aantal_eenheden_geplaatst_nivo[self.kleur][self.nivo] += 1
                        self.aantal_eenheiden_geplaatst_punten[self.kleur][self.type] += self.nivo + 1
                        if self.team_1 < 0:
                            self.team_1 = self.kleur
                        elif self.geselecterde_kleur != self.team_1:
                            self.team_2 = self.kleur
        elif not self.eenheden_aan_het_plaatsen:
            for geselecteerde_eenheid in self.eenheiden[self.geselecterde_kleur]:
                # print(geselecteerde_eenheid.boot)
                if geselecteerde_eenheid.x == self.aangepaste_x and geselecteerde_eenheid.y == self.aangepaste_y and not geselecteerde_eenheid.is_geweest:
                    for eenheid in self.eenheiden[self.geselecterde_kleur]:
                        if eenheid.x != self.aangepaste_x or eenheid.y != self.aangepaste_y:
                            eenheid.is_geselecteerd = False
                    geselecteerde_eenheid.is_geselecteerd = not geselecteerde_eenheid.is_geselecteerd
                    break
                for i, kleur in enumerate(self.eenheiden):
                    for eenheid in kleur:
                        if eenheid.x == self.aangepaste_x and eenheid.y == self.aangepaste_y:
                            self.kan_ik_verplaatsen = False
                if self.geselecteerde_eenheid and self.kan_ik_verplaatsen:
                    if self.kortste_weg != False:
                        if self.geselecteerde_eenheid.boot == 0 and self.geselecteerde_eenheid.welk_type == 0:
                            vlakterijn[self.geselecteerde_eenheid.y // 16][self.geselecteerde_eenheid.x // 16] = 2
                        self.geselecteerde_eenheid.x = self.aangepaste_x
                        self.geselecteerde_eenheid.y = self.aangepaste_y
                        self.geselecteerde_eenheid.is_geselecteerd = False
                        self.geselecteerde_eenheid.uithouding -= self.kortste_weg[4]
                        self.geselecteerde_eenheid.bewegen = self.kortste_weg[3]
                        if self.geselecteerde_eenheid.boot == 0 and self.geselecteerde_eenheid.welk_type == 0:
                            vlakterijn[self.geselecteerde_eenheid.y // 16][self.geselecteerde_eenheid.x // 16] = 4
                        # print(self.geselecteerde_eenheid.bewegen)
                        if self.geselecteerde_eenheid.bewegen <= 0:
                            self.geselecteerde_eenheid.is_geweest = True


            # begin_x_verschil = self.aangepaste_x - geselecteerde_eenheid.x
                # if begin_x_verschil < 0:
                #     x_verschil = 16
                #     begin_x_verschil *= -1
                # elif begin_x_verschil == 0:
                #     x_verschil = 0
                # else:
                #     x_verschil = -16
                # begin_y_verschil = self.aangepaste_y - geselecteerde_eenheid.y
                # if begin_y_verschil < 0:
                #     y_verschil = 16
                #     begin_y_verschil *= -1
                # elif begin_y_verschil == 0:
                #     y_verschil = 0
                # else:
                #     y_verschil = -16
                # positief_x_verschil = x_verschil
                # positief_y_verschil = y_verschil
                # if x_verschil < 0:
                #     positief_x_verschil *= -1
                # if y_verschil < 0:
                #     positief_y_verschil *= -1
                # vershil = positief_x_verschil + positief_y_verschil
                # if geselecteerde_eenheid.is_geselecteerd:
                #     geselecteerde_eenheid.bewegen = geselecteerde_eenheid.stard_bewegen
                #     if vershil <= geselecteerde_eenheid.bewegen * 16:
                #         while geselecteerde_eenheid.bewegen > 0:
                #             geselecteerde_eenheid_bewegen = geselecteerde_eenheid.bewegen
                #             for i, kleur in enumerate(self.eenheiden):
                #                 for eenheid in kleur:
                #                     if eenheid.x == geselecteerde_eenheid.x - x_verschil and eenheid.y == geselecteerde_eenheid.y - y_verschil:
                #                         self.kan_ik_verplaatsen = False
                #                         geselecteerde_eenheid.bewegen = -1
                #             if self.kan_ik_verplaatsen:
                #                 if begin_x_verschil >= 0:
                #                     begin_x_verschil -= 16
                #                 if begin_y_verschil >= 0:
                #                     begin_y_verschil -= 16
                #                 if begin_x_verschil < 0 and begin_y_verschil < 0:
                #                     break
                #                 geselecteerde_eenheid.bewegen -= self.ondergrond_impact[vlakterijn[int(geselecteerde_eenheid.y / 16)][int(geselecteerde_eenheid.x / 16)]]
                #                 if begin_x_verschil >= 0:
                #                     geselecteerde_eenheid.x -= x_verschil
                #                 if begin_y_verschil >= 0:
                #                     geselecteerde_eenheid.y -= y_verschil
                #                 geselecteerde_eenheid_bewegen = geselecteerde_eenheid.bewegen
                #
                #         if geselecteerde_eenheid_bewegen <= 0:
                #             geselecteerde_eenheid.is_geweest = True
                #         geselecteerde_eenheid.is_geselecteerd = False
                #         geselecteerde_eenheid.bewegen = geselecteerde_eenheid_bewegen
                #         geselecteerde_eenheid.stard_bewegen = geselecteerde_eenheid_bewegen
                #     else:
                #         geselecteerde_eenheid.is_geweest = False
                #         geselecteerde_eenheid.is_geselecteerd = False

    def dood_eenhijd(self, eenheid):
        i = eenheid.kleur
        vlakterijn = getTerrein()
        self.dode_eenheiden[i].append(eenheid)
        if eenheid.gezondheid < 0:
            self.aantal_gestorven[0] += 1
        else:
            self.aantal_gestorven[1] += 1
        self.aantal_eenheden_geplaatst_nivo[i][eenheid.nivo] -= 1
        self.eenheiden[i].remove(eenheid)
        self.balans(self.geselecterde_kleur, i, eenheid.nivo)
        self.geselecteerde_eenheid.eenheden_gedood += 1
        self.geselecteerde_eenheid.ervaring += 10
        if eenheid.boot == 0 and eenheid.welk_type == 0:
            vlakterijn[eenheid.y // 16][eenheid.x // 16] = 4
        for bezegeeenheid in self.eenheiden[self.geselecterde_kleur]:
            if bezegeeenheid.is_geselecteerd and bezegeeenheid.bereik < 2:
                bezegeeenheid.x = self.aangepaste_x
                bezegeeenheid.y = self.aangepaste_y

    def Naar_achter(self, geduwde, x, y, positiefx_verschil, positiefy_verschil):
        naar_achter_type_aanval = self.geselecteerde_eenheid.duwen#[4, 2, 5, 0, 0, 1]
        naar_achter_type_verdedigen = self.geselecteerde_eenheid.duwbaarhijd#[3, 5, 4, 1, 0, 1]
        naar_achter_type_ondergrond = [1, 2, 10, 3, 0, 0, 4]
        ondergrond = naar_achter_type_ondergrond[self.terrein[geduwde.y // 16][geduwde.x // 16]]
        self.naar_achter = random.triangular(0, 10)
        if self.naar_achter + naar_achter_type_verdedigen + ondergrond <= -2 + positiefx_verschil * 2  + positiefy_verschil + naar_achter_type_aanval:
            aantal_naast = 0
            # if self.geselecteerde_eenheid.bereik < 2:
            if x < 0:
                x = -16
            elif x == 0:
                x = 0
            else:
                x = 16
            if y < 0:
                y = -16
            elif y == 0:
                y = 0
            else:
                y = 16
            if 0 < geduwde.x < self.game_breedte - 16 and 0 < geduwde.y < self.game_hoogte - 16:
                kan_ik_naar_achter = True
            else:
                kan_ik_naar_achter = False
            for i, kleur in enumerate(self.eenheiden):
                for eenheid in kleur:
                    if eenheid.x - x == geduwde.x and eenheid.y - y == geduwde.y:
                        kan_ik_naar_achter = False
                    x_verschil = abs(geduwde.x - x - eenheid.x)
                    y_verschil = abs(geduwde.y - y - eenheid.y)
                    verschil = x_verschil + y_verschil
                    if verschil <= 16 and eenheid.kleur == geduwde.kleur:
                        aantal_naast += 1
            if aantal_naast > 1:
                kan_ik_naar_achter = False
            if kan_ik_naar_achter:
                for i, kleur in enumerate(self.eenheiden):
                    for eenheid in kleur:
                        if eenheid.x + x == geduwde.x and eenheid.y + y == geduwde.y:
                            eenheid.x += x
                            eenheid.y += y
                            eenheid.uithouding -= 1
                geduwde.x += x
                geduwde.y += y
                self.balans(self.geselecterde_kleur, geduwde.kleur, geduwde.nivo)
            pass

    def val_aan0(self):
        self.kan_ik_verplaatsen = True
        self.kan_ik_aanvallen = False
        self.naar_achter = random.triangular(0, 10)
        for i, kleur in enumerate(self.eenheiden):
            for eenheid in kleur:
                if eenheid.x == self.aangepaste_x and eenheid.y == self.aangepaste_y :
                    self.kan_ik_aanvallen = True

        for i, kleur in enumerate(self.eenheiden):
            for eenheid in kleur:
                if eenheid.kleur != self.geselecteerde_eenheid.kleur:
                    x_verschil_16 = eenheid.x - self.geselecteerde_eenheid.x
                    if x_verschil_16 < 0:
                        x_verschil_16 = -16
                    elif x_verschil_16 == 0:
                        x_verschil_16 = 0
                    else:
                        x_verschil_16 = 16
                    y_verschil_16 = eenheid.y - self.geselecteerde_eenheid.y
                    if y_verschil_16 < 0:
                        y_verschil_16 = -16
                    elif y_verschil_16 == 0:
                        y_verschil_16 = 0
                    else:
                        y_verschil_16 = 16
                    if eenheid.x == self.aangepaste_x + x_verschil_16 and eenheid.y == self.aangepaste_y + y_verschil_16:
                        self.kan_ik_verplaatsen = False
        for i, kleur in enumerate(self.eenheiden):
            for eenheid in kleur:
                if eenheid.kleur != self.geselecterde_kleur:
                    x_verschil = eenheid.x - self.geselecteerde_eenheid.x
                    if x_verschil < 0:
                        positiefx_verschil = (x_verschil * -1) / 16
                    else:
                        positiefx_verschil = x_verschil / 16
                    y_verschil = eenheid.y - self.geselecteerde_eenheid.y
                    if y_verschil < 0:
                        positiefy_verschil = (y_verschil * -1) / 16
                    else:
                        positiefy_verschil = y_verschil / 16


                    if eenheid.x == self.aangepaste_x and eenheid.y == self.aangepaste_y and self.geselecteerde_eenheid.bereik >= self.geselecteerde_eenheid.verschil:
                        if self.naar_achter + eenheid.nivo <= 2 + positiefx_verschil / 2 + positiefy_verschil / 2 + self.geselecteerde_eenheid.nivo:
                            self.Naar_achter(eenheid, x_verschil, y_verschil)
                        eenheid.raak_gewond(self.geselecteerde_eenheid.aanval, self.geselecteerde_eenheid.moraalaanval)
                        if eenheid.gezondheid <= 0 or eenheid.moraal <= 0:
                            self.dood_eenhijd(eenheid)
                        break
                    elif positiefx_verschil <= self.geselecteerde_eenheid.bewegen and positiefy_verschil == 0 and eenheid.x == self.aangepaste_x and eenheid.y == self.aangepaste_y and self.kan_ik_verplaatsen:
                        for bezegeeenheid in self.eenheiden[self.geselecterde_kleur]:
                            if bezegeeenheid.is_geselecteerd:
                                if x_verschil < 0:
                                    bezegeeenheid.x += x_verschil + 16
                                else:
                                    bezegeeenheid.x += x_verschil - 16
                        random_aanval = int(random.triangular(0, positiefx_verschil))
                        if self.naar_achter + eenheid.nivo <= 2 + positiefx_verschil / 2 + positiefy_verschil / 2 + self.geselecteerde_eenheid.nivo:
                            self.Naar_achter(eenheid, x_verschil, y_verschil)
                        eenheid.raak_gewond(self.geselecteerde_eenheid.aanval + positiefx_verschil - random_aanval, self.geselecteerde_eenheid.moraalaanval + positiefx_verschil)
                        if eenheid.gezondheid <= 0 or eenheid.moraal <= 0:
                            self.dood_eenhijd(eenheid)
                        break
                    elif positiefy_verschil <= self.geselecteerde_eenheid.bewegen and positiefx_verschil == 0 and eenheid.x == self.aangepaste_x and eenheid.y == self.aangepaste_y  and self.kan_ik_verplaatsen:
                        for bezegeeenheid in self.eenheiden[self.geselecterde_kleur]:
                            if bezegeeenheid.is_geselecteerd:
                                if y_verschil < 0:
                                    bezegeeenheid.y += y_verschil + 16
                                else:
                                    bezegeeenheid.y += y_verschil - 16
                        random_aanval = int(random.triangular(0, positiefy_verschil))
                        if self.naar_achter + eenheid.nivo <= 2 + positiefx_verschil / 2 + positiefy_verschil / 2 + self.geselecteerde_eenheid.nivo:
                            self.Naar_achter(eenheid, x_verschil, y_verschil)
                        eenheid.raak_gewond(self.geselecteerde_eenheid.aanval + positiefy_verschil - random_aanval, self.geselecteerde_eenheid.moraalaanval + positiefx_verschil)
                        if eenheid.gezondheid <= 0 or eenheid.moraal <= 0:
                            self.dood_eenhijd(eenheid)
                        break
        for bezegeeenheid in self.eenheiden[self.geselecterde_kleur]:
            if bezegeeenheid.is_geselecteerd and self.kan_ik_aanvallen:
                bezegeeenheid.is_geselecteerd = False
                bezegeeenheid.is_geweest = True

    def val_aan(self):
        self.kan_ik_verplaatsen = True
        self.kan_ik_aanvallen = False
        self.naar_achter = random.triangular(0, 10)

        if self.geselecteerde_eenheid:
            for i, kleur in enumerate(self.eenheiden):
                for eenheid in kleur:
                    if eenheid.kleur != self.geselecterde_kleur:
                        x_verschil = eenheid.x - self.geselecteerde_eenheid.x
                        if x_verschil < 0:
                            positiefx_verschil = (x_verschil * -1) // 16
                            self.schietrichting_x = -1
                        else:
                            positiefx_verschil = x_verschil // 16
                            self.schietrichting_x = 1
                        y_verschil = eenheid.y - self.geselecteerde_eenheid.y
                        if y_verschil < 0:
                            self.schietrichting_y = -1
                            positiefy_verschil = (y_verschil * -1) // 16
                        else:
                            self.schietrichting_y = 1
                            positiefy_verschil = y_verschil // 16
                        if self.balansen[self.geselecterde_kleur] > 0:
                            extra_aanvalen_moraal = self.balansen[self.geselecterde_kleur]
                        else:
                            extra_aanvalen_moraal = 0
                        # print(extra_aanvalen_moraal)

                        # print(f"{positiefx_verschil} : {positiefy_verschil} : {self.geselecteerde_eenheid.bewegen}")
                        if eenheid.x == self.aangepaste_x and eenheid.y == self.aangepaste_y and self.geselecteerde_eenheid.bereik >= self.geselecteerde_eenheid.verschil / 16:
                            self.kan_ik_aanvallen = True
                            self.schietanimatie = 0
                            if positiefx_verschil > positiefy_verschil:
                                self.duur_schietanimatie = x_verschil * self.schietrichting_x
                            else:
                                self.duur_schietanimatie = y_verschil * self.schietrichting_y
                            self.schietanimatie_x = self.geselecteerde_eenheid.x
                            self.einde_schietanimatie_x = self.aangepaste_x
                            self.schietanimatie_y = self.geselecteerde_eenheid.y
                            self.einde_schietanimatie_y = self.aangepaste_y
                            if self.geselecteerde_eenheid.bereik > 1:
                                new_munitie = Munitie(self.geselecteerde_eenheid, self.duur_schietanimatie, self.schietanimatie_x, self.schietanimatie_y, self.einde_schietanimatie_x, self.einde_schietanimatie_y, self.schietrichting_x, self.schietrichting_y)
                                self.munieties.append(new_munitie)
                            # if self.geselecteerde_eenheid.welk_type == 4:

                            self.Naar_achter(eenheid, x_verschil, y_verschil, positiefx_verschil, positiefy_verschil)
                            eenheid.raak_gewond(self.geselecteerde_eenheid.aanvallen, self.geselecteerde_eenheid.aanvallen_moraal + extra_aanvalen_moraal)
                            self.geselecteerde_eenheid.ervaring += self.geselecteerde_eenheid.aanvallen + 1
                            self.geselecteerde_eenheid.schade_gedaan += self.geselecteerde_eenheid.aanvallen
                            self.geselecteerde_eenheid.aantal_keer_aangevallen += 1
                            self.geselecteerde_eenheid.uithouding -= 3
                            if abs(x_verschil) + abs(y_verschil) > 16:
                                self.geselecteerde_eenheid.munitie -= 1
                            self.rondom_moraal_verliezen(eenheid, self.geselecteerde_eenheid.aanvallen_moraal)
                            if eenheid.gezondheid <= 0 or eenheid.moraal <= 0:
                                self.dood_eenhijd(eenheid)
                            break

                        elif self.kortste_weg != False and positiefy_verschil == 0 and eenheid.x == self.aangepaste_x and eenheid.y == self.aangepaste_y and self.kan_ik_verplaatsen:
                            self.kan_ik_aanvallen = True
                            for bezegeeenheid in self.eenheiden[self.geselecterde_kleur]:
                                if bezegeeenheid.is_geselecteerd:
                                    if x_verschil < 0:
                                        bezegeeenheid.x += x_verschil + 16
                                    else:
                                        bezegeeenheid.x += x_verschil - 16
                            random_aanval = int(random.triangular(0, positiefx_verschil))
                            self.Naar_achter(eenheid, x_verschil, y_verschil, positiefx_verschil, positiefy_verschil)
                            eenheid.raak_gewond(self.geselecteerde_eenheid.aanvallen + positiefx_verschil - random_aanval, self.geselecteerde_eenheid.aanvallen_moraal + extra_aanvalen_moraal)
                            self.geselecteerde_eenheid.schade_gedaan += self.geselecteerde_eenheid.aanvallen
                            self.geselecteerde_eenheid.ervaring += self.geselecteerde_eenheid.aanvallen + 1
                            self.geselecteerde_eenheid.aantal_keer_aangevallen += 1
                            self.geselecteerde_eenheid.uithouding -= 3 + (abs(x_verschil) // 16)
                            self.rondom_moraal_verliezen(eenheid, self.geselecteerde_eenheid.aanvallen_moraal)
                            if eenheid.gezondheid <= 0 or eenheid.moraal <= 0:
                                self.dood_eenhijd(eenheid)
                            break
                        elif self.kortste_weg != False and positiefx_verschil == 0 and eenheid.x == self.aangepaste_x and eenheid.y == self.aangepaste_y  and self.kan_ik_verplaatsen:
                            self.kan_ik_aanvallen = True
                            for bezegeeenheid in self.eenheiden[self.geselecterde_kleur]:
                                if bezegeeenheid.is_geselecteerd:
                                    if y_verschil < 0:
                                        bezegeeenheid.y += y_verschil + 16
                                    else:
                                        bezegeeenheid.y += y_verschil - 16
                            random_aanval = int(random.triangular(0, positiefy_verschil))
                            self.Naar_achter(eenheid, x_verschil, y_verschil, positiefx_verschil, positiefy_verschil)
                            eenheid.raak_gewond(self.geselecteerde_eenheid.aanvallen + positiefy_verschil - random_aanval, self.geselecteerde_eenheid.aanvallen_moraal + extra_aanvalen_moraal)
                            self.geselecteerde_eenheid.schade_gedaan += self.geselecteerde_eenheid.aanvallen
                            self.geselecteerde_eenheid.ervaring += self.geselecteerde_eenheid.aanvallen + 1
                            self.geselecteerde_eenheid.aantal_keer_aangevallen += 1
                            self.geselecteerde_eenheid.uithouding -= 3 + (abs(y_verschil) // 16)
                            self.rondom_moraal_verliezen(eenheid, self.geselecteerde_eenheid.aanvallen_moraal)
                            if eenheid.gezondheid <= 0 or eenheid.moraal <= 0:
                                self.dood_eenhijd(eenheid)
                            break

            for bezegeeenheid in self.eenheiden[self.geselecterde_kleur]:
                if bezegeeenheid.is_geselecteerd and self.kan_ik_aanvallen:
                    bezegeeenheid.is_geselecteerd = False
                    bezegeeenheid.is_geweest = True

    def rondom_moraal_verliezen(self, eenheid, moraalaanval):
        gewonde_eenheid = eenheid
        for i, kleur in enumerate(self.eenheiden):
            for eenheid in kleur:
                if eenheid.kleur == gewonde_eenheid.kleur and eenheid != gewonde_eenheid:
                    if abs(eenheid.x - gewonde_eenheid.x) == 16 and abs(eenheid.y - gewonde_eenheid.y) == 0 or abs(eenheid.x - gewonde_eenheid.x) == 0 and abs(eenheid.y - gewonde_eenheid.y) == 16:
                        moraalaanval = random.triangular(-10, 85) // 20
                        eenheid.raak_gewond(0, moraalaanval)
                        print(int(moraalaanval))

    def volgendebeurt(self):
        if self.volgende_beurt:
            if len(self.eenheiden[self.geselecterde_kleur]) > 1:
                for eenheid in self.eenheiden[self.geselecterde_kleur]:
                    for generaal in self.eenheiden[self.geselecterde_kleur]:
                        x_verchil = abs(eenheid.x - generaal.x)
                        y_verchil = abs(eenheid.y - generaal.y)
                        verchil = x_verchil + y_verchil
                        if generaal.nivo == 3 and eenheid.moraal + 2 < eenheid.begin_moraal and verchil < 64:
                            eenheid.moraal += 3
            for i, eenheid in enumerate(self.eenheiden[self.geselecterde_kleur]):
                eenheid.is_geweest = False
                eenheid.is_zichtbaar = False
                eenheid.start_bewegen = eenheid.begin_bewegen
                eenheid.bewegen = eenheid.start_bewegen
                prosent = len(self.begin_eenheiden[self.geselecterde_kleur]) / 5
                extra_moraal = (len(self.eenheiden[self.geselecterde_kleur]) / prosent) - 3
                if eenheid.moraal + extra_moraal < eenheid.begin_moraal:
                    eenheid.moraal += extra_moraal
                # if eenheid.uithouding <= 0:
                #     eenheid.uithouding += 1
                if eenheid.uithouding + (uithouding_terugkrijgen_type[eenheid.welk_type] * uithouding_terugkrijgen_nivo[
                    eenheid.nivo]) <= eenheid.begin_uithouding:
                    eenheid.uithouding += eenheid.uithouding_terugkrijgen
                # print(f"{eenheid_namen[eenheid.welk_type]} : {eenheid.nivo + 1} : {uithouding_terugkrijgen_type[eenheid.welk_type] * uithouding_terugkrijgen_nivo[eenheid.nivo]}")
                # if eenheid.moraal < eenheid.begin_moraal and len(self.begin_eenheiden[self.geselecterde_kleur]) / 2 <= len(self.eenheiden[self.geselecterde_kleur]):
                #     eenheid.moraal += 1
                # if len(self.begin_eenheiden[self.geselecterde_kleur]) / 2.5 >= len(self.eenheiden[self.geselecterde_kleur]):
                #     eenheid.moraal -= 1
                # if len(self.begin_eenheiden[self.geselecterde_kleur]) / 3 >= len(self.eenheiden[self.geselecterde_kleur]):
                #     eenheid.moraal -= 2
                if self.aantal_eenheden_geplaatst_nivo[eenheid.kleur][3] == 0:
                    eenheid.moraal -= 1
            self.geselecterde_kleur += 1
            if self.geselecterde_kleur > 4:
                self.geselecterde_kleur = 0
            while len(self.eenheiden[self.geselecterde_kleur]) < 1:
                self.geselecterde_kleur += 1
                if self.geselecterde_kleur > 4:
                    self.geselecterde_kleur = 0
            for eenheid in self.eenheiden[self.geselecterde_kleur]:
                eenheid.is_zichtbaar = True
        self.volgende_beurt = not self.volgende_beurt
        for y, rij in enumerate(self.lijst_met_terijnblokken):
            for x, tegel in enumerate(rij):
                tegel.ben_ik_zichtbaar = False


    def highlight(self, x, y):
        pyxel.blt(x, y, 0, 0, 160, 16, 16, pyxel.COLOR_BLACK)

    def run(self):
        pyxel.run(self.update, self.draw)

