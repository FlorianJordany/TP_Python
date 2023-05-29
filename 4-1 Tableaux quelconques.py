# Implémenter une fonction index_minimum(t,d,f)qui renvoie le numéro de la case contenant la plus petite valeur du
# tableau tentre les cases det f.

tableau = [10, 5, 8, 3, 7, 2]

def index_minimum(t, d, f):
    index_min = d
    for i in range(d, f):
        if t[i] < t[index_min]:
            index_min = i
    return index_min

ind_min = index_minimum(tableau, 0, len(tableau))

print("Indice min est :", ind_min)

# Programmer un tri à bulles.

def tri_bulles(tableau):
    for i in range(len(tableau) - 1):
        for j in range(len(tableau) - i - 1):
            if tableau[j] > tableau[j + 1]:
                tableau[j], tableau[j + 1] = tableau[j + 1], tableau[j]

tri_bulles(tableau)
print("Nouveau tableau :", tableau)
