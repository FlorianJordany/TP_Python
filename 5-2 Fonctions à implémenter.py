#from PyGnuplot import gp
from pygnuplot import gnuplot


#Écrire une fonction copie(t)qui renvoie un nouveau tableau contenant dans le même ordre les mêmes valeurs que le
# tableau t; vérifier qu'une modification de la copie n'altère pas le tableau original.

def copie(t):
    copie_t = t.copy()
    return copie_t

tab = [2, 5, 9, 13, 18]
copie_tab = copie(tab)

print("Tab :", tab)
print("Copie_tab :", copie_tab)
print(30*"*")

#Proposer une fonction inverse(t)qui fournit un nouveau tableau contenant les mêmes valeurs que le tableau t mais
# dans l'ordre inverse.
def inverse(t):
    inverse_t = t[::-1]
    return inverse_t

inverse_tab = inverse(tab)

print("Tab :", tab)
print("Inverse_tab :", inverse_tab)
print(30*"*")

# Implémenter des fonctions pour produire des tableaux : oUnefonction tableau_premiers_entiers(n)qui produit un
# tableau contenant dans l'ordre tous les entiers de 1 à n, oUnefonction tableau_premiers_entiers_melanges(n)qui
# propose ces mêmes entiers mélangés aléaoirement,
# oUnefonction tableau_premiers_entiers_inverses(n)qui propose ces mêmes entiers du plus grand au plus petit.

import random

def tableau_premiers_entiers(n):
    tableau = list(range(1, n+1))
    return tableau

def tableau_premiers_entiers_melanges(n):
    tableau = list(range(1, n+1))
    random.shuffle(tableau)
    return tableau

def tableau_premiers_entiers_inverses(n):
    tableau = list(range(n, 0, -1))
    return tableau

n = 20

tableau_entiers = tableau_premiers_entiers(n)
tableau_melange = tableau_premiers_entiers_melanges(n)
tableau_inverse = tableau_premiers_entiers_inverses(n)

print("Tableau_entiers :", tableau_entiers)
print("Tableau_melange :", tableau_melange)
print("Tableau_inverse :", tableau_inverse)
print(30*"*")

# Proposer une procédure ligne_dans_fichier(f,n,t)dont le rôle est d'écrire dans le fichier fla valeur
# (numérique) de n, une tabulation, la valeur (numérique) de tet enfin un passage à la ligne.

def ligne_dans_fichier(f, n, t):
    with open(f, 'a') as fichier:
        fichier.write(str(n) + '\t' + str(t) + '\n')

fichier = "donnees.txt"
ligne_dans_fichier(fichier, "test", 6)
ligne_dans_fichier(fichier, 15, "blabla")

# Écrire une fonction temps_tri_bulles(t)qui fait une copie du tableau tet renvoie le temps nécessaire au tri à
# bulles pour classer cette copie.

import time

def temps_tri_bulles(t):
    copie_t = t.copy()
    debut = time.time()

    n = len(copie_t)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if copie_t[j] > copie_t[j + 1]:
                copie_t[j], copie_t[j + 1] = copie_t[j + 1], copie_t[j]

    fin = time.time()
    temps = fin - debut
    return temps

tableauBulle = [5, 2, 8, 1, 9, 3]
temps = temps_tri_bulles(tableauBulle)
print("Time :", temps, "secondes")
print(30*"*")

# Coder la procédure stats_melange(nmin,nmax,pas,fois)qui pour chaque taille de tableau comprise entre nminet
# nmaxen avançant de pasen pasproduit foistableaux mélangés aléatoirement et écrit dans un fichier le temps
# moyen nécessaire au tri à bulles pour classer ces tableaux.

def stats_melange(nmin, nmax, pas, fois):
    fichier = "temps_tri_bulles.txt"
    with open(fichier, 'w') as f:
        for n in range(nmin, nmax + 1, pas):
            temps_total = 0

            for _ in range(fois):
                tableau = [random.randint(1, 100) for _ in range(n)]

                debut = time.time()

                for i in range(n - 1):
                    for j in range(n - 1 - i):
                        if tableau[j] > tableau[j + 1]:
                            tableau[j], tableau[j + 1] = tableau[j + 1], tableau[j]

                fin = time.time()
                temps = fin - debut
                temps_total += temps

            temps_moyen = temps_total / fois
            f.write(f"Taille du tableau: {n} Temps moyen de tri à bulles: {temps_moyen}\n")

    print("Fichier :", fichier)

stats_melange(10, 100, 10, 5)
print(30*"*")

# Même question avec la fonction stats_ordonne(nmin,nmax,pas,fois)pour des tableaux déjà ordonnés.

def stats_ordonne(nmin, nmax, pas, fois):
    fichier = "temps_tri_bulles_ordonne.txt"
    with open(fichier, 'w') as f:
        for n in range(nmin, nmax + 1, pas):
            temps_total = 0

            for _ in range(fois):
                tableau = list(range(1, n + 1))

                debut = time.time()

                for i in range(n - 1):
                    for j in range(n - 1 - i):
                        if tableau[j] > tableau[j + 1]:
                            tableau[j], tableau[j + 1] = tableau[j + 1], tableau[j]

                fin = time.time()
                temps = fin - debut
                temps_total += temps

            temps_moyen = temps_total / fois
            f.write(f"Taille du tableau: {n} - Temps moyen de tri à bulles: {temps_moyen}\n")

    print("Fichier :", fichier)

stats_ordonne(10, 100, 10, 5)
print(30*"*")

# Même question avec la fonction stats_inverse(nmin,nmax,pas,fois)pour des tableaux déjà ordonnés mais
# en ordre inverse.

def stats_inverse(nmin, nmax, pas, fois):
    fichier = "temps_tri_bulles_inverse.txt"
    with open(fichier, 'w') as f:
        for n in range(nmin, nmax + 1, pas):
            temps_total = 0

            for _ in range(fois):
                tableau = list(range(n, 0, -1))

                debut = time.time()

                for i in range(n - 1):
                    for j in range(n - 1 - i):
                        if tableau[j] > tableau[j + 1]:
                            tableau[j], tableau[j + 1] = tableau[j + 1], tableau[j]

                fin = time.time()
                temps = fin - debut
                temps_total += temps

            temps_moyen = temps_total / fois
            f.write(f"Taille du tableau: {n} - Temps moyen de tri à bulles: {temps_moyen}\n")

    print("Fichier : ", fichier)

stats_inverse(10, 100, 10, 5)
print(30 * "*")

# Produire à l'aide de votre code des fichiers de statistiques pour des tailles de tableau variant de 100 en 100,
# entre 100 et 1000, avec 5répétitions pour chaque taille de tableau. Visualiser ces données avec gnuplotet comparer
# l'évolution du temps nécessaire au tri bulles selon le type de tableaux et selon leurs tailles.

stats_melange(100, 1000, 100, 5)
stats_ordonne(100, 1000, 100, 5)
stats_inverse(100, 1000, 100, 5)


