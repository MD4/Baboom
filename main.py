__author__ = 'md4'

import genetics
import math
import random

def evaluate(individual):
    def sum(a, b):
        return a + str(b)
    return int(reduce(sum, individual, ''))

def birth_fn():
    return [int(math.floor(random.random() * 10)) for x in range(0, 2)]


genetics = genetics.Genetics(evaluate, birth_fn, 2000)

genetics.process()