import math
import itertools
from PrimeGenerator import PrimeGenerator

def partition(number):
        answer = set()
        answer.add((number, ))
        for x in range(1, number):
            for y in partition(number - x):
                answer.add(tuple(sorted((x, ) + y)))
        return answer

# doesn't check inputs at all :P, warning
def isPrime(n, primes):

    if n in primes:
        return True

    for p in primes:
        if n % p == 0:
            return False

    return True

# load prime numbers from the net
primes1 = {int(x) for x in open("primes1.txt").read().split() if len(set(x)) == len(x)}
primes2 = {int(x) for x in open("primes2.txt").read().split() if len(set(x)) == len(x)}
primes3 = {int(x) for x in open("primes3.txt").read().split() if len(set(x)) == len(x)}
primes4 = {int(x) for x in open("primes4.txt").read().split() if len(set(x)) == len(x)}
primes5 = {int(x) for x in open("primes5.txt").read().split() if len(set(x)) == len(x)}
primes6 = {int(x) for x in open("primes6.txt").read().split() if len(set(x)) == len(x)}
primes = primes1 | primes2 | primes3 | primes4 | primes5 | primes6

# build a set to list dictionary that takes a set of
# digits and returns the list of relevant primes that do not
# contain those digits
primeListsDict = {}
pandigital = {i for i in xrange(1,10)}
primeToDigits = {}
primeSets = [[] for i in xrange(9)]
for p in primes:

    # get digits
    n = p
    digits = set()
    while(n!=0):
        digits.add(n % 10)
        n /= 10

    # skip primes with 9 or more digits
    # and skip primes that contain a 0
    length = len(digits)
    if length >= 9 or 0 in digits:
        continue

    # separate primes based on the number of digits
    primeSets[len(digits)].append(p)
    
    # dictionary taking a prime to it's digits so the operation
    # need only be calculated once
    primeToDigits[p] = digits

    # get digits that are not included
    notIncluded = pandigital - digits
        
    # for each subset of the digits that are not included
    # we are going to add the specific prime that we are working
    # with to the respective prime list
    for i in xrange(len(notIncluded)+1):
        for x in itertools.permutations(notIncluded, i):

            key = frozenset(x)

            # store result in dictionary
            if not key in primeListsDict:
                primeListsDict[key] = [[] for i in xrange(9)]
                                
            if p not in primeListsDict[key][length]:
                primeListsDict[key][length].append(p)

                
answer = 0

# 1,1,7
theKey = set()
for i in primeListsDict[frozenset(theKey)][1]:
    theKey.add(i)
    for j in primeListsDict[frozenset(theKey)][1]:
        if(i<j):
            theKey.add(j)
            answer += len(primeListsDict[frozenset(theKey)][7])
            print theKey
            print " : "
            print primeListsDict[frozenset(theKey)][7]
            theKey.remove(j)
    theKey.remove(i)

print answer

answer1 = 0
# 1,2,2,2,2
theKey.clear()
for i in primeListsDict[frozenset(set())][1]:
    theKey.add(i)
    frozenKey1 = frozenset(theKey)
    if(frozenKey1 in primeListsDict):
        for j in primeListsDict[frozenKey1][2]:
            theKey |= primeToDigits[j]
            frozenKey2 = frozenset(theKey)
            if(frozenKey2 in primeListsDict):
                for k in primeListsDict[frozenKey2][2]:
                    if(j<k):
                        theKey |= primeToDigits[k]                        
                        frozenKey3 = frozenset(theKey)
                        if(frozenKey3 in primeListsDict):
                            for m in primeListsDict[frozenKey3][2]:
                                if (k<m):
                                    theKey |= primeToDigits[m]
                                    frozenKey4 = frozenset(theKey)
                                    if(frozenKey4 in primeListsDict):
                                        for n in primeListsDict[frozenset(theKey)][2]:
                                            if(m<n):
                                                # debug code
                                                theKey |= primeToDigits[n]                                                
                                                answer1 += 1
                                                print str(i)+str(j)+str(k)+str(m)+str(n)
                                                theKey -= primeToDigits[n]
                                    theKey -= primeToDigits[m]
                        theKey -= primeToDigits[k]
            theKey -= primeToDigits[j]
    theKey.remove(i)

print answer1
    
def primeListBuilder(frozenKey, digits, prev, theKey, whichPart, partition):

    # base case
    if(whichPart == len(partition) - 1):
        if(frozenKey in primeListsDict):
            newDigits = partition[whichPart]
            if(newDigits > digits):
                return len(primeListsDict[frozenKey][partition[whichPart]]) 
            else:
                ret = 0
                for x in primeListsDict[frozenKey][partition[whichPart]]:
                    if (x>prev):
                        ret += 1
                return ret
        else:
            return 0

    # recursive case
    answer = 0
    if(frozenKey in primeListsDict):
        for x in primeListsDict[frozenKey][digits]:
            if(prev<x):
                theKey |= primeToDigits[x]
                newFrozenKey = frozenset(theKey)
                answer += primeListBuilder(newFrozenKey, partition[whichPart], x, theKey, whichPart+1, partition)
                theKey -= primeToDigits[x]

    return answer
            
print primeListBuilder(frozenset([]), 1, 0, set(), 0, (1,1,7))
print primeListBuilder(frozenset([]), 1, 0, set(), 0, (1,2,2,2,2)) 

# TODO why is this counting so many extras???
    
# arbitrary p
#parts = partition(9)
#for p in parts:
#    answer +=


## setup for initial stages of the bruteforce algorithm
#primeListThatDoesNotContainTheDigitsContainedInTheKey[frozenset(set())] = [primeSets[i] for i in xrange(9)]

## generate each possible partition of the nine digits and try
## each possible combination of prime numbers from the imported list
#answer = 0
#parts = partition(9)
#for p in parts:

#    length = len(p)
#    if(length == 1 or length > 6):
#        continue

#    possiblePrimeSet = [0 for k in xrange(len(p))]
#    index = [0 for k in xrange(len(p))]
#    keepLooking = True
#    while keepLooking:
        
#        # maintain a digit set which represents the digits
#        # that we've already seen
#        alreadySeen = set()
#        for i in len(p)-1:

#            # get the number of digits for this particular section of the partition
#            digits = p[i]

#            # use the index vector to build a possible prime set
#            key = frozenset(alreadySeen)
#            primesExist1 = key in primeListThatDoesNotContainTheDigitsContainedInTheKey
#            if primesExist1:
#                primesExist2 = primeListThatDoesNotContainTheDigitsContainedInTheKey[key][digits]>0
#            else:
#                primesExist2 = False
#            primesExist = primesExist1 and primesExist2
#            if (primesExist):
#                possiblePrimeSet[i] = primeListThatDoesNotContainTheDigitsContainedInTheKey[frozenset(alreadySeen)][digits][index[i]]
#                alreadySeen |= primeToDigits[possiblePrimeSet[i]]
#            else:
#                # we have failed to complete a possible prime set and must increment the index
#                # vector accordingly
#                break

#        # ensure that the 

#        if primesExist:
#            # in this case, the search found possible prime sets and we
#            # add them to the solution
#            answer += len(primeListThatDoesNotContainTheDigitsContainedInTheKey[key][digits])
            

#        # increment index vector
#        indexToIncrement = len(index) - 2
#        while (indexToIncrement >= 0):

#            if index[indexToIncrement] < len(primeListThatDoesNotContainTheDigitsContainedInTheKey[frozenset(alreadySeen)][p[indexToIncrement]])-1:
#                index[indexToIncrement] += 1
#                break
#            else:
#                index[indexToIncrement] = 0
#                indexToIncrement -= 1

#        # stop looking once you've gone through all the
#        # possible combinations
#        if(indexToIncrement < 0):
#            keepLooking = False                                              

