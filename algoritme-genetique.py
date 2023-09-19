import random
import Functions as fc

villes = fc.creer_villes()
individues = fc.creer_individues(villes)
distances = fc.calculer_distances(individues)

individuesStr = []
invStr = ''

for individue in individues:

    for l in individue:
        invStr += str(l)

    individuesStr.append(invStr)
    invStr = ''

#creation d'un dictionnaire comprehension ou la cle est l'individu et la valeur est la distance
dictIndivDist = {individue: distance for (individue, distance) in zip(individuesStr, distances)}

#on tri le 50dictionnaire par ordre croissant de distance
dictIndivDist = dict(sorted(dictIndivDist.items(), key=lambda item: item[1]))
dic50 = fc.dictionnaire50(dictIndivDist)

# On crée la premiere generation
generation1 = fc.croisement(dic50)



#affichage des croisement de 2 individues



















