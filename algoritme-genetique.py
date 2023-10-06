import random
import matplotlib as plt
import Functions as fc

# Creation des villes et les 100 premiers individues
villes = fc.creer_villes()
individues, individuesStr = fc.creer_individues(villes)

# Calcul des dictances des 100 premiers parcours
distances = fc.calculer_distances(individues)
#print("Nombre de distances des premiers individues", len(distances))



#individuesStr = fc.faireListStrings()

# Creation d'un dictionnaire comprehension ou la cle est l'individu et la valeur est la distance
dictIndivDist = {individue: distance for (individue, distance) in zip(individuesStr, distances)}

# On tri le dictionnaire par ordre croissant de distance
dictIndivDist = dict(sorted(dictIndivDist.items(), key=lambda item: item[1]))

# On prend les 50 meilleurs individues (parcours)

dic50 = fc.dictionnaire50(dictIndivDist)


# On crée la premiere generation
generation1, generation1Int = fc.croisement(dic50)

# On calcule les distances de la premiere generation
ListDistancesGen1 = fc.calculer_distances(generation1Int)
#print(ListDistancesGen1)
#print("Nombre de distances generation 1: ", len(ListDistancesGen1))

distanceOptimale = min(ListDistancesGen1)
print(distanceOptimale)

index = ListDistancesGen1.index(distanceOptimale)
print(index)

cheminPlusCourt = generation1[index]
print(cheminPlusCourt)

#dictIndivDistGen1 = {individue: distance for (individue, distance) in ()}

#print("Nombre d'instances dans le dictionnaire", len(dictIndivDistGen1))

# Tri de la liste par ordre croisant
# dictIndivDistGen1 = dict(sorted(dictIndivDistGen1.items(), key=lambda item: item[1]))

# affichage graphique avec l'import matplotlib de la premiere distance du dictionnaire DictIndivdistancesGen1 dans la console

# affichage des croisement de 2 individues

fc.plot(cheminPlusCourt, distanceOptimale)














