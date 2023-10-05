import numpy as np
import random as random
import matplotlib.pyplot as plt
import math

villes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
villesStr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def faireListInt(listStr):

    listInt = [[int(ville) for ville in parcours] for parcours in listStr]

    return listInt
def faireListStrings(individues):

    individuesStr = []
    invStr = ''

    for individue in individues:

        for l in individue:
            invStr += str(l)

        individuesStr.append(invStr)
        invStr = ''

    return individuesStr

 # Coordonnees X
coordonneesX = np.random.rand(10)

# Coordnonnees Y
coordonneesY = np.random.rand(10)

# Coordonnes X et Y ensemble dans un tuple
coordonnees = [i for (i) in zip(coordonneesX, coordonneesY)]

# Villes et coordonnees X, Y ensemble dans un dictionnaire
coordonneesVilles = {ville: i for (ville, i) in zip(villes, coordonnees)}
coordonnesVillesStr = {ville: i for (ville, i) in zip(villesStr, coordonnees)}
individues = []
distances = []

def creer_villes():

    villesList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    return villesList


def creer_individues(villes):

    for n in range(0, 100):

        individues.append(random.sample(villes, k=len(villes)))
        individues[n].append(individues[n][0])

    #print("Individues:", individues)
    #print("Nombre d'individues: ", len(individues))

    individuesStr = faireListStrings(individues)

    return individues, individuesStr


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

    distances.clear()

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

def dictionnaire50(dictIndivDist):

    dictIndivDist50 = {k: dictIndivDist[k] for k in list(dictIndivDist)[:50]}


    return dictIndivDist50


def croisement(dic50):

    generation1 = []
    count = 0
    keys = list(dic50.keys())
    doubles1 = []
    doubles2 = []

    while count <= 24:

        doubles1.clear()
        doubles2.clear()
        fils1 = ''
        fils2 = ''

        # Sélection aleatoire des parents
        parent1 = random.choice(keys)
        parent2 = random.choice(keys)

        # Croisement
        fils1 = parent1.replace(parent1[6:9], parent2[6:9])
        fils2 = parent2.replace(parent2[6:9], parent1[6:9])

        # Cherche pour des doubles
        for f1 in fils1:
            
            nb = fils1.count(f1)
            index = fils1.index(f1)
            
            if index == 0 and nb == 2:
                continue

            else:
                
                if nb >= 2 and f1 not in doubles1:
                    doubles1.append(f1)


        for f2 in fils2:
            
            nb = fils2.count(f2)  
            index = fils2.index(f2)
            
            if index == 0 and nb == 2:
                continue
            
            else:

                if nb >= 2 and f2 not in doubles2:
                    doubles2.append(f2)

        # Eliminations des doubles
        if len(doubles1) > 0 and len(doubles2) > 0:

            fils1 = fils1.replace(doubles1[0], doubles2[0], 1)
            fils2 = fils2.replace(doubles2[0], doubles1[0], 1)

            if len(doubles1) > 1 and len(doubles2) > 1:
                fils1 = fils1.replace(doubles1[1], doubles2[1], 1)
                fils2 = fils2.replace(doubles2[1], doubles1[1], 1)

                if len(doubles1) > 2 and len(doubles2) > 2:
                    fils1 = fils1.replace(doubles1[2], doubles2[2], 1)
                    fils2 = fils2.replace(doubles2[2], doubles1[2], 1)

        generation1.append(fils1)
        generation1.append(fils2)

        count += 1

    generation1Int= faireListInt(generation1)
    #print("Generation 1 string:", generation1)
    #print("Generation 1 int: ", generation1Int)
    #print("Nombres d'enfants generation 1: ", len(generation1Int))

    return generation1, generation1Int




def plot(parcours):

    plt.figure(figsize=(10, 10))
    plt.plot(coordonneesX, coordonneesY, 'o-')
    for i, city in enumerate(parcours):
        plt.text(city[0], city[1], str(i), fontsize=12, ha='right')
    plt.title('Le parcours le plus court')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

def plot2(cheminPlusCourt, distanceOptimale):

    #print("Coordonnées villes: ", coordonnesVillesStr)

    x = []
    y = []

    for ville in cheminPlusCourt:
        x.append(coordonnesVillesStr[ville][0])
        y.append(coordonnesVillesStr[ville][1])

    plt.plot(x, y, marker='o')

    for i, city in enumerate(coordonnees):
        plt.text(city[0], city[1], str(i), fontsize=12, ha='right')



# Mutation




