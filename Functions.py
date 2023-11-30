import numpy as np
import random as random
import matplotlib.pyplot as plt
import Individu as Indiv
import copy

individues = []
distances = []

def creer_villes(nbVilles):

    villes = []
    villesStr = []
    
    for i in range(nbVilles):
        villes.append(i)
        villesStr.append(str(i))
        
    return villes, villesStr


def creerCoordonnees(villes, villesStr):
    # Coordonnees X
    x = np.random.rand(len(villes))

    # Coordnonnees Y
    y = np.random.rand(len(villes))

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


def croisementOOP6(individues):
    nbIndividues = len(individues)
    listIndividues = copy.deepcopy(individues)
    generation = []
    count = 0
    doubles1 = []
    doubles2 = []
    indexList = []
    morceau1 = []
    morceau2 = []

    while count < nbIndividues / 2:

        doubles1.clear()
        doubles2.clear()
        morceau1.clear()
        morceau2.clear()

        # Sélection aleatoire des parents
        parent1 = random.choice(listIndividues)
        listIndividues.remove(parent1)
        parent2 = random.choice(listIndividues)
        listIndividues.remove(parent2)

        # Sauvegarde des parcours des parents dans des variables
        parcours1 = parent1.parcoursList
        parcours2 = parent2.parcoursList

        # Sauvegarde du morceau de chaque parcours qui sera utilisé pour le croisement
        # for n in range(6, 9):
        for n in range(2, 4):
            morceau1.append(parent2.parcoursList[n])
            morceau2.append(parent1.parcoursList[n])

        # Croisement

        # for n in range(6, 9):
        for n in range(2, 4):
            # parcours1[n] = morceau1[n - 6]
            # parcours2[n] = morceau2[n - 6]
            parcours1[n] = morceau1[n - 2]
            parcours2[n] = morceau2[n - 2]


        for f1 in parcours1:

            nb = parcours1.count(f1)
            index = parcours1.index(f1)

            if (index == 0 and nb == 2) or (index == 6 and nb == 2):
                continue

            else:

                if nb >= 2 and f1 not in doubles1:
                    doubles1.append(f1)

        for f2 in parcours2:

            nb = parcours2.count(f2)
            index = parcours2.index(f2)

            if (index == 0 and nb == 2) or (index == 6 and nb == 2):
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

        generation.append(fils1)
        generation.append(fils2)

        count = count + 1

    return generation





def croisementOOP10(individues):
    nbIndividues = len(individues)
    listIndividues = copy.deepcopy(individues)
    generation = []
    count = 0
    doubles1 = []
    doubles2 = []
    indexList = []
    morceau1 = []
    morceau2 = []

    while count < nbIndividues / 2:

        doubles1.clear()
        doubles2.clear()
        morceau1.clear()
        morceau2.clear()

        # Sélection aleatoire des parents
        parent1 = random.choice(listIndividues)
        listIndividues.remove(parent1)
        parent2 = random.choice(listIndividues)
        listIndividues.remove(parent2)

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

        generation.append(fils1)
        generation.append(fils2)

        count = count + 1

    return generation


def croisementOOP20(individues):
    nbIndividues = len(individues)
    listIndividues = copy.deepcopy(individues)
    generation = []
    count = 0
    doubles1 = []
    doubles2 = []
    indexList = []
    morceau1 = []
    morceau2 = []

    while count < nbIndividues / 2:

        doubles1.clear()
        doubles2.clear()
        morceau1.clear()
        morceau2.clear()

        # Sélection aleatoire des parents
        parent1 = random.choice(listIndividues)
        listIndividues.remove(parent1)
        parent2 = random.choice(listIndividues)
        listIndividues.remove(parent2)

        # Sauvegarde des parcours des parents dans des variables
        parcours1 = parent1.parcoursList
        parcours2 = parent2.parcoursList

        # Sauvegarde du morceau de chaque parcours qui sera utilisé pour le croisement
        for n in range(12, 17):
            morceau1.append(parent2.parcoursList[n])
            morceau2.append(parent1.parcoursList[n])

        # Croisement

        for n in range(12, 17):
            # parcours1[n] = morceau1[n - 6]
            # parcours2[n] = morceau2[n - 6]
            parcours1[n] = morceau1[n - 12]
            parcours2[n] = morceau2[n - 12]

        for f1 in parcours1:

            nb = parcours1.count(f1)
            index = parcours1.index(f1)

            if (index == 0 and nb == 2) or (index == 20 and nb == 2):
                continue

            else:

                if nb >= 2 and f1 not in doubles1:
                    doubles1.append(f1)

        for f2 in parcours2:

            nb = parcours2.count(f2)
            index = parcours2.index(f2)

            if (index == 0 and nb == 2) or (index == 20 and nb == 2):
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
                    
                    if len(doubles1) > 3 and len(doubles2) > 3:
                        indexList.append(parcours1.index(doubles1[3]))
                        indexList.append(parcours2.index(doubles2[3]))

                        parcours1[indexList[0]] = doubles2[3]
                        parcours2[indexList[1]] = doubles1[3]

                        indexList.clear()
                        
                        if len(doubles1) > 4 and len(doubles2) > 4:
                            indexList.append(parcours1.index(doubles1[4]))
                            indexList.append(parcours2.index(doubles2[4]))

                            parcours1[indexList[0]] = doubles2[4]
                            parcours2[indexList[1]] = doubles1[4]

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

        generation.append(fils1)
        generation.append(fils2)

        count = count + 1

    return generation



def croisementOOP100(individues):
    nbIndividues = len(individues)
    listIndividues = copy.deepcopy(individues)        
    generation = []
    count = 0
    doubles1 = []
    doubles2 = []
    indexList = []
    morceau1 = []
    morceau2 = []

    while count < nbIndividues / 2:

        doubles1.clear()
        doubles2.clear()
        morceau1.clear()
        morceau2.clear()

        # Sélection aleatoire des parents
        parent1 = random.choice(listIndividues)
        listIndividues.remove(parent1)
        parent2 = random.choice(listIndividues)
        listIndividues.remove(parent2)

        # Sauvegarde des parcours des parents dans des variables
        parcours1 = parent1.parcoursList
        parcours2 = parent2.parcoursList

        # Sauvegarde du morceau de chaque parcours qui sera utilisé pour le croisement
        for n in range(60, 81):
            morceau1.append(parent2.parcoursList[n])
            morceau2.append(parent1.parcoursList[n])

        # Croisement

        for n in range(60, 81):
            # parcours1[n] = morceau1[n - 6]
            # parcours2[n] = morceau2[n - 6]
            parcours1[n] = morceau1[n - 60]
            parcours2[n] = morceau2[n - 60]

        for f1 in parcours1:

            nb = parcours1.count(f1)
            index = parcours1.index(f1)

            if (index == 0 and nb == 2) or (index == 100 and nb == 2):
                continue

            else:

                if nb >= 2 and f1 not in doubles1:
                    doubles1.append(f1)

        for f2 in parcours2:

            nb = parcours2.count(f2)
            index = parcours2.index(f2)

            if (index == 0 and nb == 2) or (index == 100 and nb == 2):
                continue

            else:

                if nb >= 2 and f2 not in doubles2:
                    doubles2.append(f2)

        # Eliminations des doublons
         
        for j in range(0, len(morceau1)):
                
            if j == 0:
                
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
                    
            else:
                
                if len(doubles1) > j and len(doubles2) > j:
                    
                    indexList.append(parcours1.index(doubles1[j]))
                    indexList.append(parcours2.index(doubles2[j]))

                    parcours1[indexList[0]] = doubles2[j]
                    parcours2[indexList[1]] = doubles1[j]

                    indexList.clear()                    
                    
                
        # if len(doubles1) > 0 and len(doubles2) > 0:
        #
        #     if parcours1[0] == doubles1[0]:
        #
        #         index = parcours1.index(doubles1[0], 1)
        #         parcours1[index] = doubles2[0]
        #
        #     else:
        #
        #         index = parcours1.index(doubles1[0])
        #         parcours1[index] = doubles2[0]
        #
        #     if parcours2[0] == doubles2[0]:
        #
        #         index = parcours2.index(doubles2[0], 1)
        #         parcours2[index] = doubles1[0]
        #
        #     else:
        #
        #         index = parcours2.index(doubles2[0])
        #         parcours2[index] = doubles1[0]
        #
        #     if len(doubles1) > 1 and len(doubles2) > 1:
        #
        #         indexList.append(parcours1.index(doubles1[1]))
        #         indexList.append(parcours2.index(doubles2[1]))
        #
        #         parcours1[indexList[0]] = doubles2[1]
        #         parcours2[indexList[1]] = doubles1[1]
        #
        #         indexList.clear()
        #
        #         if len(doubles1) > 2 and len(doubles2) > 2:
        #             indexList.append(parcours1.index(doubles1[2]))
        #             indexList.append(parcours2.index(doubles2[2]))
        #
        #             parcours1[indexList[0]] = doubles2[2]
        #             parcours2[indexList[1]] = doubles1[2]
        #
        #             indexList.clear()
        #
        #             if len(doubles1) > 3 and len(doubles2) > 3:
        #                 indexList.append(parcours1.index(doubles1[3]))
        #                 indexList.append(parcours2.index(doubles2[3]))
        #
        #                 parcours1[indexList[0]] = doubles2[3]
        #                 parcours2[indexList[1]] = doubles1[3]
        #
        #                 indexList.clear()
        #
        #                 if len(doubles1) > 4 and len(doubles2) > 4:
        #                     indexList.append(parcours1.index(doubles1[4]))
        #                     indexList.append(parcours2.index(doubles2[4]))
        #
        #                     parcours1[indexList[0]] = doubles2[4]
        #                     parcours2[indexList[1]] = doubles1[4]
        #
        #                     indexList.clear()
        #                     
                        

        # Creation des nouveaux individues d'après le croisement

        fils1 = parent1
        fils2 = parent2

        fils1.parcoursList = parcours1
        fils2.parcoursList = parcours2

        fils1.toStr(fils1.parcoursList)
        fils2.toStr(fils2.parcoursList)

        fils1.calculerDistance()
        fils2.calculerDistance()

        generation.append(fils1)
        generation.append(fils2)

        count = count + 1

    return generation




def croisementOOP250(individues):
    nbIndividues = len(individues)
    listIndividues = copy.deepcopy(individues)
    generation = []
    count = 0
    doubles1 = []
    doubles2 = []
    indexList = []
    morceau1 = []
    morceau2 = []

    while count < nbIndividues / 2:

        doubles1.clear()
        doubles2.clear()
        morceau1.clear()
        morceau2.clear()

        # Sélection aleatoire des parents
        parent1 = random.choice(listIndividues)
        listIndividues.remove(parent1)
        parent2 = random.choice(listIndividues)
        listIndividues.remove(parent2)

        # Sauvegarde des parcours des parents dans des variables
        parcours1 = parent1.parcoursList
        parcours2 = parent2.parcoursList

        # Sauvegarde du morceau de chaque parcours qui sera utilisé pour le croisement
        for n in range(150, 201):
            morceau1.append(parent2.parcoursList[n])
            morceau2.append(parent1.parcoursList[n])

        # Croisement

        for n in range(150, 201):
            # parcours1[n] = morceau1[n - 6]
            # parcours2[n] = morceau2[n - 6]
            parcours1[n] = morceau1[n - 150]
            parcours2[n] = morceau2[n - 150]

        for f1 in parcours1:

            nb = parcours1.count(f1)
            index = parcours1.index(f1)

            if (index == 0 and nb == 2) or (index == 250 and nb == 2):
                continue

            else:

                if nb >= 2 and f1 not in doubles1:
                    doubles1.append(f1)

        for f2 in parcours2:

            nb = parcours2.count(f2)
            index = parcours2.index(f2)

            if (index == 0 and nb == 2) or (index == 250 and nb == 2):
                continue

            else:

                if nb >= 2 and f2 not in doubles2:
                    doubles2.append(f2)

        # Eliminations des doublons
         
        for j in range(0, len(morceau1)):
                
            if j == 0:
                
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
                    
            else:
                
                if len(doubles1) > j and len(doubles2) > j:
                    
                    indexList.append(parcours1.index(doubles1[j]))
                    indexList.append(parcours2.index(doubles2[j]))

                    parcours1[indexList[0]] = doubles2[j]
                    parcours2[indexList[1]] = doubles1[j]

                    indexList.clear()                    
                    
                
        # if len(doubles1) > 0 and len(doubles2) > 0:
        #
        #     if parcours1[0] == doubles1[0]:
        #
        #         index = parcours1.index(doubles1[0], 1)
        #         parcours1[index] = doubles2[0]
        #
        #     else:
        #
        #         index = parcours1.index(doubles1[0])
        #         parcours1[index] = doubles2[0]
        #
        #     if parcours2[0] == doubles2[0]:
        #
        #         index = parcours2.index(doubles2[0], 1)
        #         parcours2[index] = doubles1[0]
        #
        #     else:
        #
        #         index = parcours2.index(doubles2[0])
        #         parcours2[index] = doubles1[0]
        #
        #     if len(doubles1) > 1 and len(doubles2) > 1:
        #
        #         indexList.append(parcours1.index(doubles1[1]))
        #         indexList.append(parcours2.index(doubles2[1]))
        #
        #         parcours1[indexList[0]] = doubles2[1]
        #         parcours2[indexList[1]] = doubles1[1]
        #
        #         indexList.clear()
        #
        #         if len(doubles1) > 2 and len(doubles2) > 2:
        #             indexList.append(parcours1.index(doubles1[2]))
        #             indexList.append(parcours2.index(doubles2[2]))
        #
        #             parcours1[indexList[0]] = doubles2[2]
        #             parcours2[indexList[1]] = doubles1[2]
        #
        #             indexList.clear()
        #
        #             if len(doubles1) > 3 and len(doubles2) > 3:
        #                 indexList.append(parcours1.index(doubles1[3]))
        #                 indexList.append(parcours2.index(doubles2[3]))
        #
        #                 parcours1[indexList[0]] = doubles2[3]
        #                 parcours2[indexList[1]] = doubles1[3]
        #
        #                 indexList.clear()
        #
        #                 if len(doubles1) > 4 and len(doubles2) > 4:
        #                     indexList.append(parcours1.index(doubles1[4]))
        #                     indexList.append(parcours2.index(doubles2[4]))
        #
        #                     parcours1[indexList[0]] = doubles2[4]
        #                     parcours2[indexList[1]] = doubles1[4]
        #
        #                     indexList.clear()
        #                     
                        

        # Creation des nouveaux individues d'après le croisement

        fils1 = parent1
        fils2 = parent2

        fils1.parcoursList = parcours1
        fils2.parcoursList = parcours2

        fils1.toStr(fils1.parcoursList)
        fils2.toStr(fils2.parcoursList)

        fils1.calculerDistance()
        fils2.calculerDistance()

        generation.append(fils1)
        generation.append(fils2)

        count = count + 1

    return generation




# Mutation


def mutation(generation1):
    
    for individu in generation1:
        
        individu.mutation()
        
    return generation1
        
        

def trouverCheminPlusCourt(nbGenerations, nbVilles, listIndividues):
    
    count = 0
    individues = []
    generation = listIndividues
    meilleurIndividueParGeneration = []
    dicList = []
    doubles = []
    
    if(nbVilles == 6):
        
        while count < nbGenerations:
                
            individues = croisementOOP6(generation)
            #individues.sort(key=lambda individu: individu.distance, reverse=True)
            individues = mutation(individues)
            #individues.sort(key=lambda individu: individu.distance)
            
            generation.extend(individues)
                
            print(f"Censé d'être 100 : {len(generation)}")
            generation.sort(key=lambda individu: individu.distance)
            generation = generation[:50]
            print(f"Censé d'être 50 : {len(generation)}")

            meilleurIndividueParGeneration.append(generation[0])
    
    
            count = count + 1
            dicList.append({"parcours": generation[0].parcoursList, "distance": generation[0].distance, "generation": count})
            print(f"Generation {count} :")
            print("Parcours plus court :", generation[0].parcoursList)
            print("Distance :", generation[0].distance)
            print()
    
        meilleurIndividueParGeneration.sort(key=lambda individu: individu.distance)
        dicList.sort(key=lambda item: item["distance"])
        print()
        print(len(meilleurIndividueParGeneration))
        print(f"Meilleur individu : {dicList[0]['parcours']}")
        print(f"Distance : {dicList[0]['distance']}")
        print(f"Generation : {dicList[0]['generation']}")
        print()
        plot(meilleurIndividueParGeneration[0])
        for v in meilleurIndividueParGeneration[0].parcoursList:
            
            nb = meilleurIndividueParGeneration[0].parcoursList.count(v)
            index = meilleurIndividueParGeneration[0].parcoursList.index(v)
            
            if (index == 0 and nb == 2) or (index == 6 and nb == 2):
                continue
    
            else:
    
                if nb >= 2 and v not in doubles:
                    doubles.append(v)
                    
        print("Doublons : ", doubles)
        
        return individues
    
    
    elif(nbVilles == 10):
        
        while count < nbGenerations:
                
            individues = croisementOOP10(generation)
            #individues.sort(key=lambda individu: individu.distance, reverse=True)
            
            individues = mutation(individues)
            #individues.sort(key=lambda individu: individu.distance)
            
            generation.extend(individues)
            
            generation.sort(key=lambda individu: individu.distance)
            print(f"Censé d'être 100 : {len(generation)}")
            generation = generation[:50]
            print(f"Censé d'être 50 : {len(generation)}")
            meilleurIndividueParGeneration.append(generation[0])
    
    
            count = count + 1
            dicList.append({"parcours": generation[0].parcoursList, "distance": generation[0].distance, "generation": count})
            print(f"Generation {count} :")
            print("Parcours plus court :", generation[0].parcoursList)
            print("Distance :", generation[0].distance)
    
        meilleurIndividueParGeneration.sort(key=lambda individu: individu.distance)
        dicList.sort(key=lambda item: item["distance"])
        print()
        print(len(meilleurIndividueParGeneration))
        print(f"Meilleur individu : {dicList[0]['parcours']}")
        print(f"Distance : {dicList[0]['distance']}")
        print(f"Generation : {dicList[0]['generation']}")
        print()
            
        plot(meilleurIndividueParGeneration[0])
    
        for v in meilleurIndividueParGeneration[0].parcoursList:
            
            nb = meilleurIndividueParGeneration[0].parcoursList.count(v)
            index = meilleurIndividueParGeneration[0].parcoursList.index(v)
            
            if (index == 0 and nb == 2) or (index == 10 and nb == 2):
                continue
    
            else:
    
                if nb >= 2 and v not in doubles:
                    doubles.append(v)
                    
        print("Doublons : ", doubles)
        
        return individues
    
    
    
    elif(nbVilles == 20):
        
        while count < nbGenerations:
                
            individues = croisementOOP20(generation)
            #individues.sort(key=lambda individu: individu.distance, reverse=True)
            
            individues = mutation(individues)
            individues.sort(key=lambda individu: individu.distance)
            
            generation.extend(individues)
            generation.sort(key=lambda individu: individu.distance)
            generation = generation[:50]
            meilleurIndividueParGeneration.append(generation[0])
    
    
            count = count + 1
            dicList.append({"parcours": generation[0].parcoursList, "distance": generation[0].distance, "generation": count})
            print(f"Generation {count} :")
            print("Parcours plus court :", generation[0].parcoursList)
            print("Distance :", generation[0].distance)
    
        meilleurIndividueParGeneration.sort(key=lambda individu: individu.distance)
        dicList.sort(key=lambda item: item["distance"])
        print()
        print(len(meilleurIndividueParGeneration))
        print(f"Meilleur individu : {dicList[0]['parcours']}")
        print(f"Distance : {dicList[0]['distance']}")
        print(f"Generation : {dicList[0]['generation']}")
        print()
        plot(meilleurIndividueParGeneration[0])
    
        for v in meilleurIndividueParGeneration[0].parcoursList:
            
            nb = meilleurIndividueParGeneration[0].parcoursList.count(v)
            index = meilleurIndividueParGeneration[0].parcoursList.index(v)
            
            if (index == 0 and nb == 2) or (index == 20 and nb == 2):
                continue
    
            else:
    
                if nb >= 2 and v not in doubles:
                    doubles.append(v)
                    
        print("Doublons : ", doubles)
        
        return individues
    
    
    
    elif(nbVilles == 100):
        
        while count < nbGenerations:
                
            individues = croisementOOP100(generation)
            #individues.sort(key=lambda individu: individu.distance, reverse=True)
            
            individues = mutation(individues)
            individues.sort(key=lambda individu: individu.distance)
            
            generation.extend(individues)
            generation.sort(key=lambda individu: individu.distance)
            print(f"Censé d'être 100 : {len(generation)}")
            generation = generation[:50]
            print(f"Censé d'être 50 : {len(generation)}")
            meilleurIndividueParGeneration.append(generation[0])
    
            count = count + 1
            dicList.append({"parcours": generation[0].parcoursList, "distance": generation[0].distance, "generation": count})
            print(f"Generation {count} :")
            print("Parcours plus court :", generation[0].parcoursList)
            print("Distance :", generation[0].distance)
    
        meilleurIndividueParGeneration.sort(key=lambda individu: individu.distance)
        dicList.sort(key=lambda item: item["distance"])
        print()
        print(len(meilleurIndividueParGeneration))
        print(f"Meilleur individu : {dicList[0]['parcours']}")
        print(f"Distance : {dicList[0]['distance']}")
        print(f"Generation : {dicList[0]['generation']}")
        print()
        for individu in generation:
            print(individu.parcoursList)
        plot(meilleurIndividueParGeneration[0])
    
        for v in meilleurIndividueParGeneration[0].parcoursList:
            
            nb = meilleurIndividueParGeneration[0].parcoursList.count(v)
            index = meilleurIndividueParGeneration[0].parcoursList.index(v)
            
            if (index == 0 and nb == 2) or (index == 100 and nb == 2):
                continue
    
            else:
    
                if nb >= 2 and v not in doubles:
                    doubles.append(v)
                    
        print("Doublons : ", doubles)
        
        return individues
        
    
    
    elif(nbVilles == 250):
        
        while count < nbGenerations:
                
            individues = croisementOOP100(generation)
            #individues.sort(key=lambda individu: individu.distance, reverse=True)
            
            individues = mutation(individues)
            individues.sort(key=lambda individu: individu.distance)
            
            generation.extend(individues)
            generation.sort(key=lambda individu: individu.distance)
            print(f"Censé d'être 100 : {len(generation)}")
            generation = generation[:50]
            print(f"Censé d'être 50 : {len(generation)}")
            
            meilleurIndividueParGeneration.append(generation[0])
    
            count = count + 1
            dicList.append({"parcours": generation[0].parcoursList, "distance": generation[0].distance, "generation": count})
            print(f"Generation {count} :")
            print("Parcours plus court :", generation[0].parcoursList)
            print("Distance :", generation[0].distance)
    
        meilleurIndividueParGeneration.sort(key=lambda individu: individu.distance)
        dicList.sort(key=lambda item: item["distance"])
        print()
        print(len(meilleurIndividueParGeneration))
        print(f"Meilleur individu : {dicList[0]['parcours']}")
        print(f"Distance : {dicList[0]['distance']}")
        print(f"Generation : {dicList[0]['generation']}")
        print()
        for individu in generation:
            print(individu.parcoursList)
        plot(meilleurIndividueParGeneration[0])
    
        for v in meilleurIndividueParGeneration[0].parcoursList:
            
            nb = meilleurIndividueParGeneration[0].parcoursList.count(v)
            index = meilleurIndividueParGeneration[0].parcoursList.index(v)
            
            if (index == 0 and nb == 2) or (index == 250 and nb == 2):
                continue
    
            else:
    
                if nb >= 2 and v not in doubles:
                    doubles.append(v)
                    
        print("Doublons : ", doubles)
        
        return individues
    
    

