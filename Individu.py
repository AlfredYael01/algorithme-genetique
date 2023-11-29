import random as random
import matplotlib.pyplot as plt
import math


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
        self.calculerDistance()

    def creerParcours(self):

        self.parcoursList = random.sample(self.villes, k=len(self.villes))
        self.parcoursList.append(self.parcoursList[0])

        self.toStr(self.parcoursList)

    def toStr(self, parcours):

        self.parcoursStr = ''

        for ville in parcours:
            self.parcoursStr += str(ville)

    def toInt(self, parcoursStr):

        self.parcoursList = []

        for ville in parcoursStr:
            self.parcoursList.append(int(ville))

    def calculerDistance(self):

        self.distance = 0
        i = 0

        # Dans le 'while' on mesure la distance entre chaque ville
        #while i < 10:
        while i < len(self.villes):
            ville1 = self.parcoursList[i]
            ville2 = self.parcoursList[i + 1]

            # On sauvegarde la distance entre chacune des villes
            self.distance = self.distance + self.calculer_distance_entre_2_villes(ville1, ville2)
            i += 1

    def calculer_distance_entre_2_villes(self, ville1, ville2):

        distance = math.sqrt((math.pow(self.coordonneesVilles[ville2][0] - self.coordonneesVilles[ville1][0], 2)) +
                             (math.pow(self.coordonneesVilles[ville2][1] - self.coordonneesVilles[ville1][1], 2)))

        return distance

    def plot(self):

        x = []
        y = []

        for ville in self.parcoursList:
            x.append(self.coordonneesVilles[ville][0])
            y.append(self.coordonneesVilles[ville][1])

        plt.plot(x, y, marker='o')

        for i, coordonneesVille in enumerate(self.coordonnees):
            plt.text(coordonneesVille[0], coordonneesVille[1], str(i), fontsize=12)

    def mutation(self):

        ville1 = []
        ville2 = []

        # ville1 = self.parcoursList[1]
        # ville2 = self.parcoursList[5]
        #
        # self.parcoursList[1] = ville2
        # self.parcoursList[5] = ville1

        # ville1 = self.parcoursList[3]
        # ville2 = self.parcoursList[8]
        #
        # self.parcoursList[3] = ville2
        # self.parcoursList[8] = ville1

        ville1.append(self.parcoursList[1])
        ville1.append(self.parcoursList[2])
        ville2.append(self.parcoursList[18])
        ville2.append(self.parcoursList[19])

        self.parcoursList[1] = ville2[0]
        self.parcoursList[2] = ville2[1]
        self.parcoursList[18] = ville1[0]
        self.parcoursList[19] = ville1[1]

        self.calculerDistance()
        