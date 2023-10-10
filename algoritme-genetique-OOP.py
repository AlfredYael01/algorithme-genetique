import Functions as fc

# Creation des villes et des coordonnées
villes, villesStr = fc.creer_villes()
x, y, coordonnees, coordonneesVilles, coordonnesVillesStr = fc.creerCoordonnees(villes, villesStr)


# Creation des premiers 100 individues et tri part distance croissante
listIndividues = fc.creerIndividues(villes, villesStr, x, y, coordonnees, coordonneesVilles, coordonnesVillesStr)
listIndividues.sort(key=lambda individu: individu.distance)

print("Parcours plus court premiers individues : ", listIndividues[0].parcoursList)
print("Distance :", listIndividues[0].distance)
print("Nb individues : ", len(listIndividues))
print()

# Selection de 50 individues avec les distances le plus courtes
listIndividues50 = [individu for individu in listIndividues[:50]]


# Creation de la generation 1 et tri part distance croissante
generation1 = fc.croisementOOP(listIndividues50)
generation1.sort(key=lambda individu: individu.distance)

print("Parcours plus court première generation: ", generation1[0].parcoursList)

# Cherche pour des doublons
doubles = []
parcours1 = generation1[0].parcoursList

for f1 in parcours1:

    nb = parcours1.count(f1)
    index = parcours1.index(f1)

    if (index == 0 and nb == 2) or (index == 10 and nb == 2):
        continue

    else:

        if nb >= 2 and f1 not in doubles:
            doubles.append(f1)

print("Doublons: ", doubles)
print("Distance : ", generation1[0].distance)
print("Nb generation1: ", len(generation1))

# Plot
generation1[0].plot()
