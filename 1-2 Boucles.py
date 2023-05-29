# Écrire une boucle while qui compte jusqu'à 100. Idem avec une boucle for.

count = 0

while count <= 100:
    print(count)
    count += 1

for i in range(101):
    print(i)

# À l'aide de boucles imbriquées, dessiner des figures géométriques : triangles et carrés, creux ou non.
# Idem à l'aide de procédures et de leurs paramètres.

import turtle

# Carré
for i in range(4):
    turtle.forward(100)
    turtle.left(90)


# Triangle
'''
for i in range(3):
    turtle.forward(100)
    turtle.left(120)
'''
