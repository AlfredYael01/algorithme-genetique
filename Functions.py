import numpy as np
import random as random
import matplotlib.pyplot as plt
import math

villes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

 # Coordonnees X
coordonneesX = np.random.rand(10)

# Coordnonnees Y
coordonneesY = np.random.rand(10)

# Coordonnes X et Y ensemble dans un tuple
coordonnees = [i for (i) in zip(coordonneesX, coordonneesY)]

# Villes et coordonnees X, Y ensemble dans un dictionnaire
coordonneesVilles = {ville: i for (ville, i) in zip(villes, coordonnees)}

individues = []
distances = []

def creer_villes():

    villesList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    return villesList


def creer_individues(villes):

    for n in range(0, 100):

        individues.append(random.sample(villes, k=len(villes)))

    return individues


def calculer_distance_entre_2_villes(ville1, ville2):
    distance = math.sqrt((math.pow(coordonneesVilles[ville2][0] - coordonneesVilles[ville1][0], 2)) + (
        math.pow(coordonneesVilles[ville2][1] - coordonneesVilles[ville1][1], 2)))

    # print("x2:", coordonneesVilles[ville2][0])
    # print("x1:", coordonneesVilles[ville1][0])
    # print("y2:", coordonneesVilles[ville2][1])
    # print("y1:", coordonneesVilles[ville1][1])
    # print("Distance: ", distance)

    return distance


def calculer_distances(individues):
    for individu in individues:

        distance = 0
        i = 0

        # Dans le 'while' on mesure la distance de chaque parcours
        while i <= 9:

            # Quand on arrive a la derniere ville, on mesure la distance entre celle-ci et la premiere
            if i == 9:
                ville1 = individu[i]
                ville2 = individu[0]
                distance = distance + calculer_distance_entre_2_villes(ville1, ville2)
                break

            ville1 = individu[i]
            ville2 = individu[i + 1]

            # On sauvegarde la distance entre chacune des villes
            distance = distance + calculer_distance_entre_2_villes(ville1, ville2)
            i += 1

        # On sauvegarde la distance du parcours de chaque individu dans une liste
        distances.append(distance)

    return distances



