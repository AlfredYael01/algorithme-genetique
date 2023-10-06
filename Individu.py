import numpy as np
import random as random
import matplotlib.pyplot as plt
import math
import Functions as fc


class Individu:

    parcoursList = []
    parcoursStr = ""
    distance = 0

    def __init__(self, villes, villesStr, x, y, coordonnees, coordonneesVilles, coordonneesVillesStr):

        self.villes = villes
        self.villesStr = villesStr
        self.x = x
        self.y = y
        self.coordonnees = coordonnees
        self.coordonneesVilles = coordonneesVilles
        self.coordonneesVillesStr = coordonneesVillesStr
        self.creerParcours()
        self.calculerDistace()

    def creerParcours(self):

        self.parcoursList = random.sample(self.villes, k=len(self.villes))
        self.parcoursList.append(self.parcoursList[0])

        self.toStr(self.parcoursList)

    def toStr(self, parcours):

        for ville in parcours:
            self.parcoursStr += str(ville)

    def toInt(self, parcoursStr):

        for ville in parcoursStr:
            self.parcoursList.append(int(ville))

    def calculerDistace(self):

        i = 0

        # Dans le 'while' on mesure la distance entre chaque ville
        while i < 10:

            # Quand on arrive a la derniere ville, on stop le while
            #if i == 9:
                #break

            ville1 = self.parcoursList[i]
            ville2 = self.parcoursList[i + 1]

            # On sauvegarde la distance entre chacune des villes
            self.distance = self.distance + self.calculer_distance_entre_2_villes(ville1, ville2)
            i += 1

    def calculer_distance_entre_2_villes(self, ville1, ville2):

        distance = math.sqrt((math.pow(self.coordonneesVilles[ville2][0] - self.coordonneesVilles[ville1][0], 2)) + (
            math.pow(self.coordonneesVilles[ville2][1] - self.coordonneesVilles[ville1][1], 2)))

        return distance

