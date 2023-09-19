import Functions as fc

villes = fc.creer_villes()
individues = fc.creer_individues(villes)
individuesStr= [str(individue) for individue in individues]
distances = fc.calculer_distances(individues)
#creation d'un dictionnaire comprehension ou la cle est l'individu et la valeur est la distance
dictIndivDist = {individue:distance for (individue, distance) in zip(individuesStr, distances)}
#on tri le dictionnaire par ordre croissant de distance
dictIndivDist = dict(sorted(dictIndivDist.items(), key=lambda item: item[1]))
dic50 = fc.dictionnaire50(dictIndivDist)

print(villes)
print(individues)
print(distances)
print(dictIndivDist)
print(dic50)
print(len(dic50))


