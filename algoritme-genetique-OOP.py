import Functions as fc
import time as time
# Creation des villes et des coordonnées

nbVilles = 250
nbGenerations = 100

t1 = time.perf_counter()
villes, villesStr = fc.creer_villes(nbVilles)

x, y, coordonnees, coordonneesVilles, coordonnesVillesStr = fc.creerCoordonnees(villes, villesStr)

# Creation des premiers 100 individues et tri part distance croissante
listIndividues = fc.creerIndividues(villes, villesStr, x, y, coordonnees, coordonneesVilles, coordonnesVillesStr)
listIndividues.sort(key=lambda individu: individu.distance)
listIndividues = listIndividues[:50]

print("Parcours plus court premiers individues : ", listIndividues[0].parcoursList)
print("Distance :", listIndividues[0].distance)
print("Nb individues : ", len(listIndividues))
print()

# Selection de 50 individues avec les distances le plus courtes
fc.trouverCheminPlusCourt(nbGenerations, nbVilles, listIndividues)
t2 = time.perf_counter()
print(f"Temps du calcul : {t2 - t1}")
