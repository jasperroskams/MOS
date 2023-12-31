import math
import random

import pyxel
from terrein import testerrein, getTerrein
ondergrond_impact = [2, 3, 5, 3, 1, 1, 2]
ondergrond_impact_boot = [20, 20, 2, 20, 20, 20, 20]


VERDEDIGEN = 0
AANVALLEN = 1
AANVALLENMORAAL = 2
GEZONDHEID = 3
MORAAL = 4
BEWEGEN = 5
BEREIK = 6
UITHOUDING = 7
ZICHT = 8
UITHOUDING_TERUGKRIJGEN = 9
ZICHTBAARHEID = 10
MORAAL_VERDEDIGEN = 11
MUNITIE = 12
KAN_IK_BOUWEN = 13
DUWEN = 14
DUWBAARHIJD = 15
GRAS = 0
BOS = 1
WATER = 2
BERG = 3
WEG = 4
BRUG = 5
GEBOUW = 6
MUUR = 7
POORT = 8


eenheden_sterren = [
    [
        [
            [5, 7, 12, 0],
            [6, 10, 0, 0],
            [14, 14, 17, 21],
            [8, 10, 0, 0],
            [9, 12, 0, 0],
            [5, 7, 0, 0],
        ],
        [
            [6, 10, 15, 0],
            [0, 8, 0, 0],
            [8, 9, 13, 17],
            [10, 12, 13, 0],
            [9, 10, 0, 0],
            [6, 8, 13, 0],
        ],
        [
            [8, 13, 16, 19],
            [4, 7, 0, 0],
            [8, 9, 11, 0],
            [7, 0, 0, 0],
            [9, 11, 0, 0],
            [4, 6, 0, 0],
        ],
        [
            [4, 7, 11, 0],
            [4, 9, 0, 0],
            [8, 9, 12, 14],
            [6, 9, 0, 0],
            [13, 13, 20, 0],
            [3, 4, 0, 0],
        ],
        [
            [2, 6, 11, 0],
            [10, 14, 19, 0],
            [8, 9, 17, 15],
            [0, 0, 0, 0],
            [10, 11, 15, 0],
            [5, 8, 0, 0],
        ],
    ],
    [
        [
            [2, 5, 9, 0],
            [4, 5, 0, 0],
            [10, 11, 12, 14],
            [2, 4, 0, 0],
            [4, 6, 0, 0],
            [0, 1, 0, 0],
        ],
        [
            [4, 6, 9, 0],
            [5, 0, 0, 0],
            [3, 5, 6, 10],
            [3, 5, 10, 0],
            [4, 6, 0, 0],
            [0, 2, 5, 0],
        ],
        [
            [7, 10, 14, 18],
            [0, 2, 0, 0],
            [4, 5, 8, 0],
            [1, 0, 0, 0],
            [2, 5, 0, 0],
            [0, 0, 0, 0],
        ],
        [
            [2, 5, 9, 0],
            [0, 4, 0, 0],
            [6, 5, 6, 8],
            [1, 3, 0, 0],
            [6, 7, 13, 0],
            [0, 0, 0, 0],
        ],
        [
            [0, 3, 7, 0],
            [7, 11, 16, 0],
            [3, 5, 8, 11],
            [0, 0, 0, 0],
            [2, 6, 10, 0],
            [0, 2, 0, 0],
        ],
    ],
]

class Eenheid():

    eenheden = [
     [#booten
         [  # T0
             # blauw
             [
                 # transport
                 [
                     # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                     [  25,   1,   1,  21,  12,   6,   1,   8,   8,   1,   3,   2,   0,   0,   0,   0],  # I
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # II
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                 ],
                 # oorlog
                 [
                     # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                     [  40,   6,   3,  24,  15,   8,   2,   8,  10,   3,   3,   2,   4],  # I
                     [  55,   8,   4,  27,  18,   6,   3,  10,   8,   3,   3,   2,   5],  # II
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                     [  75,  12,   5,  33,  21,   8,   4,  12,  10,   4,   2,   4,   6],  # IV
                 ],
             ],
             # paars
             [
                 # transport
                 [
                     # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                     [  30,   4,   2,  24,  15,   6,   1,   8,   8,   1,   3,   1,   0],  # I
                     [  35,   5,   3,  27,  18,   6,   1,   8,   8,   2,   3,   2,   0],  # II
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                 ],
                 # oorlog
                 [
                     # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                     [  50,   5,   3,  24,  18,   8,   3,  10,   8,   3,   3,   2,   3],  # I
                     [  60,   7,   4,  27,  18,   6,   0,  12,   8,   3,   3,   3,   0],  # II
                     [  70,   9,   4,  30,  21,   6,   5,  12,   8,   3,   2,   3,   4],  # III
                     [  80,  11,   5,  33,  24,   6,   6,  14,   9,   3,   1,   4,   5],  # IV
                 ],
             ],
             # wit
             [
                 # transport
                 [
                     # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                     [  20,   3,   2,  21,  15,   6,   1,   8,   8,   2,   3,   2,   0],  # I
                     [  30,   4,   3,  24,  18,   6,   1,   8,   8,   3,   3,   2,   0],  # II
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                 ],
                 # oorlog
                 [
                     # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                     [  65,   5,   4,  21,  15,  10,   3,  12,   9,   3,   3,   2,   5],  # I
                     [  75,   6,   4,  21,  18,   8,   0,  14,   8,   3,   3,   3,   0],  # II
                     [  85,   8,   5,  24,  18,   8,   0,  16,   8,   4,   2,   4,   0],  # III
                     [  90,  10,   5,  27,  21,   8,   6,  20,   9,   4,   2,   4,   6],  # IV
                 ],
             ],
             # rood
             [
                 # transport
                 [
                     # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                     [  25,   3,   2,  21,  12,   6,   4,   8,   8,   2,   3,   2,   2],  # I
                     [  30,   4,   3,  24,  15,   6,   4,   8,   8,   3,   3,   2,   3],  # II
                     [  40,   6,   3,  30,  18,   6,   5,  12,   8,   3,   3,   3,   4],  # III
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                 ],
                 # oorlog
                 [
                     # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                     [  65,  14,   4,  30,  21,  10,   8,   8,  10,   3,   3,   3,  10],  # I
                     [  75,  16,   5,  36,  24,  12,   8,  10,   9,   3,   3,   4,  10],  # II
                     [  85,  18,   5,  42,  24,  10,  10,  10,   9,   4,   2,   5,  12],  # III
                     [  95,  20,   6,  45,  27,  10,  12,  10,  10,   5,   2,   6,  12],  # IV
                 ],
             ],
             # geel
             [
                 # transport
                 [
                     # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                     [  15,   2,   3,  21,  12,   6,   1,   8,   8,   2,   3,   2,   0],  # I
                     [  20,   4,   3,  24,  15,   6,   1,   8,   8,   3,   3,   2,   0],  # II
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                 ],
                 # oorlog
                 [
                     # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                     [  45,   8,   3,  24,  15,   6,   4,   6,   8,   2,   4,   2,   5],  # I
                     [  60,  10,   4,  27,  18,   8,   4,   8,   8,   3,   4,   3,   6],  # II
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   4,   0,   0],  # III
                     [  80,  14,   5,  33,  21,   6,   4,   8,   8,   4,   4,   4,   8],  # IV
                 ],
             ],
         ],
        [  # T1
            # blauw
            [
                # transport
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  30,   2,   1,  21,  12,   6,   1,   8,   8,   3,   3,   1,   0],  # I
                    [  35,   3,   1,  24,  15,   6,   1,  10,   8,   3,   3,   2,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # oorlog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  40,   5,   2,  24,  15,  10,   4,   6,   8,   3,   3,   2,   8],  # I
                    [  50,   7,   2,  30,  18,   8,   5,   8,   8,   3,   3,   2,  10],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [  70,  14,   3,  36,  21,   6,   6,  10,   8,   5,   2,   3,  14],  # IV
                ],
            ],
            # paars
            [
                # transport
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  25,   3,   1,  21,  12,   6,   1,   8,  10,   3,   3,   2,   0],  # I
                    [  30,   4,   1,  21,  15,   6,   1,   8,   8,   3,   3,   2,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # oorlog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  30,   4,   3,  24,  18,   8,   3,   6,   9,   3,   3,   2,   4],  # I
                    [  40,   6,   3,  24,  18,   6,   5,   8,   8,   4,   3,   2,   5],  # II
                    [  50,   4,   9,  27,  21,   8,   3,   8,   8,   4,   3,   3,   6],  # III
                    [  60,  12,   4,  30,  24,   6,   5,  10,   8,   5,   2,   4,   8],  # IV
                ],
            ],
            # wit
            [
                # transport
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  20,   2,   1,  21,  12,   6,   1,   8,   8,   3,   3,   2,   0],  # I
                    [  25,   3,   1,  21,  15,   8,   1,   8,   8,   3,   3,   2,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # oorlog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  35,   3,   2,  24,  15,   6,   4,   6,   8,   3,   3,   2,   4],  # I
                    [  45,   5,   3,  24,  18,   6,   4,   8,   8,   3,   3,   2,   5],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [  55,   8,   3,  27,  21,   6,   5,   8,   8,   3,   2,   3,   6],  # IV
                ],
            ],
            # rood
            [
                # transport
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  20,   3,   1,  21,  12,   5,   1,   8,   8,   3,   3,   2,   0],  # I
                    [  30,   4,   1,  24,  15,   5,   3,   8,   8,   4,   3,   2,   3],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # oorlog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  50,   8,   3,  24,  18,   8,   5,   8,   9,   3,   3,   3,   6],  # I
                    [  60,  10,   3,  27,  21,  10,   5,  10,   8,   4,   3,   3,   7],  # II
                    [  70,  12,   4,  30,  21,   8,   6,  10,   8,   4,   3,   4,   8],  # III
                    [  80,  14,   5,  33,  24,   8,   7,  12,   9,   5,   2,   5,  10],  # IV
                ],
            ],
            # geel
            [
                # transport
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  20,   2,   1,  21,  12,   6,   1,   8,   8,   2,   3,   2,   0],  # I
                    [  25,   3,   1,  21,  15,   6,   1,   8,   8,   3,   3,   2,   0],  # II
                    [  30,   4,   1,  24,  18,   6,   3,  12,   8,   4,   3,   3,   3],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # oorlog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  35,   4,   2,  24,  15,   6,   4,   6,   8,   2,   3,   2,   5],  # I
                    [  40,   6,   3,  24,  18,   8,   4,   8,   8,   3,   3,   2,   6],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [  60,   9,   4,  27,  21,   6,   5,   8,   8,   3,   2,   3,   8],  # IV
                ],
            ],
        ],

        [  # T2
            # blauw
            [
                # transport
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  30,   2,   2,  21,  12,   6,   1,   8,   8,   1,   3,   2,   0],  # I
                    [  35,   3,   2,  21,  15,   6,   1,   8,   8,   2,   3,   2,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # oorlog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  60,   8,   3,  24,  15,   6,   6,   8,  10,   3,   3,   2,   6],  # I
                    [  70,  10,   4,  27,  18,   6,   7,   8,   8,   3,   3,   2,   6],  # II
                    [  80,  13,   4,  30,  21,   8,   8,  10,   8,   4,   3,   3,   8],  # III
                    [  85,  15,   5,  33,  21,   8,   9,  12,  10,   5,   2,   4,  10],  # IV
                ],
            ],
            # paars
            [
                # transport
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  25,   2,   2,  21,  12,   6,   1,   8,   8,   1,   3,   1,   0],  # I
                    [  35,   3,   2,  24,  15,   6,   1,   8,   8,   2,   3,   2,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # oorlog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  50,   8,   3,  24,  15,   6,   6,   8,   8,   3,   3,   2,   6],  # I
                    [  65,  10,   4,  24,  18,   6,   6,   8,   8,   3,   3,   3,   6],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [  80,  12,   5,  30,  24,   6,   8,   8,   9,   4,   2,   4,   8],  # IV
                ],
            ],
            # wit
            [
                # transport
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  20,   3,   2,  21,  12,   6,   1,   8,   8,   2,   3,   2,   0],  # I
                    [  25,   4,   2,  21,  15,   6,   1,   8,   8,   3,   3,   2,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # oorlog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  50,   8,   4,  21,  15,   6,   6,   8,   8,   3,   3,   2,   6],  # I
                    [  60,  10,   4,  21,  18,   6,   6,   8,   8,   3,   3,   2,   6],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [  80,  12,   5,  27,  21,   8,   8,   8,   9,   4,   2,   2,   8],  # IV
                ],
            ],
            # rood
            [
                # transport
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  25,   3,   2,  21,  12,   6,   4,   8,   8,   2,   3,   2,   2],  # I
                    [  30,   4,   3,  24,  15,   6,   4,   8,   8,   3,   3,   2,   3],  # II
                    [  40,   6,   3,  30,  18,   6,   5,  12,   8,   3,   3,   3,   4],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # oorlog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  65,  14,   4,  30,  21,  10,   8,   8,  10,   3,   3,   3,  10],  # I
                    [  75,  16,   5,  36,  24,  12,   8,  10,   9,   3,   3,   4,  10],  # II
                    [  85,  18,   5,  42,  24,  10,  10,  10,   9,   4,   2,   5,  12],  # III
                    [  95,  20,   6,  45,  27,  10,  12,  10,  10,   5,   2,   6,  12],  # IV
                ],
            ],
            # geel
            [
                # transport
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  15,   2,   3,  21,  12,   6,   1,   8,   8,   2,   3,   2,   0],  # I
                    [  20,   4,   3,  24,  15,   6,   1,   8,   8,   3,   3,   2,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # oorlog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  45,   8,   3,  24,  15,   6,   4,   6,   8,   2,   4,   2,   5],  # I
                    [  60,  10,   4,  27,  18,   8,   4,   8,   8,   3,   4,   3,   6],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   4,   0,   0],  # III
                    [  80,  14,   5,  33,  21,   6,   4,   8,   8,   4,   4,   4,   8],  # IV
                ],
            ],
        ],
         [  # T3
             # blauw
             [
                 # transport
                 [
                     # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                     [  30,   2,   2,  21,  12,   6,   1,   8,   8,   1,   3,   2,   0],  # I
                     [  35,   3,   2,  21,  15,   6,   1,   8,   8,   2,   3,   2,   0],  # II
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                 ],
                 # oorlog
                 [
                     # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                     [  60,   8,   3,  24,  15,   6,   6,   8,  10,   3,   3,   2,   6],  # I
                     [  70,  10,   4,  27,  18,   6,   7,   8,   8,   3,   3,   2,   6],  # II
                     [  80,  13,   4,  30,  21,   8,   8,  10,   8,   4,   3,   3,   8],  # III
                     [  85,  15,   5,  33,  21,   8,   9,  12,  10,   5,   2,   4,  10],  # IV
                 ],
             ],
             # paars
             [
                 # transport
                 [
                     # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                     [  25,   2,   2,  21,  12,   6,   1,   8,   8,   1,   3,   1,   0],  # I
                     [  35,   3,   2,  24,  15,   6,   1,   8,   8,   2,   3,   2,   0],  # II
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                 ],
                 # oorlog
                 [
                     # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                     [  50,   8,   3,  24,  15,   6,   6,   8,   8,   3,   3,   2,   6],  # I
                     [  65,  10,   4,  24,  18,   6,   6,   8,   8,   3,   3,   3,   6],  # II
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                     [  80,  12,   5,  30,  24,   6,   8,   8,   9,   4,   2,   4,   8],  # IV
                 ],
             ],
             # wit
             [
                 # transport
                 [
                     # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                     [  20,   3,   2,  21,  12,   6,   1,   8,   8,   2,   3,   2,   0],  # I
                     [  25,   4,   2,  21,  15,   6,   1,   8,   8,   3,   3,   2,   0],  # II
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                 ],
                 # oorlog
                 [
                     # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                     [  50,   8,   4,  21,  15,   6,   6,   8,   8,   3,   3,   2,   6],  # I
                     [  60,  10,   4,  21,  18,   6,   6,   8,   8,   3,   3,   2,   6],  # II
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                     [  80,  12,   5,  27,  21,   8,   8,   8,   9,   4,   2,   2,   8],  # IV
                 ],
             ],
             # rood
             [
                 # transport
                 [
                     # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                     [  25,   3,   2,  21,  12,   6,   4,   8,   8,   2,   3,   2,   2],  # I
                     [  30,   4,   3,  24,  15,   6,   4,   8,   8,   3,   3,   2,   3],  # II
                     [  40,   6,   3,  30,  18,   6,   5,  12,   8,   3,   3,   3,   4],  # III
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                 ],
                 # oorlog
                 [
                     # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                     [  65,  14,   4,  30,  21,  10,   8,   8,  10,   3,   3,   3,  10],  # I
                     [  75,  16,   5,  36,  24,  12,   8,  10,   9,   3,   3,   4,  10],  # II
                     [  85,  18,   5,  42,  24,  10,  10,  10,   9,   4,   2,   5,  12],  # III
                     [  95,  20,   6,  45,  27,  10,  12,  10,  10,   5,   2,   6,  12],  # IV
                 ],
             ],
             # geel
             [
                 # transport
                 [
                     # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                     [  15,   2,   3,  21,  12,   6,   1,   8,   8,   2,   3,   2,   0],  # I
                     [  20,   4,   3,  24,  15,   6,   1,   8,   8,   3,   3,   2,   0],  # II
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                 ],
                 # oorlog
                 [
                     # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                     [  45,   8,   3,  24,  15,   6,   4,   6,   8,   2,   4,   2,   5],  # I
                     [  60,  10,   4,  27,  18,   8,   4,   8,   8,   3,   4,   3,   6],  # II
                     [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   4,   0,   0],  # III
                     [  80,  14,   5,  33,  21,   6,   4,   8,   8,   4,   4,   4,   8],  # IV
                 ],
             ],
         ],

    ],
    [

            [  # T0
                # blauw
                [
                    # zwaard
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [  10,   3,   6,  15,  18,   5,   1,  10,  10,   2,   5,   2,   0,   0,   7,   4],  # I
                        [  15,   4,   7,  15,  18,   5,   1,  10,   8,   2,   5,   2,   0,   0,   9,   6],  # II
                        [  35,   5,   8,  18,  21,   6,   1,  12,   8,   2,   5,   3,   0,   0,  10,   8],  # III
                        [  45,   6,  10,  21,  24,   6,   1,  14,   8,   3,   5,   4,   0,   0,  12,  10],  # IV
                    ],
                    # speer
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [  15,   2,   5,  15,  18,   5,   1,   8,   8,   2,   4,   2,   0,   0,   5,   6],  #,  I
                        [  25,   3,   6,  18,  18,   5,   1,   8,   8,   2,   4,   2,   0,   0,   7,   8],  # , II
                        [  40,   3,   7,  18,  18,   5,   1,   8,   8,   2,   4,   3,   0,   0,   9,  10],  # I, II
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # , IV
                    ],
                    # paard
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [  10,   2,   5,  15,  18,  12,   1,  16,  12,   4,   4,   3,   0,   0,   8,   6],  # I
                        [  15,   4,   6,  15,  18,  14,   1,  16,  10,   4,   4,   3,   0,   0,  10,   8],  # II
                        [  30,   5,   8,  18,  18,  11,   1,  16,  10,   4,   4,   4,   0,   0,  12,  10],  # III
                        [  40,   6,  10,  21,  21,  11,   1,  16,  10,   4,   4,   5,   0,   0,  14,  12],  # IV
                    ],
                    # kanon
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # I
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # II
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                    ],
                    # boog
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [  10,   2,   6,  15,  18,   8,   3,  10,  12,   3,   4,   2,   5,   0,   0,   2],  # I
                        [  15,   3,   8,  15,  18,   8,   4,   8,  12,   3,   5,   3,   7,   0,   0,   4],  # II
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                    ],
                    # hamer
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # I
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # II
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                    ]
                ],
                # paars
                [
                    # zwaard
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [  25,   4,   3,  21,  18,   5,   2,  10,   8,   1,   4,   3,   2,   0,   5,   8],  # I
                        [  35,   5,   4,  21,  18,   6,   2,  10,   8,   2,   4,   4,   2,   1,   7,  10],  # II
                        [  45,   6,   4,  21,  21,   6,   3,  12,   8,   3,   4,   5,   2,   0,   8,  12],  # III
                        [  55,   7,   5,  21,  21,   6,   3,  15,   8,   3,   4,   6,   2,   0,  10,  14],  # IV
                    ],
                    # speer
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [  30,   2,   2,  18,  18,   5,   1,   8,   8,   1,   4,   1,   0,   0,   1,   6],  # I
                        [  40,   3,   3,  21,  18,   5,   1,  10,   8,   1,   4,   2,   0,   0,   2,   8],  # II
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                    ],
                    # paard
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [  10,   2,   4,  15,  18,  11,   1,  16,  12,   4,   5,   3,   0,   0,   4,   0],  # I
                        [  20,   4,   5,  15,  18,  11,   1,  15,  10,   3,   4,   3,   0,   0,   7,   0],  # II
                        [  40,   6,   7,  18,  21,  10,   1,  15,  10,   3,   4,   4,   0,   0,   9,   0],  # III
                        [  50,   8,   9,  21,  24,  10,   1,  15,  10,   4,   4,   5,   0,   0,  11,   0],  # IV
                    ],
                    # kanon
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [   5,   3,   4,  15,  18,   4,   5,   6,   8,   1,   4,   2,   7,   0,   0,  30],  # I
                        [  10,   6,   5,  15,  18,   3,   6,   6,   8,   2,   4,   3,   4,   0,   0,  30],  # II
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                    ],
                    # boog
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [   5,   3,   3,  15,  12,   7,   3,  10,  10,   3,   4,   1,   4,   0,   0,   2],  # I
                        [  10,   5,   3,  15,  18,   5,   4,   8,   8,   1,   4,   3,   6,   0,   0,   4],  # II
                        [  25,   6,   4,  18,  21,   5,   5,   8,   8,   2,   4,   3,   6,   0,   0,   6],  # III
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                    ],
                    # hamer
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [   5,   1,   1,  12,  12,  12,   1,  10,   8,   3,   4,   1,   0,   1,   1,   1],  # I
                        [   5,   1,   1,  12,  15,  14,   1,  10,   8,   3,   4,   1,   0,   1,   2,   2],  # II
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                    ]
                ],
                # wit
                [
                    # zwaard
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [  20,   4,   3,  15,  12,   5,   1,   8,   8,   1,   4,   0,   0,   0,   0,   0],  # I
                        [  25,   6,   4,  15,  15,   5,   1,   8,   8,   2,   4,   1,   0,   0,   0,   0],  # II
                        [  40,   8,   6,  18,  18,   6,   1,  12,   8,   2,   4,   3,   0,   0,   0,   0],  # III
                        [  50,   9,   6,  21,  21,   6,   1,  12,   8,   2,   4,   3,   0,   0,   0,   0],  # IV
                    ],
                    # speer
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [  35,   3,   3,  15,  15,   4,   1,   6,   8,   1,   3,   1,   0,   0,   0,   0],  # I
                        [  45,   5,   4,  18,  18,   5,   1,   8,   8,   2,   3,   2,   0,   0,   0,   0],  # II
                        [  55,   6,   5,  21,  21,   6,   1,   8,   8,   3,   3,   3,   0,   0,   0,   0],  # III
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                    ],
                    # paard
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [  10,   4,   4,  15,  12,  12,   4,  16,  12,   4,   4,   2,   5,   0,   0,   0],  # I
                        [  20,   6,   4,  15,  15,  12,   1,  15,  10,   4,   4,   2,   0,   0,   0,   0],  # II
                        [  55,   6,  14,  18,  18,   7,   1,  15,  10,   3,   4,   0,   0,   0,   0,   0],  # III
                        [  70,   8,  16,  21,  18,   7,   1,  15,  10,   3,   4,   1,   0,   0,   0,   0],  # IV
                    ],
                    # kanon
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [  10,   4,   4,  15,  12,   3,   4,   6,   8,   1,   3,   0,   5,   0,   0,   0],  # I
                        [  15,   5,   4,  15,  15,   3,   5,   6,   8,   2,   3,   1,   6,   0,   0,   0],  # II
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                    ],
                    # boog
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [  10,   3,   3,  15,  12,   6,   3,   10,  9,   2,   4,   1,   4,   0,   0,   0],  # I
                        [  20,   7,   4,  21,  18,   6,   4,   8,   8,   2,   3,   2,   7,   0,   0,   0],  # II
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                    ],
                    # hamer
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [   5,   1,   1,  12,  12,  12,   1,  10,   8,   3,   4,   0,   0,   0,   0,   0],  # I
                        [  10,   2,   1,  12,  15,  14,   1,  10,   8,   3,   4,   0,   0,   0,   0,   0],  # II
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                    ]
                ],
                # rood
                [
                    # zwaard
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [  20,   4,   4,  15,  12,   5,   1,   8,   8,   1,   4,   1,   0,   0,   0,   0],  # I
                        [  25,   6,   5,  15,  15,   5,   1,   8,   8,   2,   4,   1,   0,   0,   0,   0],  # II
                        [  35,   7,   6,  18,  18,   6,   1,  10,   8,   2,   4,   2,   0,   0,   0,   0],  # III
                        [  50,   8,   7,  21,  21,   6,   1,  10,   8,   3,   4,   3,   0,   0,   0,   0],  # IV
                    ],
                    # speer
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [  40,   3,   5,  18,  21,   4,   1,   6,   8,   1,   4,   4,   0,   0,   0,   0],  # I
                        [  60,   5,   6,  21,  24,   4,   1,   8,   8,   2,   4,   6,   0,   0,   0,   0],  # II
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                    ],
                    # paard
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [   5,   7,   6,  12,  15,  12,   5,  16,  12,   4,   4,   2,   3,   0,   0,   0],  # I
                        [  10,   6,   8,  12,  18,  12,   1,  15,  10,   4,   4,   2,   0,   0,   0,   0],  # II
                        [  45,   8,   6,  18,  18,  10,   1,  15,  10,   5,   4,   3,   0,   0,   0,   0],  # III
                        [  55,   9,   7,  21,  21,  10,   1,  15,  10,   4,   4,   4,   0,   0,   0,   0],  # IV
                    ],
                    # kanon
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # I
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # II
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                    ],
                    # boog
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [  10,   4,   2,  15,  12,   6,   3,  10,   9,   2,   4,   2,   3,   0,   0,   0],  # I
                        [  15,   5,   2,  15,  15,   5,   5,   8,   8,   2,   4,   3,   5,   0,   0,   0],  # II
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                    ],
                    # hamer
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # I
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # II
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                    ]
                ],
                # geel
                [
                    # zwaard
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [  15,   4,   2,  15,  12,   4,   1,   8,   8,   1,   4,   0,   0,   0,   0,   0],  # I
                        [  25,   6,   3,  15,  15,   4,   1,   8,   8,   2,   4,   1,   0,   0,   0,   0],  # II
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                    ],
                    # speer
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [  35,   2,   3,  18,  15,   4,   1,   6,   8,   2,   4,   2,   0,   0,   0,   0],  # I
                        [  50,   3,   3,  21,  18,   5,   1,   8,   8,   2,   4,   4,   0,   0,   0,   0],  # II
                        [  60,   4,   4,  21,  21,   6,   1,   8,   8,   3,   4,   5,   0,   0,   0,   0],  # III
                        [  70,   4,   5,  24,  24,   6,   1,  10,   8,   3,   4,   7,   0,   0,   0,   0],  # IV
                    ],
                    # paard
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [   5,   5,   5,   9,  12,  12,   3,  16,  10,   4,   4,   2,   2,   0,   0,   0],  # I
                        [   5,   6,   6,  12,  15,  12,   3,  15,  10,   4,   4,   2,   4,   0,   0,   0],  # II
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                        [  20,   9,   7,  21,  21,  10,   4,  15,   8,   4,   4,   4,   8,   0,   0,   0],  # IV
                    ],
                    # kanon
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [   5,   5,   4,  15,  12,   4,   4,   6,   8,   1,   3,   0,   5,   0,   0,   0],  # I
                        [  10,   7,   5,  15,  15,   3,   5,   6,   8,   2,   3,   1,   6,   0,   0,   0],  # II
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                    ],
                    # boog
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [  10,   4,   3,  15,  12,   6,   3,  10,   9,   2,   4,   1,   4,   0,   0,   0],  # I
                        [  20,   6,   3,  15,  15,   5,   5,   8,   8,   1,   4,   2,   6,   0,   0,   0],  # II
                        [  30,   8,   4,  15,  15,   6,   6,   8,   8,   2,   4,   3,   8,   0,   0,   0],  # III
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                    ],
                    # hamer
                    [
                        # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                        [   5,   1,   1,  12,  12,  12,   1,  10,   8,   3,   4,   0,   0,   0,   0,   0],  # I
                        [  10,   2,   1,  12,  15,  14,   1,  10,   8,   3,   4,   0,   0,   0,   0,   0],  # II
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                        [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                    ]
                ],
            ],

            [#T1
            #blauw
            [
                #zwaard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  20,   6,   4,  21,  18,   4,   1,   8,   8,   1,   4,   0,   0,   0,   0,   0],#I
                    [  30,   9,   5,  21,  21,   5,   1,   8,   8,   2,   4,   1,   0,   0,   0,   0],#II
                    [  40,  12,   7,  27,  27,   6,   1,  12,   8,   2,   4,   2,   0,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ],
                #speer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  35,   4,   3,  21,  21,   4,   1,   6,   8,   1,   4,   1,   0,   0,   0,   0],#I
                    [  40,   7,   4,  27,  27,   5,   1,   8,   8,   1,   4,   2,   0,   0,   0,   0],#II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ],
                #paard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  25,   6,   5,  21,  18,  12,   1,  16,  12,   4,   4,   2,   0,   0,   0,   0],#I
                    [  35,   9,   6,  21,  21,  12,   1,  15,  10,   4,   4,   2,   0,   0,   0,   0],#II
                    [  50,  12,   8,  27,  27,  10,   1,  15,  10,   5,   4,   3,   0,   0,   0,   0],#III
                    [  65,  15,   9,  33,  33,  10,   1,  15,  10,   4,   4,   4,   0,   0,   0,   0],#IV
                ],
                #kanon
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  10,   7,   6,  21,  18,   3,   7,   6,   8,   1,   4,   0,   6,   0,   0,   0],#I
                    [  15,  10,   6,  21,  21,   3,   9,   6,   8,   2,   4,   1,   6,   0,   0,   0],#II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ],
                #boog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  10,   4,   3,  21,  18,   6,   3,  10,   9,   2,   4,   1,   4,   0,   0,   0],#I
                    [  20,   7,   4,  21,  21,   5,   5,   8,   8,   1,   4,   1,   8,   0,   0,   0],#II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ],
                # hamer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [   5,   2,   2,  18,  18,  12,   1,  10,   8,   3,   4,   0,   0,   0,   0,   0],# I
                    [  10,   3,   2,  18,  21,  14,   1,  10,   8,   3,   4,   0,   0,   0,   0,   0],# II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],# III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],# IV
                ]
            ],
            #paars
            [
                #zwaard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  20,   9,   4,  21,  21,   5,   1,   8,   8,   1,   4,   1,   0,   0,   0,   0],#I
                    [  35,  10,   6,  21,  27,   5,   2,  10,   8,   2,   4,   2,   1,   0,   0,   0],#II
                    [  45,  12,   8,  27,  27,   6,   3,  12,   9,   2,   4,   3,   2,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ],
                #speer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#I
                    [  35,   6,   4,  21,  18,   4,   1,   8,   8,   1,   4,   1,   0,   0,   0,   0],#II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ],
                #paard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  15,   4,   3,  18,  18,  10,   1,  12,  10,   4,   4,   1,   0,   0,   0,   0],#I
                    [  25,   7,   5,  21,  21,  10,   1,  10,   8,   3,   4,   2,   0,   0,   0,   0],#II
                    [  35,  10,   8,  27,  27,   8,   1,  12,   8,   4,   4,   3,   0,   0,   0,   0],#III
                    [  45,  13,   9,  33,  33,   8,   1,  14,   8,   4,   4,   3,   0,   0,   0,   0],#IV
                ],
                #kanon
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  15,   9,   4,  21,  18,   5,   8,   6,   8,   2,   4,   0,   8,   0,   0,   0],#I
                    [  20,  10,   5,  21,  18,   5,  10,   6,   8,   2,   4,   1,  10,   0,   0,   0],#II
                    [  25,   6,  12,  27,  21,   6,   6,   8,   9,   2,   4,   2,   5,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ],
                #boog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [   4,   4,   2,  21,  18,   6,   3,  10,   9,   2,   4,   0,   4,   0,   0,   0],#I
                    [   8,   7,   3,  21,  21,   5,   5,   8,   8,   1,   4,   1,   6,   0,   0,   0],#II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ],
                # hamer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  10,   3,   1,  21,  18,   8,   1,  12,   8,   2,   4,   0,   0,   0,   0,   0],#I
                    [  15,   4,   2,  21,  18,  10,   1,  14,   8,   3,   4,   0,   0,   0,   0,   0],#II
                    [  20,   6,   3,  27,  21,  12,   1,  16,   8,   3,   4,   0,   0,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ]
            ],
            #wit
            [
                #zwaard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  30,   5,   3,  27,  21,   5,   1,   8,   8,   1,   4,   1,   0,   0,   0,   0],#I
                    [  40,   7,   5,  33,  27,   6,   1,  10,   8,   2,   4,   2,   0,   0,   0,   0],#II
                    [  50,  10,   7,  33,  33,   6,   1,  12,   8,   2,   4,   3,   0,   0,   0,   0],#III
                    [  60,  12,   9,  36,  36,   8,   1,  12,   8,   2,   4,   4,   0,   0,   0,   0],#IV
                ],
                #speer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  20,   4,   2,  21,  18,   4,   1,   6,   8,   1,   4,   0,   0,   0,   0,   0],#I
                    [  30,   6,   3,  21,  21,   4,   1,   8,   8,   1,   4,   1,   0,   0,   0,   0],#II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ],
                #paard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  15,   4,   3,  18,  18,  10,   1,  12,  10,   4,   4,   1,   0,   0,   0,   0],#I
                    [  20,   6,   4,  21,  21,  10,   1,  10,   8,   3,   4,   2,   0,   0,   0,   0],#II
                    [  30,   9,   5,  27,  21,   8,   1,  12,   8,   3,   4,   2,   0,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   8,   0,   0,   0,   0,   0,   0,   0],#IV
                ],
                #kanon
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  10,   7,   3,  21,  15,   3,   7,   6,   8,   2,   4,   0,   6,   0,   0,   0],#I
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ],
                #boog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  10,   4,   2,  18,  18,   8,   4,   8,   9,   2,   4,   0,   6,   0,   0,   0],#I
                    [  20,   7,   3,  21,  21,   4,   4,   8,   8,   1,   4,   1,   8,   0,   0,   0],#II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ],
                # hamer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [   5,   1,   1,  18,  18,   8,   1,  10,   8,  2,    4,   0,   0,   0,   0,   0],#I
                    [  10,   3,   1,  18,  21,   8,   1,  10,   8,  3,    4,   0,   0,   0,   0,   0],#II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,    0,   0,   0,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,    0,   0,   0,   0,   0,   0],#IV
                ]
            ],
            #rood
            [
                #zwaard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  20,   6,   3,  21,  18,   4,   1,   6,   8,   1,   4,   0,   0,   0,   0,   0],#I
                    [  25,  10,   4,  21,  21,   5,   1,   8,   8,   1,   4,   1,   0,   0,   0,   0],#II
                    [  35,  12,   6,  27,  27,   6,   1,  10,   8,   2,   4,   1,   0,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ],
                #speer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  20,   4,   2,  21,  18,   4,   1,   6,   8,   1,   4,   1,   0,   0,   0,   0],#I
                    [  25,   7,   3,  27,  27,   4,   1,   8,   8,   1,   4,   2,   0,   0,   0,   0],#II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ],
                #paard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  15,   4,   2,  18,  18,  10,   1,  12,  10,   4,   4,   1,   0,   0,   0,   0],#I
                    [  20,   7,   4,  21,  21,  10,   1,  10,   8,   3,   4,   2,   0,   0,   0,   0],#II
                    [  30,   9,   5,  27,  27,   8,   1,  10,   8,   3,   4,   3,   0,   0,   0,   0],#III
                    [  40,  12,   7,  27,  27,   8,   1,  12,   8,   3,   4,   3,   0,   0,   0,   0],#IV
                ],
                #kanon
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  10,   9,   4,  21,  15,   3,   6,   6,   8,   2,   4,   0,   5,   0,   0,   0],#I
                    [  20,  12,   5,  21,  18,   3,   8,   6,   8,   2,   4,   1,   6,   0,   0,   0],#II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ],
                #boog
                [
                    #  ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  15,   6,   5,  21,  18,   7,   4,  10,  10,   3,   4,    1,   8,   0,   0,   0],#I
                    [  25,   9,   7,  21,  21,   5,   6,   8,   9,   2,   4,    2,   8,   0,   0,   0],#II
                    [  35,  12,   9,  27,  27,   6,   9,  10,  10,   3,   4,    3,  10,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,    0,   0,   0,   0,   0],#IV
                ],
                # hamer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [   5,   1,   1,  18,  15,   8,   1,  10,   8,   3,   4,   0,   0,   0,   0,   0],#I
                    [  10,   3,   2,  18,  15,  10,   1,  10,   8,   3,   4,   0,   0,   0,   0,   0],#II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ]
            ],
            #geel
            [
                #zwaard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  15,   4,   2,  18,  18,   4,   1,   6,   8,   1,   4,   0,   0,   0,   0,   0],#I
                    [  25,   7,   3,  21,  21,   4,   1,   8,   8,   1,   4,   1,   0,   0,   0,   0],#II
                    [  35,   9,   5,  27,  27,   6,   1,  10,   8,   2,   4,   2,   0,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ],
                #speer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  30,   6,   4,  27,  27,   5,   1,   8,   8,   2,   4,   2,   0,   0,   0,   0],#I
                    [  45,   9,   6,  33,  33,   6,   1,  10,   8,   2,   4,   3,   0,   0,   0,   0],#II
                    [  60,  10,   8,  36,  36,   6,   1,  12,   8,   3,   4,   4,   0,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ],
                #paard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  15,   4,   3,  18,  18,  12,   1,  10,  10,   3,   4,   2,   0,   0,   0,   0],#I
                    [  25,   7,   4,  21,  21,  10,   1,   8,   8,   3,   4,   2,   0,   0,   0,   0],#II
                    [  30,  12,   5,  27,  27,   8,   3,  12,   8,   4,   4,   3,   6,   0,   0,   0],#III
                    [  40,  12,   7,  33,  33,   8,   1,  10,   8,   3,   4,   3,   0,   0,   0,   0],#IV
                ],
                #kanon
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#I
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ],
                #boog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [  10,   4,   2,  21,  18,   6,   3,   6,   9,   3,   4,   1,   8,   0,   0,   0],#I
                    [  20,   7,   3,  21,  21,   5,   5,   8,   8,   2,   4,   1,   6,   0,   0,   0],#II
                    [  30,  10,   4,  27,  27,   6,   6,   9,   8,   2,   4,   2,   6,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ],
                # hamer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  zba  mve  mun  bou  duw  dba
                    [   0,   2,   1,  18,  18,  10,   1,  10,   8,   3,   4,   0,   0,   0,   0,   0],#I
                    [   5,   4,   2,  21,  21,  10,   1,  10,   8,   3,   4,   0,   0,   0,   0,   0],#II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],#IV
                ]
            ],
            ],

            [#T2
            # blauw
            [
                # zwaard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  30,   4,   6,  30,  24,    5,   4,   8,   8,   1,   4,   1,   5],  # I
                    [  40,   6,   8,  30,  30,    5,   5,   8,   9,   2,   4,   1,   5],  # II
                    [  50,   8,   8,  36,  36,    6,   5,  12,   9,   2,   4,   2,   6],  # III
                    [   0,   0,   0,   0,   0,    0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # speer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  50,   2,   6,  36,  36,   5,   1,   6,   8,  1,   4,   2,   0],  # I
                    [  60,   4,   6,  36,  36,   5,   1,   8,   8,  2,   4,   2,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0],  # IV
                ],
                # paard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  40,   5,  10,  30,  24,  12,   3,  16,  12,   4,   5,   2,   4],  # I
                    [  55,   6,  10,  30,  30,  12,   5,  15,  10,   4,   4,   3,   5],  # II
                    [  65,   8,  10,  36,  36,  10,   5,  15,  10,   5,   4,   3,   6],  # III
                    [  75,  10,  12,  42,  42,  10,   1,  15,  10,   4,   5,   4,   0],  # IV
                ],
                # kanon
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  15,   5,   8,  30,  24,   4,   8,   6,   8,  1,   3,   0,   8],  # I
                    [  25,   8,   8,  30,  30,   4,  10,   6,   8,  2,   3,   1,   8],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0],  # IV
                ],
                # boog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  25,   4,   6,  30,  24,   6,   6,   8,  10,  2,   4,   0,   7],  # I
                    [  30,   6,   6,  30,  30,   5,   7,   8,  11,  2,   5,   1,   7],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0],  # IV
                ],
                # hamer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  10,   1,   2,  24,  24,  12,   1,  10,   8,   3,   4,   0,   0],  # I
                    [  15,   2,   2,  24,  30,  14,   1,  10,   8,   3,   4,   0,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ]
            ],
            # paars
            [
                # zwaard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  40,   5,   6,  30,  30,   5,   4,   8,   8,  1,   4,   1,   5],  # I
                    [  45,   6,   6,  30,  36,   5,   4,  10,   9,  2,   4,   1,   5],  # II
                    [  50,   7,   8,  36,  36,   6,   5,  12,   9,  2,   4,   2,   6],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0],  # IV
                ],
                # speer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  50,   2,   1,  42,  42,   5,   1,   8,   8,   1,   3,   1,   0],  # I
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # paard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  20,   3,   3,  24,  24,  10,   1,  12,  10,   4,   4,   1,   0],  # I
                    [  30,   4,   4,  30,  30,  10,   3,  10,   8,   3,   3,   2,   2],  # II
                    [  45,   6,   4,  36,  36,   8,   4,  12,   8,   4,   3,   2,   3],  # III
                    [  60,   7,   5,  42,  42,   8,   1,  14,   8,   4,   3,   3,   0],  # IV
                ],
                # kanon
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  20,   6,   4,  30,  24,   5,  10,   6,   9,   2,   4,   1,   7],  # I
                    [  30,   7,   4,  30,  24,   6,  12,   6,  10,   2,   4,   2,   7],  # II
                    [  40,   9,   4,  36,  30,   7,  14,   8,  12,   2,   4,   3,   8],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # boog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  30,   4,   2,  30,  24,   6,   6,  10,   9,   3,   4,   1,   6],  # I
                    [  35,   5,   2,  30,  30,   5,   8,   8,  10,   2,   5,   2,   7],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # hamer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  10,   2,   2,  30,  18,   8,   1,  12,   8,   2,   4,   0,   0],  # I
                    [  15,   3,   2,  30,  24,   10,  1,  14,   8,   3,   4,   0,   0],  # II
                    [   9,   4,   3,  36,  30,   12,  1,  16,   8,   3,   4,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ]
            ],
            # wit
            [
                # zwaard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  40,   6,   3,  36,  30,   5,   5,   8,   9,   2,   4,   2,   8],  # I
                    [  50,   7,   4,  42,  36,   6,   5,  10,   9,   2,   4,   2,   8],  # II
                    [  60,   8,   4,  42,  42,   6,   6,  12,  10,   2,   5,   3,   9],  # III
                    [  70,   9,   5,  48,  48,   8,   6,  12,  10,   2,   5,   4,  10],  # IV
                ],
                # speer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  45,   2,   2,  30,  24,   4,   1,   6,   8,   1,   3,   1,   0],  # I
                    [  50,   3,   2,  30,  30,   5,   1,   8,   8,   2,   4,   1,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # paard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  30,   3,   3,  24,  24,  10,   1,  12,  10,   4 ,  4,   1,   0],  # I
                    [  35,   4,   3,  30,  30,  10,   1,  10,   9,   3 ,  4,   1,   0],  # II
                    [  40,   6,   4,  36,  30,   8,   4,  12,   9,   3 ,  4,   2,   3],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0 ,  0,   0,   0],  # IV
                ],
                # kanon
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  10,   5,   6,  30,  18,   3,   9,   6,   9,   2,   3,   1,   6],  # I
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # boog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  20,   3,   2,  24,  24,   8,   6,   8,   9,   2,   4,   0,   6],  # I
                    [  30,   5,   2,  30,  30,   5,   6,   8,  10,   2,   4,   1,   7],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # hamer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [   5,   1,   1,  24,  24,   8,   1,  10,   8,   2,   4,   0,   0],  # I
                    [  10,   2,   1,  24,  30,   8,   1,  10,   8,   3,   4,   0,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ]
            ],
            # rood
            [
                # zwaard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  30,   5,   2,  30,  24,   5,   4,   6,   8,   1,   4,   2,   6],  # I
                    [  40,   6,   3,  30,  30,   5,   4,   8,   9,   2,   4,   2,   7],  # II
                    [  45,   7,   3,  36,  36,   6,   5,  10,   9,   2,   4,   3,   7],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # speer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  40,   2,   3,  30,  24,   4,   1,   6,   8,   1,   3,   1,   0],  # I
                    [  50,   3,   3,  36,  36,   5,   1,   8,   8,   2,   4,   2,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # paard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  25,   3,   3,  24,  24,  10,   1,  12,  15,   4,   4,   2,   0],  # I
                    [  30,   5,   3,  30,  30,  10,   4,  10,   9,   3,   4,   2,   1],  # II
                    [  40,   6,   4,  36,  36,   8,   5,  10,   9,   3,   4,   3,   5],  # III
                    [  50,   8,   5,  36,  36,   8,   1,  12,  10,   3,   5,   3,   0],  # IV
                ],
                # kanon
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  10,   6,   4,  30,  18,   4,   8,   6,   9,   2,   4,   1,   6],  # I
                    [  20,   8,   4,  30,  24,   4,  10,   6,   9,   2,   4,   2,   6],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # boog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  30,   4,   3,  30,  24,   7,   8,  10,  10,   3,   4,   2,   7],  # I
                    [  40,   6,   3,  30,  30,   5,  10,   8,  11,   2,   5,   2,   8],  # II
                    [  50,   8,   4,  36,  36,   6,  13,  10,  12,   3,   6,   3,   9],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # hamer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [   5,   1,   1,  24,  18,   8,   1,  10,   8,   3,   4,   0,   0],  # I
                    [  10,   2,   1,  24,  18,  10,   1,  10,   8,   3,   4,   0,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ]
            ],
            # geel
            [
                # zwaard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  20,   3,   2,  24,  24,   5,   4,    6,   8,   1,   3,   1,   4],  # I
                    [  30,   4,   2,  30,  30,   5,   4,    8,   8,   2,   4,   1,   4],  # II
                    [  40,   5,   3,  36,  36,   6,   5,   10,   8,   2,   4,   2,   5],  # III
                    [   0,   0,   0,   0,   0,   0,   0,    0,   0,   0,   0,   0,   0],  # IV
                ],
                # speer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  45,   4,   3,  36,  42,   5,   4,   8,   8,   2,   4,   2,   6],  # I
                    [  55,   6,   4,  42,  48,   6,   4,  10,   8,   2,   4,   2,   7],  # II
                    [  65,   8,   5,  48,  54,   6,   4,  12,   8,   3,   5,   3,   8],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # paard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  20,   3,   3,  24,  24,  12,   5,  10,  10,   3,   4,   1,   2],  # I
                    [  30,   5,   4,  30,  30,  10,   4,   8,   8,   3,   4,   2,   3],  # II
                    [  40,   8,   4,  36,  36,   8,   4,  12,   8,   4,   4,   2,   4],  # III
                    [  50,   8,   5,  42,  42,   8,   1,  10,   8,   3,   5,   3,   1],  # IV
                ],
                # kanon
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  20,   5,   5,  24,  21,   6,   8,   6,   8,   2,   3,   1,   7],  # I
                    [  30,   7,   6,  27,  24,   6,  10,   6,   8,   2,   3,   2,   9],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # boog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  20,   4,   2,  30,  24,   6,   5,   6,   9,   3,   4,   1,   6],  # I
                    [  25,   6,   2,  30,  30,   5,   7,   8,  10,   2,   5,   2,   7],  # II
                    [  30,   8,   2,  36,  36,   6,  10,   9,  11,   2,   5,   3,   8],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # hamer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  10,   1,   1,  24,  24,  10,   1,  10,   8,   3,   4,   0,   0],  # I
                    [  15,   3,   1,  30,  30,  10,   1,  10,   8,   3,   4,   0,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ]
            ],
        ],
        [  # T3
            # blauw
            [
                # zwaard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  20,   6,   6,  30,  24,   6,   5,   9,  11,   2,   3,   3,   6],  # I
                    [  25,   8,   7,  36,  27,   6,   6,  10,  11,   2,   3,   3,   6],  # II
                    [  30,  10,   8,  42,  30,   7,   6,  12,  11,   2,   4,   4,   7],  # III
                    [  40,  12,   9,  48,  33,   8,   7,  14,  11,   3,   4,   5,   8],  # IV
                ],
                # speer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  30,   4,   3,  36,  30,   5,   5,   6,  12,   2,   3,   4,   5],  # I
                    [  40,   5,   4,  39,  33,   5,   5,   8,  12,   2,   3,   5,   6],  # II
                    [  50,   6,   5,  42,  36,   6,   6,  10,  12,   3,   3,   6,   7],  # III
                    [  60,   7,   6,  48,  39,   6,   6,  12,  12,   3,   3,   7,   8],  # IV
                ],
                # paard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  45,   8,   6,  39,  12,  14,   5,  16,  12,   4,   2,   4,   7],  # I
                    [  65,  10,   8,  45,  15,  12,   8,  15,  10,   4,   2,   5,   6],  # II
                    [  80,  12,  10,  51,  18,   8,  11,  15,  10,   4,   2,   6,   6],  # III
                    [  85,  14,  12,  54,  21,   8,  12,  15,  10,   4,   2,   7,   6],  # IV
                ],
                # kanon
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  10,   6,   7,  30,  24,   5,  12,   8,  10,   2,   3,   3,   6],  # I
                    [  15,   8,   8,  33,  27,   5,  13,   8,  10,   2,   3,   3,   8],  # II
                    [  20,  10,   9,  36,  30,   6,  15,  10,  10,   3,   3,   4,  10],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # boog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  20,   6,   4,  24,  21,   8,   7,   8,  14,   3,   4,   2,   7],  # I
                    [  30,   7,   5,  27,  24,   8,   8,   8,  16,   3,   5,   3,   9],  # II
                    [  40,   8,   6,  30,  27,   8,  10,  10,  18,   3,   6,   4,   9],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # hamer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [   5,   1,   1,  12,  12,  12,   1,  10,   8,   3,   4,   0,   0],  # I
                    [  10,   1,   1,  12,  15,  14,   1,  10,   8,   3,   4,   0,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ]
            ],
            # paars
            [
                # zwaard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  15,   3,   1,  18,  18,   5,   2,   9,   8,   1,   4,   2,   2],  # I
                    [  25,   5,   2,  18,  18,   6,   3,  10,   8,   2,   4,   4,   2],  # II
                    [  30,   7,   2,  18,  21,   6,   4,  12,   8,   3,   4,   5,   3],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # speer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  20,   2,   2,  18,  18,   4,   1,   6,   8,   1,   4,   1,   0],  # I
                    [  30,   3,   3,  18,  18,   5,   1,   8,   8,   1,   4,   2,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # paard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  10,   2,   2,  15,  15,  11,   1,  16,  12,   4,   5,   3,   0],  # I
                    [  15,   4,   3,  15,  18,  11,   1,  15,  10,   3,   4,   3,   0],  # II
                    [  20,   6,   3,  18,  21,  10,   1,  15,  10,   3,   4,   4,   0],  # III
                    [  30,   8,   4,  21,  24,  10,   1,  15,  10,   4,   4,   5,   0],  # IV
                ],
                # kanon
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [   5,   4,   2,  15,  12,   3,   5,   6,   8,   1,   4,   2,   5],  # I
                    [  10,   6,   3,  15,  15,   3,   7,   6,   8,   2,   4,   3,   6],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # boog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [   5,   2,   2,  15,  12,   6,   2,  10,   9,   2,   4,   2,   4],  # I
                    [  10,   4,   2,  15,  15,   5,   4,   8,   8,   1,   4,   3,   8],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # hamer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [   5,   1,   1,  12,  12,  12,   1,  10,   8,   3,   4,   1,   0],  # I
                    [   5,   1,   1,  12,  15,  14,   1,  10,   8,   3,   4,   1,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ]
            ],
            # wit
            [
                # zwaard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  20,   4,   2,  15,  12,   4,   1,   8,   8,   1,   4,   0,   0],  # I
                    [  25,   6,   3,  15,  15,   5,   1,   8,   8,   2,   4,   1,   0],  # II
                    [  30,   8,   3,  18,  18,   6,   1,  12,   8,   2,   4,   2,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # speer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  20,   3,   3,  15,  15,   4,   1,   6,   8,   1,   4,   1,   0],  # I
                    [  30,   5,   3,  18,  18,   5,   1,   8,   8,   1,   4,   2,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # paard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  20,   4,   4,  15,  12,  12,   1,  16,  12,   4,   4,   2,   0],  # I
                    [  30,   6,   4,  15,  15,  12,   1,  15,  10,   4,   4,   2,   0],  # II
                    [  35,   8,   4,  18,  18,  10,   1,  15,  10,   5,   4,   3,   0],  # III
                    [  40,  10,   5,  21,  21,  10,   1,  15,  10,   4,   4,   4,   0],  # IV
                ],
                # kanon
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  10,   5,   4,  15,  12,   3,   7,   6,   8,   1,   4,   0,   6],  # I
                    [  15,   7,   4,  15,  15,   3,   9,   6,   8,   2,   4,   1,   6],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # boog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  10,   3,   2,  15,  12,   6,   3,  10,   9,   2,   4,   1,   4],  # I
                    [  15,   5,   2,  15,  15,   5,   5,   8,   8,   1,   4,   1,   8],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # hamer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [   5,   1,   1,  12,  12,  12,   1,  10,   8,   3,   4,   0,   0],  # I
                    [  10,   2,   1,  12,  15,  14,   1,  10,   8,   3,   4,   0,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ]
            ],
            # rood
            [
                # zwaard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  20,   4,   2,  15,  12,   4,   1,   8,   8,   1,   4,   0,   0],  # I
                    [  25,   6,   3,  15,  15,   5,   1,   8,   8,   2,   4,   1,   0],  # II
                    [  30,   8,   3,  18,  18,   6,   1,  12,   8,   2,   4,   2,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # speer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  25,   3,   3,  15,  15,   4,   1,   6,   8,   1,   4,   1,   0],  # I
                    [  30,   5,   3,  18,  18,   5,   1,   8,   8,   1,   4,   2,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # paard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  15,   4,   4,  15,  12,  12,   1,  16,  12,   4,   4,   2,   0],  # I
                    [  25,   6,   4,  15,  15,  12,   1,  15,  10,   4,   4,   2,   0],  # II
                    [  30,   8,   4,  18,  18,  10,   1,  15,  10,   5,   4,   3,   0],  # III
                    [  40,  10,   5,  21,  21,  10,   1,  15,  10,   4,   4,   4,   0],  # IV
                ],
                # kanon
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [   5,   5,   4,  15,  12,   3,   7,   6,   8,   1,   4,   0,   6],  # I
                    [  10,   7,   4,  15,  15,   3,   9,   6,   8,   2,   4,   1,   6],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # boog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [   5,   3,   2,  15,  12,   6,   3,  10,   9,   2,   4,   1,   4],  # I
                    [  10,   5,   2,  15,  15,   5,   5,   8,   8,   1,   4,   1,   8],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # hamer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [   5,   1,   1,  12,  12,  12,   1,  10,   8,   3,   4,   0,   0],  # I
                    [  10,   2,   1,  12,  15,  14,   1,  10,   8,   3,   4,   0,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ]
            ],
            # geel
            [
                # zwaard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  15,   4,   2,  15,  12,   4,   1,   8,   8,   1,   4,   0,   0],  # I
                    [  20,   6,   3,  15,  15,   5,   1,   8,   8,   2,   4,   1,   0],  # II
                    [  25,   8,   3,  18,  18,   6,   1,  12,   8,   2,   4,   2,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # speer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  20,   3,   3,  15,  15,   4,   1,   6,   8,   1,   4,   1,   0],  # I
                    [  30,   5,   3,  18,  18,   5,   1,   8,   8,   1,   4,   2,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # paard
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [  10,   4,   4,  15,  12,  12,   1,  16,  12,   4,   4,   2,   0],  # I
                    [  20,   6,   4,  15,  15,  12,   1,  15,  10,   4,   4,   2,   0],  # II
                    [  25,   8,   4,  18,  18,  10,   1,  15,  10,   5,   4,   3,   0],  # III
                    [  30,  10,   5,  21,  21,  10,   1,  15,  10,   4,   4,   4,   0],  # IV
                ],
                # kanon
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [   5,   5,   4,  15,  12,   3,   7,   6,   8,   1,   4,   0,   6],  # I
                    [  10,   7,   4,  15,  15,   3,   9,   6,   8,   2,   4,   1,   6],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # boog
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [   5,   3,   2,  15,  12,   6,   3,   10,   9,   2,   4,   1,   4],  # I
                    [  10,   5,   2,  15,  15,   5,   5,   8,   8,   1,   4,   1,   8],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ],
                # hamer
                [
                    # ver  aan  anm  gez  mor  bew  ber  uit  zie  ter  baa  mve  mun
                    [   5,   1,   1,  12,  12,  12,   1,  10,   8,   3,   4,   0,   0],  # I
                    [  10,   2,   1,  12,  15,  14,   1,  10,   8,   3,   4,   0,   0],  # II
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # III
                    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # IV
                ]
            ],
        ]

    ]
    ]


    def __init__(self, kleur, welk_type, nivo, x, y, T, Boot):
        self.kleur = kleur
        self.welk_type = welk_type
        self.nivo = nivo
        self.x = x
        self.y = y
        if Boot == False:
            self.boot = 1
        else:
            self.boot = 0
        eenheid = self.eenheden[self.boot][T][kleur][welk_type][nivo]
        self.begin_verdedigen = eenheid[VERDEDIGEN]
        self.begin_aanvallen = eenheid[AANVALLEN]
        self.begin_aanvallen_moraal = eenheid[AANVALLENMORAAL]
        self.begin_gezondheid = eenheid[GEZONDHEID]
        self.begin_moraal = eenheid[MORAAL]
        self.begin_bewegen = eenheid[BEWEGEN]
        self.start_bewegen = self.begin_bewegen
        self.begin_bereik = eenheid[BEREIK]
        self.begin_uithouding = eenheid[UITHOUDING]
        self.begin_zicht = eenheid[ZICHT]
        self.begin_zichtbaar = eenheid[ZICHTBAARHEID]
        self.uithouding_terugkrijgen = eenheid[UITHOUDING_TERUGKRIJGEN]
        self.moraal_verdedigen = eenheid[MORAAL_VERDEDIGEN] * 10
        self.munitie = eenheid[MUNITIE]
        self.kan_ik_bouwen = eenheid[KAN_IK_BOUWEN]
        self.duwen = eenheid[DUWEN]
        self.duwbaarhijd = eenheid[DUWBAARHIJD]
        self.verdedigen = self.begin_verdedigen
        self.aanvallen = self.begin_aanvallen
        self.aanvallen_moraal = self.begin_aanvallen_moraal
        self.gezondheid = self.begin_gezondheid
        self.moraal = self.begin_moraal
        self.bewegen = self.start_bewegen
        self.bereik = self.begin_bereik
        self.vorig_x = self.x
        self.vorig_y = self.y
        self.verschil = 0
        self.is_geweest = False
        self.is_geselecteerd = False
        self.is_zichtbaar = False
        self.zicht = self.begin_zicht
        self.zichtbaar = self.begin_zichtbaar
        self.uithouding = self.begin_uithouding
        self.schade_gedaan = 0
        self.schade_gekregen = 0
        self.eenheden_gedood = 0
        self.aantal_keer_aangevallen = 0
        self.ervaring = 0
        self.ervaring_nivo = 0
        self.T = T

        self.extra_v = 0
        self.extra_u = 0
        if self.T == 0 or self.T == 3:
            self.extra_v = 176
        if self.boot == 0:
            if self.T == 0 or self.T == 1:
                self.extra_u = 192
            if self.T == 2 or self.T == 3:
                self.extra_u = 224
        else:
            if self.T == 2 or self.T == 3:
                self.extra_u = 96


    def raak_gewond(self, inkomende_aanval, inkomende_moraalaanval):
        # print(f"{self.moraal} : {self.gezondheid } : {self.verdedigen}")
        # self.gezondheid = self.gezondheid - (inkomende_aanval * (inkomende_aanval / self.verdedigen))#################################################
        for i in range(1, int(inkomende_moraalaanval)):
            if random.triangular(0, 100) > self.moraal_verdedigen:
                self.moraal -= 1
        for i in range(1, int(inkomende_aanval)):
            if random.triangular(0, 100) > self.verdedigen:
                self.gezondheid -= 1
        # print(f"{self.moraal} : {self.gezondheid }")
        # print(f" ")
        # self.moraal -= inkomende_moraalaanval - i
        # self.moraal -= inkomende_moraalaanval
        self.schade_gekregen += inkomende_aanval
        self.ervaring += inkomende_aanval


    def update(self, game):
        self.terrein = getTerrein()
        xverschil = abs(self.vorig_x - self.x)
        yverschil = abs(self.vorig_y - self.y)
        verschil = xverschil + yverschil
        if self.munitie <= 0:
            if self.welk_type == 3 or self.welk_type == 4:
                self.welk_type = 0
                eenheid = self.eenheden[self.boot][self.T][self.kleur][self.welk_type][self.nivo]
                self.begin_verdedigen = eenheid[VERDEDIGEN]
                self.begin_aanvallen = eenheid[AANVALLEN]
                self.begin_aanvallen_moraal = eenheid[AANVALLENMORAAL]
                self.begin_gezondheid = eenheid[GEZONDHEID]
                self.begin_moraal = eenheid[MORAAL]
                self.moraal = self.begin_moraal
                self.begin_bewegen = eenheid[BEWEGEN]
                self.start_bewegen = self.begin_bewegen
                self.begin_uithouding = eenheid[UITHOUDING]
                self.begin_zicht = eenheid[ZICHT]
                self.begin_zichtbaar = eenheid[ZICHTBAARHEID]
                self.moraal_verdedigen = eenheid[MORAAL_VERDEDIGEN] * 10
                self.munitie = 0
            self.begin_bereik = 1




        if self.ervaring > 50 * ((self.ervaring_nivo + 1)):# and self.nivo < 2 and self.eenheiden[self.kleur][self.welk_type][self.nivo + 1][0] > 0:
            self.begin_aanvallen += 1
            self.begin_gezondheid += 3
            self.begin_verdedigen += 2
            self.begin_moraal += 3
            self.moraal_verdedigen += 2
            self.ervaring_nivo += 1
#rontkijken of ik npg kan beweegen
        # kan_ik_nog_bewegen = False
        # if not self.is_geweest:
        #     for y in range(-1, 2):
        #         y += self.y // 16
        #         for x in range(-1, 2):
        #             x += self.x // 16
        #             if ondergrond_impact[self.terrein[y][x]] <= self.bewegen:
        #                 kan_ik_nog_bewegen = True
        #     if not kan_ik_nog_bewegen:
        #         self.is_geweest = True

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if verschil > self.bewegen * 8:
                self.x = self.vorig_x
                self.y = self.vorig_y
        # print(self.gezondijd , self.MORAAL)
        self.xverschil = abs(game.aangepaste_x - self.x)
        self.yverschil = abs(game.aangepaste_y - self.y)
        self.verschil = self.xverschil + self.yverschil
        self.vorig_x = self.x
        self.vorig_y = self.y
        self.vlakterrein = getTerrein()
        ondergrond = getTerrein()[int(self.y / 16)][int(self.x / 16)]

        if self.uithouding <= 0:
            self.is_geweest = True

        if ondergrond == GRAS:
            self.verdedigen = self.begin_verdedigen
            self.bereik = self.begin_bereik
            self.zichtbaar = self.begin_zichtbaar
            self.zicht = self.begin_zicht
            self.aanvallen = self.begin_aanvallen

        if ondergrond == BOS:
            if self.bereik > 3:
                self.bereik = self.begin_bereik - 2
            self.zichtbaar = self.begin_zichtbaar + 3
            self.verdedigen = self.begin_verdedigen
            self.zicht = self.begin_zicht
            self.aanvallen = self.begin_aanvallen

        if ondergrond == WATER:
            self.verdedigen = self.begin_verdedigen - 20
            self.bereik = self.begin_bereik
            self.zichtbaar = self.begin_zichtbaar
            self.zicht = self.begin_zicht
            self.aanvallen = self.begin_aanvallen

        if ondergrond == BERG:
            self.verdedigen = self.begin_verdedigen + 5
            if self.bereik > 2:
                self.bereik = self.begin_bereik + 2
            self.zicht = self.begin_zicht + 4
            self.zichtbaar = self.begin_zichtbaar - 2
            self.aanvallen = self.begin_aanvallen

        if ondergrond == WEG:
            self.verdedigen = self.begin_verdedigen
            self.bereik = self.begin_bereik
            self.zichtbaar = self.begin_zichtbaar
            self.zicht = self.begin_zicht
            self.aanvallen = self.begin_aanvallen

        if ondergrond == BRUG:
            self.verdedigen = self.begin_verdedigen
            self.bereik = self.begin_bereik
            self.zichtbaar = self.begin_zichtbaar
            self.zicht = self.begin_zicht
            self.aanvallen = self.begin_aanvallen

        if ondergrond == GEBOUW:
            self.verdedigen = self.begin_verdedigen + 5
            self.bereik = self.begin_bereik
            self.zichtbaar = self.begin_zichtbaar + 2
            self.zicht = self.begin_zicht - 1
            self.aanvallen = self.begin_aanvallen

        if ondergrond == MUUR:
            self.verdedigen += 10
            if self.bereik > 2:
                self.bereik = self.begin_bereik + 2
            self.zicht = self.begin_zicht + 4
            self.zichtbaar = self.begin_zichtbaar

        if ondergrond == POORT:
            self.verdedigen += 10
            if self.bereik > 2:
                self.bereik = self.begin_bereik + 2
            self.zicht = self.begin_zicht + 4
            self.zichtbaar = self.begin_zichtbaar



    def draw(self, game, is_voorbeeld):
        if is_voorbeeld:
            extra_x = 0
            extra_y = 0
        else:
            extra_x = game.begin_teken_x * 16
            extra_y = game.begin_teken_y * 16

        if self.gezondheid > 0 or self.moraal > 0:
            if self.boot == 0:
                if not is_voorbeeld:
                    if game.lijst_met_terijnblokken[(self.y + extra_y) // 16][(self.x + extra_x) // 16].ben_ik_zichtbaar == True:
                        pyxel.rect(self.x + extra_x, self.y + extra_y, 15, 15, 6)
            if self.is_zichtbaar:
                if self.boot == 1:
                    pyxel.blt(self.x   + extra_x, self.y      + extra_y, 0, self.nivo * 16     , self.kleur * 16 + 80, 16, 16 ,pyxel.COLOR_BLACK)
                    pyxel.blt(self.x   + extra_x, self.y      + extra_y, 0, self.welk_type * 16 + self.extra_u, (self.kleur * 16)+ self.extra_v, 16, 16 ,pyxel.COLOR_BLACK)
                    pyxel.blt(self.x + extra_x, self.y + 14 + extra_y, 0, 0, self.kleur * 16 + 80, self.gezondheid / (self.begin_gezondheid / 6), 1, pyxel.COLOR_BLACK)
                    pyxel.blt(self.x+9 + extra_x, self.y + 14 + extra_y, 0, 0, self.kleur * 16 + 80,self.moraal/(self.begin_moraal/6), 1 ,pyxel.COLOR_BLACK)

                else:
                    pyxel.blt(self.x   + extra_x, self.y      + extra_y, 0, self.nivo * 16     , self.kleur * 16 + 80, 16, 16 ,pyxel.COLOR_BLACK)
                    pyxel.blt(self.x   + extra_x, self.y      + extra_y, 0, self.welk_type * 16 + self.extra_u, (self.kleur * 16) + self.extra_v, 16, 16 ,pyxel.COLOR_BLACK)
                    pyxel.blt(self.x + extra_x, self.y + 14 + extra_y, 0, 0, self.kleur * 16 + 80, self.gezondheid / (self.begin_gezondheid / 6), 1, pyxel.COLOR_BLACK)
                    pyxel.blt(self.x+9 + extra_x, self.y + 14 + extra_y, 0, 0 , self.kleur * 16 + 80, self.moraal/(self.begin_moraal/6), 1 ,pyxel.COLOR_BLACK)


        else:
            pyxel.blt(self.x       + extra_x, self.y + extra_y     , 0,64                  , self.kleur * 16 + 80, 16, 16 ,pyxel.COLOR_BLACK)



