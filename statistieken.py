
import matplotlib.pyplot as plt
import numpy as np

waardes = [4, 10, 10, 5, 5, 5, 10, 6, 10, 30, 20, 41, 25]

tijden = [
    [[], [], [], [], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], [], [], [], []],
]

from eenheid import Eenheid
booten = Eenheid.eenheden[0]
eenheiden = Eenheid.eenheden[1]
for i, tijd in enumerate(eenheiden):
    for kleur in tijd:
        for eenheid in kleur:
            for nivo in eenheid:
                for ii, statistiek in enumerate(nivo):
                    if nivo[0] != 0:
                        tijden[i][ii].append(statistiek)
print(tijden)


plt.style.use('_mpl-gallery')

# make data
x = np.arange(0, 65, 5)

y = [[], [], [], []]

for i,  tijd in enumerate(tijden):
    for ii, statistiek in enumerate(tijd):
        # ay.append(min(statistiek))
        # getal = (sum(statistiek) // len(statistiek))
        getal = (max(statistiek))
        # getal = (min(statistiek))
        # if i > 0:
        #     getal = getal - y[i - 1][ii]
        y[i].append(getal)
        # cy.append((max(statistiek)) - by[i])

y = np.vstack([y[0], y[1], y[2], y[3]])

# plot
fig, ax = plt.subplots()

ax.stackplot(x, y)

ax.set(xlim=(0, 8), xticks=np.arange(1, 60),
        ylim=(0, 8), yticks=np.arange(1, 60))

plt.show()
print('VerAanAnmGezMorBewBerUitZieTerBaaMveMun')
print(y)

prijzen = []

for i, tijd in enumerate(eenheiden):
    prijzen.append([])
    for ii, kleur in enumerate(tijd):
        prijzen[i].append([])
        for iii, eenheid in enumerate(kleur):
            prijzen[i][ii].append([0, 0, 0, 0])
            for iv, nivo in enumerate(eenheid):
                # prijzen[i][ii][iii].append([1])
                for v, statistiek in enumerate(nivo):
                    prijzen[i][ii][iii][iv] += statistiek * waardes[v]
                if prijzen[i][ii][iii][iv] > 0:
                    prijzen[i][ii][iii][iv] -= 300
for i, tijd in enumerate(eenheiden):
    print(f"|||||||||||||||{i}|||||||||||||||")
    for ii, kleur in enumerate(tijd):
        print(f"||{ii + 1}||")
        for iii, eenheid in enumerate(kleur):
            print(prijzen[i][ii][iii])

