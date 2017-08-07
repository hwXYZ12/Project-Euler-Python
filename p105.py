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

# helps check condition i.
tupleLists = {}
for n in xrange(7, 13):

    newTupleList = []

    listOfSets = []
    maxSubSetSize = int(math.floor(n/2))
    for i in xrange(2, maxSubSetSize+1):
        listOfSets.append(combs([j for j in xrange(1, n+1)], i))

    count = 0
    for i in xrange(2, maxSubSetSize+1):
        a = i - 2
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
                        # add tuple to the list of tuples, which represent a tuple
                        # of two tuples where each tuple represents the respective disjoint
                        # subsets
                        tuple1 = tuple(listOfSets[a][x])
                        tuple2 = tuple(listOfSets[a][y])
                        theTuple = (tuple1, tuple2)
                        newTupleList.append(theTuple)

    tupleLists[n] = newTupleList

# helps check condition ii.
cond2 = {}
for n in xrange(7, 13):
    subsetVar = int(math.floor((n+1)/2))
    cond2TupleList = []
    for m in xrange(2, subsetVar+1):
        tuple1 = tuple([x for x in xrange(n-m+2,n+1)])# size m-1 tuple, begins with the largest element
                                                        # of the set
        tuple2 = tuple([x for x in xrange(1,m+1)])        # size m tuple, begins with the smallest element
                                                        # of the set
        theTuple = (tuple1, tuple2)
        cond2TupleList.append(theTuple)
    cond2[n] = cond2TupleList

# read each set from file
specialSets = [sorted([int(num) for num in line.split(',')]) for line in open("p105_sets.txt").readlines()]

# walk through each special set and use the list of tuples
# do test whether the set is indeed special
tabulateTotal = 0
for s in specialSets:
    isSpecial = True

    for t in cond2[len(s)]:
        (t1, t2) = t
        # use the tuples to ensure that certain inequalities
        # hold

        # get the sum defined by the first tuple
        sum1 = 0
        for x in t1:
            sum1 += s[x - 1]

        # get the sum defined by the second tuple
        sum2 = 0
        for x in t2:
            sum2 += s[x - 1]

        if not (sum1 < sum2):
            # not a special set
            isSpecial = False
            break


    if isSpecial:
        # don't execute this block in the case
        # that condition ii. doesn't hold...
        # this code checks condition i.

        for t in tupleLists[len(s)]:
            (t1, t2) = t
            # use the tuples to ensure that certain inequalities
            # hold

            # get the sum defined by the first tuple
            sum1 = 0
            for x in t1:
                sum1 += s[x-1]

            # get the sum defined by the second tuple
            sum2 = 0
            for x in t2:
                sum2 += s[x-1]

            if (sum1 == sum2):
                # not a special set
                isSpecial = False
                break

    if isSpecial:
        tabulateTotal += sum(s)

print tabulateTotal



