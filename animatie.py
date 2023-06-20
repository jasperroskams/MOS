import pyxel
X = 0
Y = 1
T = 2
N = 3
C = 4

animetie1 = [
    [ 64, 128, 2, 1, 0],
    [ 80, 128, 2, 2, 0],
    [ 96, 128, 2, 3, 0],
    [112, 128, 2, 2, 0],
    [128, 128, 2, 1, 0],

    [ 64, 64, 0, 1, 1],
    [ 80, 64, 0, 1, 1],
    [ 96, 64, 0, 1, 1],
    [112, 64, 0, 1, 1],
    [128, 64, 0, 1, 1],

]

senario1 = [
    [[ 800, 0, -0.02], [3200, 0, -0.01], [3800, 0, 0]],
    [[ 500, 0, -0.02], [2900, 0, -0.01], [3800, 0, 0]],
    [[ 100, 0, -0.02], [2600, 0, -0.01], [3800, 0, 0]],
    [[ 500, 0, -0.02], [2900, 0, -0.01], [3800, 0, 0]],
    [[ 800, 0, -0.02], [3200, 0, -0.01], [3800, 0, 0]],

    [[0000, 0, 0], [3200, 0, -0.01], [3800, 0, 0]],
    [[0000, 0, 0], [2900, 0, -0.01], [3800, 0, 0]],
    [[0000, 0, 0], [2600, 0, -0.01], [3800, 0, 0]],
    [[0000, 0, 0], [2900, 0, -0.01], [3800, 0, 0]],
    [[0000, 0, 0], [3200, 0, -0.01], [3800, 0, 0]],

]


class Animatie():
    def __init__(self):
        self.timer = 0
        self.ii = 0

    def update(self):
        self.timer += 1
        for i, eenhijd in enumerate(animetie1):
            pyxel.blt(eenhijd[X], eenhijd[Y], 0, eenhijd[N] * 16, eenhijd[C] * 32, 16, 16, pyxel.COLOR_BLACK)
            pyxel.blt(eenhijd[X], eenhijd[Y], 0, eenhijd[T] * 16, 16 + eenhijd[C] * 32, 16, 16, pyxel.COLOR_BLACK)
            # print(self.timer)
            if i == 0:
                print(self.ii, i,  self.timer)
            if len(senario1[i]) > self.ii + 1:
                if self.timer == senario1[i][self.ii + 1][0]:
                    self.ii += 1
                    if len(senario1) <= i + 1:
                        i = -1
                    if self.timer < senario1[i + 1][self.ii][0]:
                        self.ii -= 1
            if self.timer >= senario1[i][self.ii][0]:
                eenhijd[X] += senario1[i][self.ii][1]
                eenhijd[Y] += senario1[i][self.ii][2]






