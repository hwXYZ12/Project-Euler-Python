import math
import operator

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def nonBouncyNumsWithNDigits(n):
    # get the decreasing numbers
    dec = sum(prod(xrange(n, n+i))/math.factorial(i) for i in xrange(1,10))
    # get the increasing numbers
    inc = prod(xrange(9, 9+n))/math.factorial(n)
    return dec + inc - 9 # 9 is the number of numbers that are both increasing and decreasing

# get the number of non-bouncy numbers less than 10**x for some x
def nonBouncyNumbers(x):
    return sum(nonBouncyNumsWithNDigits(i) for i in xrange(1, x+1))

print nonBouncyNumbers(100)
