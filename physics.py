__author__ = 'md4'

import math

class Physics:

    def tractionForce(self, mc, mp, alpha, beta, g):
        return (mc * g) * math.sin(beta) - (mp * g) * math.cos(alpha)

    def momentum(self, F, L):
        return F * L

    def inertia(self, mb, L):
        return (mb * (L**2)) / 3

    def accelerationAngUni(self, M, I):
        return M / I

    def velocity(self, a, L):
        return a * L

    def portee(self, V, g, alpha):
        return (V**2 / g) * math.sin(2 * (90 - alpha))

    def enerImpact(self, mp, V):
        return (1 / 2) * mp * V**2

    def constructViable(self, alpha, Lb, Lr, mp, g, mc):
        return ((math.sin(alpha) * Lb)**2 + (math.cos(alpha)*Lb - Lr)**2 ) * math.sin(alpha)*(mp * g) <= Lr * (mc * g)

    def energietnt(self, energiejoule):
        return energiejoule / 4184

    # alpha la hauteur de la butee en degres
    # Lb la longueur du bras en metres
    # mb la masse du bras en kilos
    # beta l'angle de la force de traction avec le bras en degres
    # mc la masse du contrepoids en kilos
    # mp la masse du projectile en kilos
    # Lr la longueur de la base en metres
    # g = 9,81m.s^2 sur terre 1,62m.s^2 sur la lune 24,80m.s^2 sur jupiter