import math
from itertools import product

def getSolListwithOneDart(n):
    ret = []
    if (n > 60):
        return ret
    elif(n>40):
        if (n%3==0):
            ret.append("T"+str(n/3))
        if(n==50):
            ret.append("D25")
        return ret
    elif(n>20):
        if(n%3==0):
            ret.append("T"+str(n/3))
        if(n%2==0):
            ret.append("D"+str(n/2))
        if(n == 25):
            ret.append("S25")
        return ret
    elif(n > 0):
        ret.append("S"+str(n))
        if(n%3==0):
            ret.append("T"+str(n/3))
        if(n%2==0):
            ret.append("D"+str(n/2))
        return ret

    return ret

def crossProduct(a,b):
    ret = []
    for i in xrange(len(a)):
        for j in xrange(len(b)):
            add = True
            for k in ret:
                (x,y) = k
                if ((x == a[i] and y == b[j])
                    or
                    (y == a[i] and x == b[j])):
                    add = False
            if add:
                ret.append((a[i],b[j]))
    return ret

def waysWithAtMostTwoDarts(n):

    count = len(getSolListwithOneDart(n))
    for i in xrange(1, n/2+1):
        thing = crossProduct(getSolListwithOneDart(i),getSolListwithOneDart(n-i))      
        count += len(thing)
    return count

waysToGetToX = {n:waysWithAtMostTwoDarts(n) for n in xrange(1,171)}

count = 0
for j in xrange(1,100):
    for i in range(1, 21)+[25]:
        end = 2*i
        if (j > end):
            leftOver = j - end
            count += waysToGetToX[leftOver]
        elif(j == end):
            count += 1


print count


