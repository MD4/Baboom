__author__ = 'md4'

import genetics
import physics
import math
import random

physics = physics.Physics()

def birth_fn():
    return [
        int(math.floor(random.random() * 150) + 1),  # Lb la longueur du bras en metres
        int(math.floor(random.random() * 90)),  # alpha la hauteur de la butee en degres
        int(math.floor(random.random() * 90)),  # beta l'angle de la force de traction avec le bras en degres
        int(math.floor(random.random() * 20000) + 1),  # mc la masse du contrepoids en kilos
        int(math.floor(random.random() * 200) + 1),  # mp la masse du projectile en kilos
        int(math.floor(random.random() * 200) + 1)  # Lr la longueur de la base en metres
    ]


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


genetics = genetics.Genetics(evaluate, birth_fn, 10000)

result = genetics.process()

portee = physics.evaluatePortee(result[0], result[1], result[2], result[3], result[4])
viable = physics.constructViable(result[1], result[0], result[5], result[4], 9.81, result[3])
energy = physics.evaluateEnergy(result[0], result[1], result[2], result[3], result[4])

print("Individu : ", result)
print("Viabilite : ", viable)
print("Portee : ", portee, "m")
print("Energie d'impact : ", energy, "gTNT")
print("Energie d'impact : ", energy / 1000, "tTNT")

#print(physics.evaluatePortee(12, 30, 60, 15000, 150))