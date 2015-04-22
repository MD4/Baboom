__author__ = 'md4'

import math


class Physics:
    def tractionForce(self, mc, mp, alpha, beta, g):
        return (mc * g) * math.sin(beta) - (mp * g) * math.cos(alpha)

    def momentum(self, F, L):
        return F * L

    def inertia(self, mb, L):
        return (mb * (L ** 2)) / 3

    def accelerationAngUni(self, M, I):
        return M / I

    def velocity(self, a, L):
        return a * L

    def portee(self, V, g, alpha):
        return (V ** 2 / g) * math.sin(2 * (90 - alpha))

    def enerImpact(self, mp, V):
        return (0.5 * mp * (V ** 2))

    def constructViable(self, alpha, Lb, Lr, mp, g, mc):
        return ((math.sin(alpha) * Lb) ** 2 + (math.cos(alpha) * Lb - Lr) ** 2 ) * math.sin(alpha) * (mp * g) <= Lr * (
            mc * g)

    def energietnt(self, energiejoule):
        return energiejoule / 4184

    def masseBras(self, Lb):
        return 30 * 30 * Lb * 0.0625  # masse volumique chene

    def evaluatePortee(self, Lb, alpha, beta, mc, mp):
        g = 9.81
        F = self.tractionForce(mc, mp, alpha, beta, g)
        M = self.momentum(F, Lb)
        mb = self.masseBras(Lb)
        I = self.inertia(mb, Lb)
        a = self.accelerationAngUni(M, I)
        V = self.velocity(a, Lb)
        return self.portee(V, g, alpha)

    def evaluateEnergy(self, Lb, alpha, beta, mc, mp):
        g = 9.81
        F = self.tractionForce(mc, mp, alpha, beta, g)
        M = self.momentum(F, Lb)
        mb = self.masseBras(Lb)
        I = self.inertia(mb, Lb)
        a = self.accelerationAngUni(M, I)
        V = self.velocity(a, Lb)
        return self.energietnt(self.enerImpact(mp, V))

    # Lb la longueur du bras en metres
    # alpha la hauteur de la butee en degres
    # beta l'angle de la force de traction avec le bras en degres
    # mc la masse du contrepoids en kilos
    # mp la masse du projectile en kilos
    # Lr la longueur de la base en metres