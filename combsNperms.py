import math
import copy

def perms(l, n):
    ret = []
    if (len(l) > 1 and n > 1):
        for i in xrange(0, len(l)):
            # get perms of list - 1 elements
            smallList = copy.copy(l)
            x = l[i]
            smallList.remove(l[i])
            listOfLists = perms(smallList, n - 1)
            for smallerList in listOfLists:
                smallerList.append(x)
                ret.append(smallerList)
        return ret

    for i in xrange(0, len(l)):
        ret.append([l[i]])
    return ret

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
                if (i > len(smallerList)-1):
                    smallerList.append(x)
                    ret.append(smallerList)
        return ret

    for i in xrange(0, len(l)):
        ret.append([l[i]])
    return ret

print combs([1,2,3,4], 2)

