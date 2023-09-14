import numpy as np
import random as random
import matplotlib.pyplot as plt


villes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

coordonneesX = np.random.rand(10)
coordonneesY = np.random.rand(10)
individues = []
listIndividues = []


def creation_individues(villes):
    count = 0
    for n in range(0, 100):

        individues.append(random.sample(villes, k=len(villes)))
        print(individues[count])
        listIndividues.append(individues)
        count = count + 1

    print(count)


creation_individues(villes)
print(listIndividues)
print(len(listIndividues))



