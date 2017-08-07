import math
import operator

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

# fill count function using a row of n units and
# blocks of length at least m units
def fillCountFunction(n, m):
    return 1 + sum(prod(n-(m+1)*(k-1)-2+j for j in xrange(2*k-1+1))/math.factorial(2*k) for k in xrange(1, int(math.floor(float(n)/(m+1)))+1))

print fillCountFunction(50, 3)
