# Créer une liste vide. Créer une liste contenant des éléments.

liste_vide = []
liste = [1, 2, 3]

# Afficher la longueur de cette liste.

print(len(liste))

# Remplacer l'une des valeurs, enlever une case et en ajouter une autre, puis afficher à nouveau la liste.

liste[1] = 9
del liste[2]
liste.append(8)
print(liste)

# Utiliser une boucle pour parcourir les éléments de la liste et les afficher un par un.
# Passer en revue les différentes syntaxes possibles.

for element in liste:
    print(element)