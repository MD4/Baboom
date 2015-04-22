__author__ = 'alexandredouchin'

import physics

class Evaluation:

    physics = physics.Physics()

    def evaluationViabilite(self, alpha, beta, Lb, Lr, mp, mc, mb):
        #alpha = 180
        #beta = 122
        #Lb = 18
        #Lr = 20
        #mp = 100
        g = 9.81
        #mc = 1800
        #mb = 200
        F = physics.tractionForce(mc, mp, alpha, beta, g)
        M = physics.momentum(F, Lb)
        I = physics.inertia(mb, Lb)
        a = physics.accelerationAngUni(M, I)
        V = physics.velocity(a, Lb)
        d = physics.portee(V, g, alpha)
        Ec = physics.enerImpact(mp, V)
        EnergieTNT = physics.energietnt(Ec)
        viableConstruct = physics.constructViable(alpha, Lb, Lr, mp, g, mc)
        if viableConstruct:
            print "true"
            print "Force de traction (N) : "
            print F
            print "Moment de bras (N.m) "
            print M
            print "Moment d'inertie du bras (kg/m^2) "
            print I
            print "Acceleration angulaire (rad/s^2) "
            print a
            print "Velocite (m/s) "
            print V
            print "Portee ( m/s) "
            print d
            print "Energie impact (Joules) "
            print Ec
            print "Equivalence Joule / gramme "
            print EnergieTNT

        else:
            print "false"

    return Ec