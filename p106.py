import math
import copy

def combs(l, n):
    ret = []
    if (len(l) > 1 and n > 1):
        for i in xrange(0, len(l)):
            # get perms of list - 1 elements
            smallList = copy.copy(l)
            x = l[i]
            smallList.remove(l[i])
            listOfLists = combs(smallList, n - 1)
            for j in xrange(0, len(listOfLists)):
                smallerList = listOfLists[j]
                if (x > smallerList[len(smallerList)-1]):
                    smallerList.append(x)
                    ret.append(smallerList)
        return ret

    for i in xrange(0, len(l)):
        ret.append([l[i]])
    return ret

listOfSets = []
for i in xrange(2, 4):
    listOfSets.append(combs([1,2,3,4,5,6,7], i))

count = 0
for i in xrange(2, 4):
    a = i - 2
    print len(listOfSets[a])
    for x in xrange(0, len(listOfSets[a])):
        for y in xrange(x+1, len(listOfSets[a])):
            # perform the first check, ensure that the two
            # sets are disjoint
            fail = False
            for z in listOfSets[a][x]:
                if(z in listOfSets[a][y]):
                    # fail
                    fail = True
            if not fail:
                # ensure that we don't know whether or not
                # the sums of the sets are unequal implicitly
                check = []
                for j in xrange(len(listOfSets[a][x])):
                    check.append(listOfSets[a][x][j]>listOfSets[a][y][j])

                consistent = True
                if check[0]:
                    for j in check:
                        if not j:
                            consistent = False
                else:
                    for j in check:
                        if j:
                            consistent = False

                if not consistent:
                    print "[ "+str(listOfSets[a][x])+" , "+str(listOfSets[a][y])+" ], "
                    count += 1

print count