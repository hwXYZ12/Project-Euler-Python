import math
from itertools import *
import operator

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

primes = [2,3,5,7,11,13,17]
bigNumber = prod(primes)
bounds = [7,6,5,4,3,2,1]
#bounds = [int(round(math.log(float(bigNumber), float(x)))) for x in primes]
exponents = [0 for x in xrange(len(primes))]

ret=10**50
finished = False
while(not finished):
    incremented = False
    currentIndex = 0
    while(not incremented):
        if exponents[currentIndex] < bounds[currentIndex]:
            exponents[currentIndex] += 1
            incremented = True
        else:
            exponents[currentIndex] = 1
            currentIndex+=1
            if(currentIndex >= len(bounds)-1):
                finished = True
                break
            
    leSum = prod(p**e for (p,e) in zip(primes, exponents))
    solns = (prod(2*e+1 for e in exponents) + 1) /2
    if solns > 1000:
        if ret > leSum:
            ret = leSum
            print ret
            print exponents


print ret





