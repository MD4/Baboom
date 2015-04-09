__author__ = 'md4'

import math

class Physics:

    def tractionForce(self, mc, mp, alpha, beta, g):
        return (mc * g) * math.sin(beta) - (mp * g) * math.cos(alpha)

    def momentum(self, F, L):
        return F * L

    def inertia(self, mb, L):
        return (mb * (L ^ 2)) / 3

    def velocity(self, a, L):
        return a * L

