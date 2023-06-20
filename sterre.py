from eenheid import Eenheid
eenheiden = Eenheid.eenheden

eenheiden_waardes = [
    [
        [
            [],
            [],
            [],
            [],
            [],
            []
        ],
        [
            [],
            [],
            [],
            [],
            [],
            []
        ],
        [
            [],
            [],
            [],
            [],
            [],
            []
        ],
        [
            [],
            [],
            [],
            [],
            [],
            []
        ],
        [
            [],
            [],
            [],
            [],
            [],
            []
        ],
    ],
    [
        [
            [],
            [],
            [],
            [],
            [],
            []
        ],
        [
            [],
            [],
            [],
            [],
            [],
            []
        ],
        [
            [],
            [],
            [],
            [],
            [],
            []
        ],
        [
            [],
            [],
            [],
            [],
            [],
            []
        ],
        [
            [],
            [],
            [],
            [],
            [],
            []
        ],
    ]
]
hoogste_waardes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
laagste_waardes = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]

for i, T in enumerate(eenheiden):
    for ii, kleur in enumerate(T):
        for iii,  type in enumerate(kleur):
            for iv, nivo in enumerate(type):
                for v, waarde in enumerate(nivo):
                    if waarde > hoogste_waardes[v]:
                        hoogste_waardes[v] = waarde
                        break
                    if waarde < laagste_waardes[v] and waarde != 0:
                        laagste_waardes[v] = waarde
                        break

    for ii, kleur in enumerate(T):
        for iii,  type in enumerate(kleur):
            for iv, nivo in enumerate(type):
                eenheiden_waarde = 0
                for v, waarde in enumerate(nivo):
                    if waarde > 0:
                        eenheiden_waarde += (waarde * laagste_waardes[v]) / hoogste_waardes[v]
                eenheiden_waardes[i][ii][iii].append(int(((eenheiden_waarde / v) - 2) * 10))



    print('[')
    for ii, kleur in enumerate(T):
        print('[')
        for iii,  type in enumerate(kleur):
            for iv, nivo in enumerate(type):
                if eenheiden_waardes[i][ii][iii][iv] < 0:
                    eenheiden_waardes[i][ii][iii][iv] = 0
            print(str(eenheiden_waardes[i][ii][iii]) + ',')
        print('],')
    print('],')



