import math
import operator

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

# n is the number of total black blocks
# and m is the number of red blocks used
def redFunction(n, m):
    actualBlackBlocks = n - 2*m

    if (actualBlackBlocks < 0):
        return -1 # error

    return math.factorial(actualBlackBlocks + m)/math.factorial(actualBlackBlocks)/math.factorial(m)

# n is the number of total black blocks
# and m is the number of blue blocks used
def blueFunction(n, m):
    actualBlackBlocks = n - 3*m

    if (actualBlackBlocks < 0):
        return -1 # error

    return math.factorial(actualBlackBlocks + m)/math.factorial(actualBlackBlocks)/math.factorial(m)

# n is the number of total black blocks
# and m is the number of green blocks used
def greenFunction(n, m):
    actualBlackBlocks = n - 4*m

    if (actualBlackBlocks < 0):
        return -1 # error

    return math.factorial(actualBlackBlocks + m)/math.factorial(actualBlackBlocks)/math.factorial(m)

n = 50
answer = (sum(redFunction(n, m) for m in xrange(1, n / 2 + 1)) +
          sum(blueFunction(n, m) for m in xrange(1, n / 3 + 1)) +
          sum(greenFunction(n, m) for m in xrange(1, n / 4 + 1)))
print answer