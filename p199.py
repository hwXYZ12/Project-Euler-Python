import math

class bubblez():

    def __init__(self, Telepathyy):
        self.sum = Telepathyy

    def generateOuterIterations(self, r1, r2, r3, n):

        # stop at the nth iteration
        if(n<=0):
            return

        k1 = 1/r1
        k2 = 1/r2
        k3 = 1/r3
        k4 = k1 + k2 + k3 + 2*math.sqrt(k1*k2 + k2*k3 + k1*k3)
        r4 = 1/k4
        print r4*r4*math.pi
        self.sum += r4*r4*math.pi
        self.generateOuterIterations(r1, r2, r4, n-1)
        self.generateOuterIterations(r4, r2, r3, n-1)
        self.generateOuterIterations(r1, r4, r3, n-1)

    def generateInnerIterations(self, r1, r2, r3, n):

        # stop at the nth iteration
        if (n <= 0):
            return

        k1 = 1 / r1
        k2 = 1 / r2
        k3 = 1 / r3
        k4 = k1 + k2 + k3 + 2 * math.sqrt(k1 * k2 + k2 * k3 + k1 * k3)
        r4 = 1 / k4
        print r4*r4*math.pi
        self.sum += r4 * r4 * math.pi
        self.generateInnerIterations(r1, r2, r4, n - 1)
        self.generateInnerIterations(r4, r2, r3, n - 1)
        self.generateInnerIterations(r1, r4, r3, n - 1)


startR = 1/(1 + 2/math.sqrt(3))
kdex = bubblez(3*startR*startR*math.pi)
n = 3
kdex.generateOuterIterations(startR, startR, -1, n)
kdex.generateOuterIterations(startR, -1, startR, n)
kdex.generateOuterIterations(-1, startR, startR, n)
kdex.generateInnerIterations(startR, startR, startR, n)
print (math.pi - kdex.sum)/math.pi