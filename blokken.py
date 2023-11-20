import random

import pyxel
import terrein

class Blok():
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c
        self.w = -1
        self.h = -1
        self.verschil = 1
        self.timer = 0
        self.ben_ik_zichtbaar = False
        self.vorige_ben_ik_zichtbaar = False
        self.ben_ik_voledig_zichtbaar = False
        self.u2 = 0
        self.w2 = 0
        self.x2 = 96
        self.animatiesnelheid = 2




    def update(self, game):
        # if self.ben_ik_zichtbaar != self.vorige_ben_ik_zichtbaar:
        self.c = game.lijst_met_terijnkleuren[game.terrein[(self.y) // 16][(self.x) // 16]]
        if self.ben_ik_zichtbaar:
            self.verschil = 1
            self.vergroot(game)
        else:
            self.verschil = -1
            self.verklijn(game)
        self.vorige_ben_ik_zichtbaar = self.ben_ik_zichtbaar

    def start_animatie(self, game):
        pyxel.rect(self.x, self.y, self.w, self.h, self.c)
        self.w += 2 * self.verschil
        self.h += 2 * self.verschil
        self.x -= self.verschil
        self.y -= self.verschil
        # print(f"w{self.w} :h{self.h} :x{self.x} :y{self.y} :ver{self.verschil} : t{self.timer}")
        self.timer += 1
        if self.w >= 16:
            self.verschil = 0
            if self.timer >= 100:
                self.verschil = -1


        pyxel.blt(self.x2, 96, 1, self.u2, 40, self.w2, 64, pyxel.COLOR_PURPLE)
        if 110 <= self.timer <= 109 + 64 // self.animatiesnelheid:
            self.w2 += self.animatiesnelheid
        if 110 + (256 // self.animatiesnelheid) <= self.timer:# <= 110 + (128 // self.animatiesnelheid):
            self.u2 += self.animatiesnelheid
            self.w2 -= self.animatiesnelheid
            self.x2 += self.animatiesnelheid

        if self.timer >= 120 + 128 // self.animatiesnelheid + (109 + 64 // self.animatiesnelheid):
            self.verschil = 0
            game.aan_het_spelen = True
            if len(game.terrein) < 17:
                terrein.randomterrein(game)
                game.aan_het_spelen = True
            # game.geselecterde_kleur = int(random.triangular(0, 5))
            # game.voorbeeldeenheid = game.geselecterde_kleur

    def vergroot(self, game):
        if self.w >= 15:
            self.verschil = 0
            self.ben_ik_voledig_zichtbaar = True
        if not game.toon_menu:
            pyxel.rect(self.x + game.begin_teken_x * 16, self.y + game.begin_teken_y * 16, self.w, self.h, self.c)
            self.w += 2 * self.verschil
            self.h += 2 * self.verschil
            self.x -= self.verschil
            self.y -= self.verschil


    def verklijn(self, game):
        self.ben_ik_voledig_zichtbaar = False
        if self.w <= -1:
            self.w = -1
            self.verschil = 0
        pyxel.rect(self.x + game.begin_teken_x * 16, self.y + game.begin_teken_y * 16, self.w, self.h, self.c)
        self.w += 2 * self.verschil
        self.h += 2 * self.verschil
        self.x -= self.verschil
        self.y -= self.verschil
        # print(self.w)
