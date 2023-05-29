# Implémenter une fonction de recherched'un élément utilisant une boucle tant queet tirant parti du fait
# que les éléments sont ordonnés.

tableau = [1, 4, 8, 13, 25, 41]

def search_element(tableau, element):
    count = 0
    while count <= len(tableau) - 1:
        if tableau[count] == element:
            return count
        elif tableau[len(tableau) - 1] == element:
            return len(tableau) - 1
        else:
            count += 1

    return -1

search = 41

indice = search_element(tableau, search)

print(indice)

# Écrire une fonction de recherche dichotomique.

tableau_dicho = [2, 7, 9, 13, 18, 24, 35, 84]
def recherche_dichotomique(tab, element):
    start = 0
    end = len(tab) - 1

    while start <= end:
        middle = (start + end) // 2
        if tab[middle] == element:
            return middle
        elif tab[middle] < element:
            start = middle + 1
        else:
            end = middle - 1

    return - 1

search_dicho = 18

indice_dicho = recherche_dichotomique(tableau_dicho, search_dicho)

print(indice_dicho)

# Proposer une procédure insertion(e,t,n)qui ajoute un élément eà sa place dans un tableau tde taille n.

tableau_insertion = [1, 5, 7, 12, 15]

def insertion(e, t, n):
    i = n - 1

    while i >= 0 and t[i] > e:
        t[i + 1] = t[i]
        i -= 1

    t[i + 1] = e

insertion_element = 9
taille = 5

insertion(insertion_element, tableau_insertion, taille)

print("Nouveau tableau_insertion :", tableau_insertion)




