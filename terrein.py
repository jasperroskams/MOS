
import random
import pyxel
import time

testerrein = [
    [0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 3, 3, 3, 3, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 3, 3, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 3, 3],
    [1, 1, 1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 4, 1, 1, 1, 4, 4, 0, 0, 0, 2, 2, 2],
    [1, 1, 1, 1, 6, 1, 1, 1, 1, 4, 2, 2, 2, 2, 0, 0],
    [1, 1, 1, 1, 2, 2, 2, 2, 2, 5, 2, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0],
]

vlakterrein = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

RIVIER = 0
WEG = 1
BOS = 2
BERG = 3
GEBOUW = 4
MEER = 5
ZEE = 6
lijst_met_terijnkleuren = [11, 3, 6, 13, 15, 4, 14, 13, 4]


def getTerrein():
    global vlakterrein
    return vlakterrein

class terein_instelling():
    def __init__(self, naam, kans, grote):
        self.naam = naam
        self.kans = kans
        self.grote = grote


def randomterrein(game):
    breedte = int(game.game_breedte / 16 - 1)
    hoogte = int(game.game_hoogte / 16 - 1)
    global vlakterrein
    vlakterrein = []
    for i in range(hoogte + 1):
        vlakterrein.append([0] * (breedte + 1))
    is_er_een_rivier = int(random.triangular(0, 10))
    is_er_een_weg = int(random.triangular(0, 10))
    is_er_een_bos = int(random.triangular(0, 10))
    is_er_een_berg = int(random.triangular(0, 10))
    is_er_een_gebouw = int(random.triangular(0, 10))
    is_er_een_meer = int(random.triangular(0, 20))
    is_er_een_stad = int(random.triangular(0, 20))
    is_er_een_zee = int(random.triangular(0, 20))
    # print(game.weg_grote)

    grote_zee = int(random.triangular(3, game.terein_instelingen[ZEE].grote * game.grootte + 3))
    if is_er_een_zee < game.terein_instelingen[ZEE].kans + game.grootte / 2:
        for x in range (0, breedte + 1):
            for y in range (0, grote_zee):
                ga_ik_zee_zetten = int(random.triangular(grote_zee - 2, grote_zee))
                if ga_ik_zee_zetten > y:
                    vlakterrein[y][x] = 2



    if is_er_een_meer < game.terein_instelingen[MEER].kans + game.grootte:
        # aantal_bossen = int(random.triangular(1, game.groote * 2))
        # for i in range (0, aantal_bossen):
        xpos = int(random.triangular(0, breedte))
        ypos = int(random.triangular(0, hoogte))
        grote_meer = int (random.triangular(0, game.terein_instelingen[MEER].grote * 64 * game.grootte))
        for i in range(0, grote_meer):
            xpos += int(random.triangular(-20, 20) / 10)
            ypos += int(random.triangular(-20, 20) / 10)
            if ypos > hoogte:
                ypos = hoogte
            if ypos < 0:
                ypos = 0
            if xpos > breedte:
                xpos = breedte
            if xpos < 0:
                xpos = 0
            # print(ypos, xpos)
            vlakterrein[ypos][xpos] = 2




    if is_er_een_rivier < game.terein_instelingen[RIVIER].kans + game.grootte:
        aantal_rivieren = int(random.triangular(1, game.grootte))
        while aantal_rivieren > 2:
            aantal_rivieren /= 2
            aantal_rivieren = int(aantal_rivieren)
            # print(aantal_rivieren)
        for i in range (0, aantal_rivieren):
            grote_rivier = int(random.triangular(1, game.terein_instelingen[RIVIER].grote + game.grootte + 1))
            rirchting = int(random.triangular(0, 16))
            if rirchting < 8:
                xpos = int(random.triangular(0, breedte))
                ypos = 0
                doel = hoogte + 1
            if rirchting >= 8:
                ypos = int(random.triangular(0, hoogte))
                xpos = 0
                doel = breedte + 1
            if rirchting < 8:
                while ypos != doel:
                    # print(ypos, xpos)
                    for i in range (0, grote_rivier):
                        if xpos + i >= breedte:
                            xpos = breedte - i
                        if xpos < 0:
                            xpos = 0
                        vlakterrein[ypos][xpos + i] = 2
                    ypos += 1
                    xpos += int(random.triangular(-18, 18) / 10)

            if rirchting > 8:
                while xpos != doel:
                    # print(ypos, xpos)
                    for i in range (0, grote_rivier):
                        if xpos + i <= len(vlakterrein):
                            vlakterrein[ypos + i][xpos] = 2############################
                    xpos += 1
                    ypos += int(random.triangular(-14, 14) / 10)
                    if ypos > hoogte - i:
                        ypos = hoogte
                    if ypos < 0:
                        ypos = 0



    if is_er_een_stad < -16 + game.grootte:
        aantal_steden = int(random.triangular(1, game.grootte))
        for i in range(0, aantal_steden):
            grote_stad = int(random.triangular(3, 6 + game.grootte))
            xpos = int(random.triangular(0, breedte))
            ypos = int(random.triangular(0, hoogte))
            if xpos + grote_stad > breedte:
                xpos = breedte - grote_stad
            if ypos + grote_stad > breedte:
                ypos = breedte - grote_stad
            for x in range(0, grote_stad):
                for y in range(0, grote_stad):
                    if (x == 0 or x == grote_stad - 1) or (y == 0 or y == grote_stad - 1):
                        if vlakterrein[xpos + x][ypos + y] != 2:
                            vlakterrein[xpos + x][ypos + y] = 7
                    else:
                        if vlakterrein[xpos + x][ypos + y] != 2:
                            vlakterrein[xpos + x][ypos + y] = 4
                    if vlakterrein[xpos + x][ypos + y] == 2:
                        zet_ik_een_brug_in_stad = int(random.triangular(0, 10))
                        if zet_ik_een_brug_in_stad < 3:
                            vlakterrein[xpos + x][ypos + y] = 5



    if is_er_een_weg < game.terein_instelingen[WEG].kans + game.grootte:
        aantal_wegen = int(random.triangular(1, game.grootte))
        while aantal_wegen > 2:
            aantal_wegen /= 2
            aantal_wegen = int(aantal_wegen)
        for i in range (0, aantal_wegen):
            aantal_geleden_vorige_verspringing = 0
            grote_weg = int(random.triangular(1, game.terein_instelingen[WEG].grote + game.grootte + 1))
            rirchting = int(random.triangular(0, 16))
            if is_er_een_zee < 1 + game.grootte / 2:
                rirchting = 10
            if rirchting < 8:
                xpos = int(random.triangular(0, breedte))
                ypos = 0
                doel = hoogte + 1
            if rirchting >= 8:
                ypos = int(random.triangular(0, hoogte))
                xpos = 0
                doel = breedte + 1
            if is_er_een_zee < 1 + game.grootte / 2:
                if ypos <= grote_zee + game.grootte:
                    ypos = grote_zee + game.grootte
            vorige_x = xpos
            vorige_y = ypos
            if rirchting < 8:
                while ypos != doel:
                    # print(ypos, xpos)
                    for i in range (0, grote_weg):
                        if vorige_x != xpos:
                            if vorige_x + i <= len(vlakterrein):
                                if vlakterrein[ypos][vorige_x + i] == 2:
                                    vlakterrein[ypos][vorige_x + i] = 5
                                elif vlakterrein[ypos][vorige_x + i] == 7:
                                    vlakterrein[ypos][vorige_x + i] = 8
                                else:
                                    vlakterrein[ypos][vorige_x + i] = 4
                                aantal_geleden_vorige_verspringing = 0
                        if xpos + i <= len(vlakterrein):
                            if vlakterrein[ypos][xpos + i] == 2:#######################################
                                vlakterrein[ypos][xpos + i] = 5
                            elif vlakterrein[ypos][xpos + i] == 7:
                                vlakterrein[ypos][xpos + i] = 8
                            else:
                                vlakterrein[ypos][xpos + i] = 4
                    ypos += 1
                    vorige_x = xpos
                    if aantal_geleden_vorige_verspringing < 10:
                        aantal_geleden_vorige_verspringing += 1
                    xpos += int(random.triangular(-16, 16) / (20 - aantal_geleden_vorige_verspringing))
                    if xpos > breedte:
                        xpos = breedte
                    if xpos < 0:
                        xpos = 0
            if rirchting > 8:
                while xpos != doel:
                    if vorige_y != ypos:
                        if vorige_y + i <= len(vlakterrein):
                            if vlakterrein[vorige_y][xpos] == 2:
                                vlakterrein[vorige_y][xpos] = 5
                            elif vlakterrein[vorige_y][xpos] == 7:
                                vlakterrein[vorige_y][xpos] = 8
                            else:
                                vlakterrein[vorige_y][xpos] = 4
                            aantal_geleden_vorige_verspringing = 0
                    if ypos + i <= len(vlakterrein):
                        if vlakterrein[ypos][xpos] == 2:
                            vlakterrein[ypos][xpos] = 5
                        elif vlakterrein[ypos][xpos] == 7:
                            vlakterrein[ypos][xpos] = 8
                        else:
                            vlakterrein[ypos][xpos] = 4
                    xpos += 1
                    vorige_y = ypos
                    if aantal_geleden_vorige_verspringing < 10:
                        aantal_geleden_vorige_verspringing += 1
                    ypos += int(random.triangular(-14, 14) / (20 - aantal_geleden_vorige_verspringing))
                    if ypos > hoogte:
                        ypos = hoogte
                    if ypos < 0:
                        ypos = 0


    if is_er_een_bos < game.terein_instelingen[BOS].kans + game.grootte:
        aantal_bossen = int(random.triangular(1, game.grootte * 2))
        for i in range (0, aantal_bossen):
            xpos = int(random.triangular(0, breedte))
            ypos = int(random.triangular(-24, hoogte + 24))
            grote_bos = int (random.triangular(0, game.terein_instelingen[BOS].grote * 32 * game.grootte))
            for i in range(0, grote_bos):
                vorige_x = xpos
                xpos += int(random.triangular(-17, 17) / 10)
                if vorige_x == xpos:
                    ypos += int(random.triangular(-20, 20) / 10)
                if ypos > hoogte:
                    ypos = hoogte
                if ypos < 0:
                    ypos = 0
                if xpos > breedte:
                    xpos = breedte
                if xpos < 0:
                    xpos = 0
                # print(ypos, xpos)
                if vlakterrein[ypos][xpos] == 0:
                    vlakterrein[ypos][xpos] = 1
                if xpos != 0:
                    if vlakterrein[ypos][xpos-1] == 0:
                        vlakterrein[ypos][xpos-1] = 1
                if ypos != 0:
                    if vlakterrein[ypos-1][xpos] == 0:
                        vlakterrein[ypos-1][xpos] = 1
                if xpos != breedte:
                    if vlakterrein[ypos][xpos+1] == 0:
                       vlakterrein[ypos][xpos+1] = 1
                if ypos != breedte:
                    if vlakterrein[ypos+1][xpos] == 0:
                        vlakterrein[ypos+1][xpos] = 1
        # for rij in vlakterrein:
            # print(rij)
        aantal_naast = 0
        max_aantal_naast = 4
        while max_aantal_naast >= 3:
            for y, rij in enumerate(vlakterrein):
                for x, tegel in enumerate(rij):
                    if y != 0 and y != hoogte and x != 0 and x != breedte:
                        if vlakterrein[y-1][x] == 1:
                            aantal_naast += 1
                        if vlakterrein[y][x-1] == 1:
                            aantal_naast += 1
                        if vlakterrein[y][x+1] == 1:
                            aantal_naast += 1
                        if vlakterrein[y+1][x] == 1:
                            aantal_naast += 1
                        if aantal_naast >= max_aantal_naast:
                            if vlakterrein[y][x] == 0:
                                print(vlakterrein[y][x])
                                vlakterrein[y][x] = 1
                                print(vlakterrein[y][x])
                        aantal_naast = 0
            max_aantal_naast -= 1
        # print('')
        # for rij in vlakterrein:
        #     print(rij)



    if is_er_een_berg < game.terein_instelingen[BERG].kans + game.grootte:
        aantal_bergen = int(random.triangular(1, game.grootte * 2))
        for i in range (0, aantal_bergen):
            xpos = int(random.triangular(0, breedte))
            ypos = int(random.triangular(0, hoogte))
            grote_berg = int(random.triangular(0, game.terein_instelingen[BERG].grote * 16))
            for i in range(0, grote_berg):
                xpos += int(random.triangular(-20, 20) / 10)
                ypos += int(random.triangular(-20, 20) / 10)
                if ypos > hoogte:
                    ypos = hoogte
                if ypos < 0:
                    ypos = 0
                if xpos > breedte:
                    xpos = breedte
                if xpos < 0:
                    xpos = 0
                # print(ypos, xpos)
                if vlakterrein[ypos][xpos] == 0:
                    vlakterrein[ypos][xpos] = 3
                if xpos != 0:
                    if vlakterrein[ypos][xpos-1] == 0:
                        vlakterrein[ypos][xpos-1] = 3
                if ypos != 0:
                    if vlakterrein[ypos-1][xpos] == 0:
                        vlakterrein[ypos-1][xpos] = 3
                if xpos != breedte:
                    if vlakterrein[ypos][xpos+1] == 0:
                       vlakterrein[ypos][xpos+1] = 3
                if ypos != breedte:
                    if vlakterrein[ypos+1][xpos] == 0:
                        vlakterrein[ypos+1][xpos] = 3

        aantal_naast = 0
        max_aantal_naast = 4
        while max_aantal_naast >= 3:
            for y, rij in enumerate(vlakterrein):
                for x, tegel in enumerate(rij):
                    if y != 0 and y != hoogte and x != 0 and x != breedte:
                        if vlakterrein[y-1][x] == 3:
                            aantal_naast += 1
                        if vlakterrein[y][x-1] == 3:
                            aantal_naast += 1
                        if vlakterrein[y][x+1] == 3:
                            aantal_naast += 1
                        if vlakterrein[y+1][x] == 3:
                            aantal_naast += 1
                        if aantal_naast >= max_aantal_naast:
                            if vlakterrein[y][x] == 0:
                                # print(vlakterrein[y][x])
                                vlakterrein[y][x] = 3
                                # print(vlakterrein[y][x])
                        aantal_naast = 0
            max_aantal_naast -= 1


    aantal_gebouwen = int(random.triangular(-10 + game.terein_instelingen[GEBOUW].kans, game.grootte * 4))
    # print(aantal_gebouwen)
    for i in range(0, aantal_gebouwen):
        xpos = int(random.triangular(0, breedte))
        ypos = int(random.triangular(0, hoogte))
        grote_gebouw = int(random.triangular(0, 4 * game.grootte))
        for i in range(0, grote_gebouw):
            xpos += int(random.triangular(-20, 20) / 10)
            ypos += int(random.triangular(-20, 20) / 10)
            if ypos > hoogte:
                ypos = hoogte
            if ypos < 0:
                ypos = 0
            if xpos > breedte:
                xpos = breedte
            if xpos < 0:
                xpos = 0
            # print(ypos, xpos)
            if vlakterrein[ypos][xpos] == 0:
                vlakterrein[ypos][xpos] = 6

    # print('////')
    # for rij in vlakterrein:
    #     print(rij)






