import math

__author__ = 'md4'

import random

class Genetics:
    evaluation_fn = None
    birth_fn = None
    population_size = 10

    def __init__(self, evaluation_fn, birth_fn, population_size):
        self.evaluation_fn = evaluation_fn
        self.birth_fn = birth_fn
        self.population_size = population_size

    def populate(self):
        return [self.birth_fn() for x in range(0, self.population_size)]

    def stop_processing(self, population):
        return len(population) > 1

    def evaluate_population(self, population):
        return [{
                    'index': x,
                    'grade': self.evaluation_fn(population[x])
                }
                for x in range(0, len(population))]

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

    def build_cuples(self, population, evaluations):
        return [[
                    self.pick_one(population, evaluations),
                    self.pick_one(population, evaluations)
                ]
                for x in range(0, int(math.floor(len(population) / 2)))]

    def crossbreed(self, cuple):
        return [cuple[int(round(random.random()))][x] for x in range(0, len(cuple[0]))]

        #slice = int(1 + math.floor(random.random() * (len(cuple[0]) - 1)))
        #return cuple[0][0:slice] + cuple[1][slice:]

    def process(self):
        population = self.populate()
        print(population)
        while self.stop_processing(population):
            evaluations = self.evaluate_population(population)
            cuples = self.build_cuples(population, evaluations)

            population = map(self.crossbreed, cuples)

        print(population)
