import numpy as np
import random as random
import matplotlib.pyplot as plt
import math
import Individu as indiv
import Functions as fc

# Creation des villes et des coordonnee
villes, villesStr = fc.creer_villes()
x, y, coordonnees, coordonneesVilles, coordonnesVillesStr = fc.creerCoordonnees(villes, villesStr)


# Creation des premiers 100 individues et tri part distance croissante
listIndividues = fc.creerIndividues(villes, villesStr, x, y, coordonnees, coordonneesVilles, coordonnesVillesStr)
listIndividues.sort(key=lambda individu: individu.distance)

# Selection de 50 individues avec les distances le plus courtes
listIndividues50 = [individu for individu in listIndividues[:50]]

for individu in listIndividues50:

    print("Parcours :", individu.parcoursList)
    print("Parcours string: ", individu.parcoursStr)
    print("Distance: ", individu.distance)
    print("Coordonnees: ", individu.coordonneesVilles)
    print()

generation1 = fc.croisementOOP(listIndividues50)

print("Nb generation1: ", len(generation1))
