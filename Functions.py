import numpy as np
import random as random
import matplotlib.pyplot as plt
import Individu as Indiv


individues = []
distances = []


def creer_villes():

    villes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    villesStr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    return villes, villesStr


def creerCoordonnees(villes, villesStr):
    # Coordonnees X
    x = np.random.rand(10)

    # Coordnonnees Y
    y = np.random.rand(10)

    # Coordonnes X et Y ensemble dans un tuple
    coordonnees = [i for i in zip(x, y)]

    # Villes et coordonnees X, Y ensemble dans un dictionnaire
    coordonneesVilles = {ville: i for (ville, i) in zip(villes, coordonnees)}
    coordonneesVillesStr = {ville: i for (ville, i) in zip(villesStr, coordonnees)}

    return x, y, coordonnees, coordonneesVilles, coordonneesVillesStr


def creerIndividues(villes, villesStr, x, y, coordonnees, coordonneesVilles, coordonneesVillesStr):

    listIndividues = []

    for n in range(100):
        individu = Indiv.Individu(villes, villesStr, x, y, coordonnees, coordonneesVilles, coordonneesVillesStr)
        listIndividues.append(individu)

    return listIndividues


def plot(individu):

    x = []
    y = []
        
    for ville in individu.parcoursList:
        
        x.append(individu.coordonneesVilles[ville][0])
        y.append(individu.coordonneesVilles[ville][1])
        
    plt.plot(x, y, marker='o')

    for i, coordonneesVille in enumerate(individu.coordonnees):
        plt.text(coordonneesVille[0], coordonneesVille[1], str(i), fontsize=12)


def croisementOOP(listIndividues50):

    generation1 = []
    count = 0
    doubles1 = []
    doubles2 = []
    indexList = []
    morceau1 = []
    morceau2 = []

    while count <= 24:

        doubles1.clear()
        doubles2.clear()

        morceau1.clear()
        morceau2.clear()

# Sélection aleatoire des parents
        parent1 = random.choice(listIndividues50)
        listIndividues50.remove(parent1)
        parent2 = random.choice(listIndividues50)
        listIndividues50.remove(parent2)


# Sauvegarde des parcours des parents dans des variables
        parcours1 = parent1.parcoursList
        parcours2 = parent2.parcoursList

# Sauvegarde du morceau de chaque parcours qui sera utilisé pour le croisement
        for n in range(6, 9):
            morceau1.append(parent2.parcoursList[n])
            morceau2.append(parent1.parcoursList[n])

# Croisement

        for n in range(6, 9):

            parcours1[n] = morceau1[n - 6]
            parcours2[n] = morceau2[n - 6]

        # Cherche pour des doublons
        for f1 in parcours1:

            nb = parcours1.count(f1)
            index = parcours1.index(f1)

            if (index == 0 and nb == 2) or (index == 10 and nb == 2):
                continue

            else:

                if nb >= 2 and f1 not in doubles1:
                    doubles1.append(f1)

        for f2 in parcours2:

            nb = parcours2.count(f2)
            index = parcours2.index(f2)

            if (index == 0 and nb == 2) or (index == 10 and nb == 2):
                continue

            else:

                if nb >= 2 and f2 not in doubles2:
                    doubles2.append(f2)

        # Eliminations des doublons
        if len(doubles1) > 0 and len(doubles2) > 0:

            if parcours1[0] == doubles1[0]:

                index = parcours1.index(doubles1[0], 1)
                parcours1[index] = doubles2[0]

            else:

                index = parcours1.index(doubles1[0])
                parcours1[index] = doubles2[0]

            if parcours2[0] == doubles2[0]:

                index = parcours2.index(doubles2[0], 1)
                parcours2[index] = doubles1[0]

            else:

                index = parcours2.index(doubles2[0])
                parcours2[index] = doubles1[0]

            if len(doubles1) > 1 and len(doubles2) > 1:

                indexList.append(parcours1.index(doubles1[1]))
                indexList.append(parcours2.index(doubles2[1]))

                parcours1[indexList[0]] = doubles2[1]
                parcours2[indexList[1]] = doubles1[1]

                indexList.clear()

                if len(doubles1) > 2 and len(doubles2) > 2:

                    indexList.append(parcours1.index(doubles1[2]))
                    indexList.append(parcours2.index(doubles2[2]))

                    parcours1[indexList[0]] = doubles2[2]
                    parcours2[indexList[1]] = doubles1[2]

                    indexList.clear()


# Creation des nouveaux individues d'après le croisement

        fils1 = parent1
        fils2 = parent2

        fils1.parcoursList = parcours1
        fils2.parcoursList = parcours2

        fils1.toStr(fils1.parcoursList)
        fils2.toStr(fils2.parcoursList)

        fils1.calculerDistance()
        fils2.calculerDistance()

        generation1.append(fils1)
        generation1.append(fils2)

        count += 1

    return generation1

# Mutation


def mutation(generation1):
    
    for individu in generation1:
        
        individu.mutation()
        
    return generation1
        
        



