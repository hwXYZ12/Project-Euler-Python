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
# and r is the number of red blocks used
# and g is the number of green blocks used
def redGreenFunction(n, r, g):
    actualBlackBlocks = n - 2*r - 3*g

    if (actualBlackBlocks < 0):
        return -1 # error

    return math.factorial(actualBlackBlocks+r+g)/math.factorial(actualBlackBlocks)/math.factorial(r)/math.factorial(g)

# n is the number of total black blocks
# and r is the number of red blocks used
# and b is the number of blue blocks used
def redBlueFunction(n, r, b):
    actualBlackBlocks = n - 2*r - 4*b

    if (actualBlackBlocks < 0):
        return -1 # error

    return math.factorial(actualBlackBlocks+r+b)/math.factorial(actualBlackBlocks)/math.factorial(r)/math.factorial(b)

# n is the number of total black blocks
# and g is the number of green blocks used
# and b is the number of blue blocks used
def greenBlueFunction(n, g, b):
    actualBlackBlocks = n - 3*g - 4*b

    if (actualBlackBlocks < 0):
        return -1 # error

    return math.factorial(actualBlackBlocks+g+b)/math.factorial(actualBlackBlocks)/math.factorial(g)/math.factorial(b)

# n is the number of total black blocks
# and r is the number of red blocks used
# and g is the number of green blocks used
# and b is the number of blue blocks used
def redGreenBlueFunction(n, r, g, b):
    actualBlackBlocks = n - 2*r - 3*g - 4*b

    if (actualBlackBlocks < 0):
        return -1 # error

    return math.factorial(actualBlackBlocks+r+g+b)/math.factorial(actualBlackBlocks)/math.factorial(g)/math.factorial(b)/math.factorial(r)


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

# add red green
for r in xrange(1, n):
    for g in xrange(1, n):
        if(2*r+3*g<=n):
            answer += redGreenFunction(n, r, g)

# add red blue
for r in xrange(1, n):
    for b in xrange(1, n):
        if(2*r+4*b<=n):
            answer += redBlueFunction(n, r, b)

# add green blue
for b in xrange(1, n):
    for g in xrange(1, n):
        if(3*g+4*b<=n):
            answer += greenBlueFunction(n, g, b)

# add red green blue
for r in xrange(1, n):
    for b in xrange(1, n):
        for g in xrange(1, n):
            if(2*r+3*g+4*b<=n):
                answer += redGreenBlueFunction(n, r, g, b)

print answer+1