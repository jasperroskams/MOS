
import random

aantal_random = 20
hoeveel_random = [0] * aantal_random
verdedigopties = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

for i, verdedeging in enumerate(verdedigopties):
    for ii in range(0, 10000000):
        random_getal_1 = int(random.triangular(0, 100))
        random_getal_2 = int(random.triangular(-100, 0))
        random_getal_3 = int(random.triangular(100, 200))
        random_getal = (random_getal_1 + random_getal_2 + random_getal_3) // 3
        if random_getal <= verdedeging:
            hoeveel_random[i] += 1
        print(random_getal, i, ii)


print('#################################################################################################################################################################################################################################################')
for i in range(0, len(hoeveel_random)):
    print(hoeveel_random[i])



















