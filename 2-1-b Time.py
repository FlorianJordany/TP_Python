# Fournit un tableau de n entiers aléatoires

import random

tab_random = []
for i in range(10):
    tab_random.append(random.randint(1, 100))

print(tab_random)

# Construit le tableau des n premiers entiers mélangés aléatoirement

tab_short = tab_random[0:5]
random.shuffle(tab_short)

print(tab_short)

# Sur des grands tableaux, mesurer le temps nécessaire à chacune des fonctions calculant
# la moyenne et recherchant un élément.

import time

tableau = []
for i in range(10000):
    tableau.append(random.randint(1, 100))

def calc_moyenne(tableau):
    return sum(tableau) / len(tableau)

def search_element(tableau, element):
    return element in tableau

start_moyenne = time.time()
moyenne = calc_moyenne(tableau)
end_moyenne = time.time()
temps_execution_moyenne = end_moyenne - start_moyenne

print(temps_execution_moyenne, "secondes.")

start_search = time.time()
search = search_element(tableau, random.randint(1, 100))
end_search = time.time()
temps_execution_search = end_search - start_search

print(temps_execution_search, "secondes.")