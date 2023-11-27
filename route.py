
from terrein import *
ondergrond_impact = [2, 3, 5, 3, 1, 1, 2]
ondergrond_impact_boot = [200, 200, 2, 200, 200, 200, 200]
uithouding_terijn = [1, 1.5, 3, 2, 0.5, 0.5, 1]
uithouding_terijn_boot = [100, 100, 1, 200, 500, 500, 100]
bouwsel_impact =     [0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
uithouding_bouwsel = [0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
nieuwe_lijst_met_tegels = []
veld_met_tegels = []
terijn = getTerrein()
for rij in terijn:
    veld_met_tegels.append([0] * len(rij))
X = 0
Y = 1
VORIGE = 2
BEWEGEN = 3
UITHOUDING = 4



def kan_ik_tot_hier(eind_x, eind_y, game, eenheid):
    global nieuwe_lijst_met_tegels, veld_met_tegels, terijn
    lijst_met_tegels = []
    kortse_weg = [0, 0, 0, 20, 0]
    begin_x = eenheid.x // 16
    begin_y = eenheid.y // 16
    bewegen = eenheid.bewegen
    boot = eenheid.boot
    tegel = [begin_x, begin_y, [begin_x, begin_y, 0], bewegen, 0]
    lijst_met_tegels.append(tegel)
    veld_met_tegels = []
    terijn = getTerrein()
    for rij in terijn:
        veld_met_tegels.append([0] * len(rij))
    while len(lijst_met_tegels) > 0:
        nieuwe_lijst_met_tegels = []
        for tegel in lijst_met_tegels:
            if tegel[X] == eind_x and tegel[Y] == eind_y and tegel[BEWEGEN] > -1:
                if kortse_weg[BEWEGEN] > tegel[BEWEGEN]:
                    kortse_weg = tegel

            rondom_kijken(tegel[X], tegel[Y], tegel[BEWEGEN], tegel[VORIGE], boot, game)
        lijst_met_tegels = nieuwe_lijst_met_tegels
    if kortse_weg[BEWEGEN] < 20:
        # print('True')
        vorige_tegel = kortse_weg[VORIGE]
        if eenheid.boot == 1:
            kortse_weg[UITHOUDING] = uithouding_terijn[terijn[kortse_weg[Y]][kortse_weg[X]]]
            kortse_weg[UITHOUDING] -= uithouding_terijn[terijn[begin_y][begin_x]]
            while len(vorige_tegel) >= 4:
                kortse_weg[UITHOUDING] += uithouding_terijn[terijn[vorige_tegel[Y]][vorige_tegel[X]]]
                game.highlight((vorige_tegel[X] + game.begin_teken_x) * 16, (vorige_tegel[Y] + game.begin_teken_y) * 16)
                vorige_tegel = vorige_tegel[VORIGE]
        else:
            kortse_weg[UITHOUDING] = uithouding_terijn_boot[terijn[kortse_weg[Y]][kortse_weg[X]]]
            kortse_weg[UITHOUDING] -= uithouding_terijn_boot[terijn[begin_y][begin_x]]
            while len(vorige_tegel) >= 4:
                kortse_weg[UITHOUDING] += uithouding_terijn_boot[terijn[vorige_tegel[Y]][vorige_tegel[X]]]
                game.highlight((vorige_tegel[X] + game.begin_teken_x) * 16, (vorige_tegel[Y] + game.begin_teken_y) * 16)
                vorige_tegel = vorige_tegel[VORIGE]
        # print(kortse_weg[4])
        return kortse_weg
    else:
        # print('False')
        return False


def rondom_kijken(begin_x, begin_y, begin_bewegen, vorige, boot, game):
    # print(vorige)
    for x in range(-1, 2):
        for y in range(-1, 2):
            xPos = begin_x + x
            yPos = begin_y + y
            if x == 0 or y == 0:
                if 0 <= xPos < len(terijn) and 0 <= yPos < len(terijn):
                    bewegen = begin_bewegen
                    if boot == 1:
                        bewegen -= ondergrond_impact[terijn[yPos][xPos]]


                        bewegen -= bouwsel_impact[game.bouwsels[yPos][xPos]]
                    else:
                        bewegen -= ondergrond_impact_boot[terijn[yPos][xPos]]
                    if bewegen >= 0:
                        if veld_met_tegels[yPos][xPos] <= bewegen:
                            veld_met_tegels[yPos][xPos] = bewegen
                            newvorige = vorige
                            uithouding = 0
                            while len(newvorige) > 3:
                                newvorige = newvorige[VORIGE]
                            if len(newvorige) > 3:
                                uithouding = newvorige[UITHOUDING] + uithouding_terijn[terijn[yPos][xPos]] + uithouding_bouwsel[game.bouwsels[yPos][xPos]]
                            # print(vorige)
                            tegel = [xPos, yPos, [begin_x, begin_y, vorige, bewegen, uithouding], bewegen, uithouding]
                            nieuwe_lijst_met_tegels.append(tegel)


# kan_ik_tot_hier(8, 0, 12, 9, 12)
print('.')
