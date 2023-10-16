
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

def getTerrein():
    global vlakterrein
    return vlakterrein




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
    print(game.weg_grote)

    grote_zee = int(random.triangular(3, game.zee_grote * game.grootte + 3))
    if is_er_een_zee < game.zee_kans + game.grootte / 2:
        for x in range (0, breedte + 1):
            for y in range (0, grote_zee):
                ga_ik_zee_zetten = int(random.triangular(grote_zee - 2, grote_zee))
                if ga_ik_zee_zetten > y:
                    vlakterrein[y][x] = 2



    if is_er_een_meer < game.meer_kans + game.grootte:
        # aantal_bossen = int(random.triangular(1, game.groote * 2))
        # for i in range (0, aantal_bossen):
        xpos = int(random.triangular(0, breedte))
        ypos = int(random.triangular(0, hoogte))
        grote_meer = int (random.triangular(0, game.meer_grote * 64 * game.grootte))
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




    if is_er_een_rivier < game.rivier_kans + game.grootte:
        aantal_rivieren = int(random.triangular(1, game.grootte))
        while aantal_rivieren > 2:
            aantal_rivieren /= 2
            aantal_rivieren = int(aantal_rivieren)
            # print(aantal_rivieren)
        for i in range (0, aantal_rivieren):
            grote_rivier = int(random.triangular(1, game.rivier_grote + game.grootte + 1))
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
                            vlakterrein[ypos + i][xpos] = 2
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



    if is_er_een_weg < game.weg_kans + game.grootte:
        aantal_wegen = int(random.triangular(1, game.grootte))
        while aantal_wegen > 2:
            aantal_wegen /= 2
            aantal_wegen = int(aantal_wegen)
        for i in range (0, aantal_wegen):
            grote_weg = int(random.triangular(1, game.weg_grote + game.grootte + 1))
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
                        if xpos + i <= len(vlakterrein):
                            if vlakterrein[ypos][xpos + i] == 2:
                                vlakterrein[ypos][xpos + i] = 5
                            elif vlakterrein[ypos][xpos + i] == 7:
                                vlakterrein[ypos][xpos + i] = 8
                            else:
                                vlakterrein[ypos][xpos + i] = 4
                    ypos += 1
                    vorige_x = xpos
                    xpos += int(random.triangular(-18, 18) / 10)
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
                    if ypos + i <= len(vlakterrein):
                        if vlakterrein[ypos][xpos] == 2:
                            vlakterrein[ypos][xpos] = 5
                        elif vlakterrein[ypos][xpos] == 7:
                            vlakterrein[ypos][xpos] = 8
                        else:
                            vlakterrein[ypos][xpos] = 4
                    xpos += 1
                    vorige_y = ypos
                    ypos += int(random.triangular(-14, 14) / 10)
                    if ypos > hoogte:
                        ypos = hoogte
                    if ypos < 0:
                        ypos = 0



    if is_er_een_bos < game.bos_kans + game.grootte:
        aantal_bossen = int(random.triangular(1, game.grootte * 2))
        for i in range (0, aantal_bossen):
            xpos = int(random.triangular(0, breedte))
            ypos = int(random.triangular(0, hoogte))
            grote_bos = int (random.triangular(0, game.bos_grote * 32 * game.grootte))
            for i in range(0, grote_bos):
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
                    vlakterrein[ypos][xpos] = 1



    if is_er_een_berg < game.berg_kans + game.grootte:
        aantal_bergen = int(random.triangular(1, game.grootte * 2))
        for i in range (0, aantal_bergen):
            xpos = int(random.triangular(0, breedte))
            ypos = int(random.triangular(0, hoogte))
            grote_berg = int(random.triangular(0, game.berg_grote * 16))
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



    aantal_gebouwen = int(random.triangular(-10 + game.gebouw_aantal, game.grootte * 4))
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

    print('////')
    # for rij in vlakterrein:
    #     print(rij)






