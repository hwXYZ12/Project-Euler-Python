import math

def isSpecialSumSet(a,b,c,d,e,f,g):

    # check boundary values
    check = g < a + b
    check &= f + g < a + b + c
    check &= e + f + g < a + b + c + d
    if not check:
        return False

    arr = []
    arr.append(a)
    arr.append(b)
    arr.append(c)
    arr.append(d)
    arr.append(e)
    arr.append(f)
    arr.append(g)

    # check sums of size 2
    checkSet = set()
    for x in xrange(7):
        for y in xrange(x+1, 7):
            newVal = arr[x] + arr[y]
            if newVal in checkSet:
                # collision and return false
                return False
            else:
                checkSet.add(newVal)

    # check sums of size 3
    checkSet.clear()
    for x in xrange(7):
        for y in xrange(x+1, 7):
            for z in xrange(y+1, 7):
                newVal = arr[x] + arr[y] + arr[z]
                if newVal in checkSet:
                    # collision and return false
                    return False
                else:
                    checkSet.add(newVal)

    # check sums of size 4
    checkSet.clear()
    for x in xrange(7):
        for y in xrange(x+1, 7):
            for z in xrange(y+1, 7):
                for w in xrange(z+1, 7):
                    newVal = arr[x] + arr[y] + arr[z]+ arr[w]
                    if newVal in checkSet:
                        # collision and return false
                        return False
                    else:
                        checkSet.add(newVal)

    # check sums of size 5
    checkSet.clear()
    for x in xrange(7):
        for y in xrange(x+1, 7):
            for z in xrange(y+1, 7):
                for w in xrange(z+1, 7):
                    for v in xrange(w+1, 7):
                        newVal = arr[x] + arr[y] + arr[z]+ arr[w]+ arr[v]
                        if newVal in checkSet:
                            # collision and return false
                            return False
                        else:
                            checkSet.add(newVal)

    # check sums of size 6
    checkSet.clear()
    for x in xrange(7):
        for y in xrange(x+1, 7):
            for z in xrange(y+1, 7):
                for w in xrange(z+1, 7):
                    for v in xrange(w+1, 7):
                        for u in xrange(v+1, 7):
                            newVal = arr[x] + arr[y] + arr[z]+ arr[w]+ arr[v]+ arr[u]
                            if newVal in checkSet:
                                # collision and return false
                                return False
                            else:
                                checkSet.add(newVal)

    return True


whichSet = set()
s = 100000000000
k = 51
for a in xrange(18, 25):
    for b in xrange(a+1, k-5):
        for c in xrange(b+1, k-4):
            for d in xrange(c + 1, k-3):
                for e in xrange(d + 1, k-2):
                    for f in xrange(e + 1, k-1):
                        for g in xrange(f + 1, k):

                            # check if any of these combinations
                            # represent a special sum set
                            check = isSpecialSumSet(a, b, c, d, e, f, g)

                            if (check):
                                temp = a + b + c + d + e + f + g
                                if (temp < s):
                                    s = temp
                                    whichSet.clear()
                                    whichSet.add(a)
                                    whichSet.add(b)
                                    whichSet.add(c)
                                    whichSet.add(d)
                                    whichSet.add(e)
                                    whichSet.add(f)
                                    whichSet.add(g)
                                    print str(a)+" "+str(b)+" "+str(c)+" "+str(d)\
                                          +" "+str(e)+" "+str(f)+" "+str(g)


print whichSet
print s
