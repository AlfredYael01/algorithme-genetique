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
generation1 = fc.croisementOOP50(listIndividues50)
generation1.sort(key=lambda individu: individu.distance)

print("Parcours plus court première generation: ", generation1[0].parcoursList)

# Cherche pour des doublons
doubles = []
parcours1 = generation1[0].parcoursList

for f1 in parcours1:

    nb = parcours1.count(f1)
    index = parcours1.index(f1)

    if (index == 0 and nb == 2) or (index == 6 and nb == 2):
        continue

    else:

        if nb >= 2 and f1 not in doubles:
            doubles.append(f1)

print("Doublons: ", doubles)
print("Distance : ", generation1[0].distance)
print("Nb generation1: ", len(generation1))
print()

# mutation
generation1Mutation = fc.mutation(generation1)
generation1Mutation.sort(key=lambda individu: individu.distance)



# Selection de 24 individues avec les distances le plus courtes
listIndividues24 = [individu for individu in generation1Mutation[:24]]


# Creation de la generation 2 et tri part distance croissante
generation2 = fc.croisementOOP24(listIndividues24)
generation2.sort(key=lambda individu: individu.distance)


print("Parcours plus court deuxième generation: ", generation2[0].parcoursList)

# Cherche pour des doublons
doubles = []
parcours1 = generation2[0].parcoursList

for f1 in parcours1:

    nb = parcours1.count(f1)
    index = parcours1.index(f1)

    if (index == 0 and nb == 2) or (index == 6 and nb == 2):
        continue

    else:

        if nb >= 2 and f1 not in doubles:
            doubles.append(f1)

print("Doublons: ", doubles)
print("Distance : ", generation2[0].distance)
print("Nb generation2: ", len(generation2))
print()

# mutation
generation2Mutation = fc.mutation(generation2)
generation2Mutation.sort(key=lambda individu: individu.distance)


# Selection de 12 individues avec les distances le plus courtes
listIndividues12 = [individu for individu in generation2Mutation[:12]]


# Creation de la generation 2 et tri part distance croissante
generation3 = fc.croisementOOP12(listIndividues12)
generation3.sort(key=lambda individu: individu.distance)


print("Parcours plus court troisième generation: ", generation3[0].parcoursList)

# Cherche pour des doublons
doubles = []
parcours1 = generation3[0].parcoursList

for f1 in parcours1:

    nb = parcours1.count(f1)
    index = parcours1.index(f1)

    if (index == 0 and nb == 2) or (index == 6 and nb == 2):
        continue

    else:

        if nb >= 2 and f1 not in doubles:
            doubles.append(f1)

print("Doublons: ", doubles)
print("Distance : ", generation3[0].distance)
print("Nb generation3: ", len(generation3))
print()

# mutation
generation3Mutation = fc.mutation(generation3)
generation3Mutation.sort(key=lambda individu: individu.distance)




# Selection de 6 individues avec les distances le plus courtes
listIndividues6 = [individu for individu in generation3Mutation[:6]]


# Creation de la generation 4 et tri part distance croissante
generation4 = fc.croisementOOP6(listIndividues6)
generation4.sort(key=lambda individu: individu.distance)


print("Parcours plus court quatrième generation: ", generation4[0].parcoursList)

# Cherche pour des doublons
doubles = []
parcours1 = generation2[0].parcoursList

for f1 in parcours1:

    nb = parcours1.count(f1)
    index = parcours1.index(f1)

    if (index == 0 and nb == 2) or (index == 6 and nb == 2):
        continue

    else:

        if nb >= 2 and f1 not in doubles:
            doubles.append(f1)

print("Doublons: ", doubles)
print("Distance : ", generation4[0].distance)
print("Nb generation4: ", len(generation4))
print()

# mutation
generation4Mutation = fc.mutation(generation4)
generation4Mutation.sort(key=lambda individu: individu.distance)




# Selection de 6 individues avec les distances le plus courtes
listIndividues2 = [individu for individu in generation4Mutation[:2]]


# Creation de la generation 4 et tri part distance croissante
generation5 = fc.croisementOOP2(listIndividues2)
generation5.sort(key=lambda individu: individu.distance)


print("Parcours plus court cinquième generation: ", generation5[0].parcoursList)

# Cherche pour des doublons
doubles = []
parcours1 = generation5[0].parcoursList

for f1 in parcours1:

    nb = parcours1.count(f1)
    index = parcours1.index(f1)

    if (index == 0 and nb == 2) or (index == 6 and nb == 2):
        continue

    else:

        if nb >= 2 and f1 not in doubles:
            doubles.append(f1)

print("Doublons: ", doubles)
print("Distance : ", generation5[0].distance)
print("Nb generation4: ", len(generation5))
print()


# mutation
generation5Mutation = fc.mutation(generation5)
generation5Mutation.sort(key=lambda individu: individu.distance)



# Plot
generation5Mutation[0].plot()
print("Parcours plus court :", generation5Mutation[0].parcoursList)
print("Distance : ", generation5Mutation[0].distance)

