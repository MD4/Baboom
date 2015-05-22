# coding=utf-8
__author__ = 'md4'

import genetics
import physics
import math
import random

PI = 3.141592654

physics = physics.Physics()

# Fonction de naissance de nos individus
def birth_fn():
    return [
        int(math.floor(random.random() * 150) + 1),     # Lb la longueur du bras en metres
        random.random() * (PI / 2.0),                   # alpha la hauteur de la butee en degres
        random.random() * (PI / 2.0),                   # beta l'angle de la force de traction avec le bras en degres
        int(math.floor(random.random() * 50000) + 1),   # mc la masse du contrepoids en kilos
        int(math.floor(random.random() * 500) + 1),     # mp la masse du projectile en kilos
        int(math.floor(random.random() * 500) + 10)      # Lr la longueur de la base en metres
    ]

# Fonction d'évaluation de nos individus
def evaluate(individual):
    wished = 300
    obtained = physics.evaluatePortee(individual[0], individual[1], individual[2], individual[3], individual[4])
    viable = physics.constructViable(individual[1], individual[0], individual[5], individual[4], 9.81, individual[3])
    energy = physics.evaluateEnergy(individual[0], individual[1], individual[2], individual[3], individual[4])

    result = 1.0 / (distance(wished, obtained) + (1 / -energy))

    if not viable:
        result /= 2

    return result


def distance(a, b):
    return abs(a - b)

    # Lb la longueur du bras en metres
    # alpha la hauteur de la butee en degres
    # beta l'angle de la force de traction avec le bras en degres
    # mc la masse du contrepoids en kilos
    # mp la masse du projectile en kilos
    # Lr la longueur de la base en metres

# On donne une population initiale de 3000 individus
genetics = genetics.Genetics(evaluate, birth_fn, 3000)

# Et hop ! Baboom !
result = genetics.process()

portee = physics.evaluatePortee(result[0], result[1], result[2], result[3], result[4])
viable = physics.constructViable(result[1], result[0], result[5], result[4], 9.81, result[3])
energy = physics.evaluateEnergy(result[0], result[1], result[2], result[3], result[4])

print("Individu : ", result)
print("Viabilite : ", viable)
print("Portee : ", portee, "m")
print("Portee : ", portee / 1000, "km")
print("Energie d'impact : ", energy, "gTNT")
print("Energie d'impact : ", energy / 1000, "kgTNT")

#print(physics.evaluatePortee(12, 30, 60, 15000, 150))