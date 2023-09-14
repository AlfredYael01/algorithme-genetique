import Functions as fc

villes = fc.creer_villes()
individues = fc.creation_individues(villes)
distances = fc.calculer_distances(individues)

print(villes)
print(individues)
print(distances)



