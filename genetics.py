# coding=utf-8
import math

__author__ = 'md4'

import random

'''
    Classe permettant l'utilisation d'un algorithme génétique
    => générique donc indépendant de tout contexte
'''
class Genetics:
    # Fonction d'évaluation d'un individu
    evaluation_fn = None
    # Fonction de 'naissance' d'un individu (supposée aléatoire)
    birth_fn = None
    # Nombre initial d'individus
    population_size = 10

    #Constructeur
    def __init__(self, evaluation_fn, birth_fn, population_size):
        self.evaluation_fn = evaluation_fn
        self.birth_fn = birth_fn
        self.population_size = population_size

    # Fait naitre les individus de la population initiale
    def populate(self):
        return [self.birth_fn() for x in range(0, self.population_size)]

    # Condition d'arrêt de l'algorithme (ici : il ne reste qu'un individu)
    def stop_processing(self, population):
        return len(population) > 1

    # Retourne l'évaluation de chaque individu d'une population donnée
    def evaluate_population(self, population):
        return [{
                    'index': x,
                    'grade': self.evaluation_fn(population[x])
                }
                for x in range(0, len(population))]

    # Permet de choisir un individu parmi la population de façon biaisée (par son évaluation)
    def pick_one(self, population, evaluations):
        def add_grade(x, y):
            return x + y['grade']

        grades_sum = reduce(add_grade, evaluations, 0)
        pick = int(round(random.random() * grades_sum))

        def pick_random_index():
            current_grade_sum = 0
            for evaluation in evaluations:
                current_grade_sum += evaluation['grade']
                if current_grade_sum >= pick:
                    return evaluation['index']
            return -1

        random_index = pick_random_index()

        return population[random_index]

    # Permet de construire des couples parmi une population donnée (suivant leur évaluation)
    def build_cuples(self, population, evaluations):
        return [[
                    self.pick_one(population, evaluations),
                    self.pick_one(population, evaluations)
                ]
                for x in range(0, int(math.floor(len(population) / 2)))]

    # Croise deux individus d'un couple
    def crossbreed(self, cuple):
        return [cuple[int(round(random.random()))][x] for x in range(0, len(cuple[0]))]

        # slice = int(1 + math.floor(random.random() * (len(cuple[0]) - 1)))
        # return cuple[0][0:slice] + cuple[1][slice:]

    # Retourne le minimum local des évaluations d'une population donnée
    def getMean(self, evaluations):
        sum = 0.0
        for evaluation in evaluations:
            sum += evaluation['grade']
        return sum / len(evaluations)

    # Retourne la variance pour des évaluations d'une population donnée
    def getVariance(self, evaluations):
        mean = self.getMean(evaluations)
        temp = 0
        for evaluation in evaluations:
            temp += (mean - evaluation['grade']) * (mean - evaluation['grade'])
        return temp / len(evaluations)


    # Boucle principale de l'algorithme génétique
    def process(self):
        population = self.populate()
        while self.stop_processing(population):
            print(str(len(population)) + " remaining")

            evaluations = self.evaluate_population(population)
            cuples = self.build_cuples(population, evaluations)

            print("Variance : " + str(self.getVariance(evaluations)))

            population = map(self.crossbreed, cuples)

        return population[0]
