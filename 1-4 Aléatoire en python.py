# Tester les fonctions de la librairie random suivantes :
# random.randint, random.randrange, random.choice, random.shuffle.

import random

print(random.randint(1, 50))

print(random.randrange(0, 50, 2))

liste_choice=[1, 2, 3]
print(random.choice(liste_choice))

liste_shuffle=[1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(liste_shuffle)
print(liste_shuffle)
