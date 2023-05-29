# Définir en Python un tableau d'entiers.

tab = [2, 7, 16, 25, 37, 58, 71, 89, 92]

# Calcule la moyenne des nombres contenus dans un tableau donné

moyenne = sum(tab) / len(tab)
print(moyenne)

# Compte le nombre d'occurrences d'un élément

element = 37
print(tab.count(element))

# Compte combien d'éléments sont supérieurs ou égaux à 10

count_10 = 0
for element in tab:
    if element > 10:
        count_10 += 1

print(count_10)

# Recherche la valeur maximale du tableau

print(max(tab))

# Teste si un élément est présent ou non, etc

search_element = 88

if search_element in tab:
    print(search_element, "est présent dans le tableau.")
else:
    print(search_element, "n'est pas présent dans le tableau.")

