from math import sqrt
from math import ceil
from math import log
import itertools

# import all the primes that are less than 10**5
primes = [int(j) for line in open("primes1.txt").readlines() for j in line.split() if int(j) < 10**5]

# find M(10,d) heuristically
# and simultaneously determine S(10, d)
# and finally the solution
M = {}
S = []
for d in xrange(1,10):
    numArray = [d for x in xrange(10)]
    for x in xrange(10):
        for y in xrange(10):
            if(y != d):
                # alter the string slightly
                numArray[x] = y
                # check if the string represents a prime
                check = sum([numArray[len(numArray)-i-1]*(10**i) for i in xrange(len(numArray))])
              
                isPrime = True
                for i in xrange(len(primes)):
                    p = primes[i]
                    if p > ceil(sqrt(check)):
                        break

                    if check % p == 0:
                        isPrime = False
                        break

                # reset string to it's original value
                numArray[x] = d

                if(isPrime):
                    # set M to its appropriate value
                    # and add the correct primes
                    M[d] = 9
                    S.append(check)

                    
# pretty good guess... missing 0, 2, and 8 though....

# check the d == 0, d == 2, and d == 8 cases separately
# this block is for d == 0
for x in xrange(1,10):
    for y in xrange(1,10):            
            check = x*(10**9)+y              
            isPrime = True
            for i in xrange(len(primes)):
                p = primes[i]
                if p > ceil(sqrt(check)):
                    break

                if check % p == 0:
                    isPrime = False
                    break

            if(isPrime):
                # set M to its appropriate value
                # and add the correct primes
                M[0] = 8
                S.append(check)

# the block for d == 2 or d == 8
for d in [2,8]:
    numArray = [d for x in xrange(10)]
    for i in xrange(10):
        for j in xrange(i+1,10):
            for x in xrange(10):
                for y in xrange(10):    
                    # alter the string slightly
                    numArray[i] = x
                    numArray[j] = y

                    # check if the string represents a prime
                    check = sum([numArray[len(numArray)-k-1]*(10**k) for k in xrange(len(numArray))])
                                        
                    # reset the array
                    numArray[i] = d
                    numArray[j] = d        

                    # ensure that check has at least 10 digits
                    if not ceil(log(check, 10)) == 10:
                        continue

                    isPrime = True
                    for m in xrange(len(primes)):
                        p = primes[m]
                        if p > ceil(sqrt(check)):
                            break

                        if check % p == 0:
                            isPrime = False
                            break                       

                    if(isPrime):
                        # set M to its appropriate value
                        # and add the correct primes
                        M[d] = 8
                        S.append(check)




print sum(S)