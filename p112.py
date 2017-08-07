def isIncreasingNumber(n):
    digits = []
    while(n != 0):
        digits.append(n % 10)
        n /= 10

    for x in xrange(len(digits)-1):
        if(digits[x] > digits[x+1]):
            return False

    return True

def isDecreasingNumber(n):
    digits = []
    while(n != 0):
        digits.append(n % 10)
        n /= 10

    for x in xrange(len(digits)-1):
        if(digits[x] < digits[x+1]):
            return False

    return True

number = 1
bouncy = 0
proportion = bouncy / number
while(proportion < 0.99):
    if not (isIncreasingNumber(number) or isDecreasingNumber(number)):
        bouncy += 1
    proportion = float(bouncy) / number
    number += 1

print number-1

#def getNextIncreasingNumber(inputArr):

#    # make a deep copy of the input array
#    arr = list(inputArr)

#    # ensure that the number is an increasing number
#    isIncreasing = True
#    for x in xrange(len(arr)-1):
#        if(arr[x] > arr[x+1]):
#            isIncreasing = False
            
#    if not isIncreasing:
#        return -1

#    # find the next digit to increase
#    needNewDigit = True
#    whichSpot = 0
#    for x in xrange(len(arr)-1, -1, -1):
#        if (arr[x] < 9):
#            arr[x] += 1
#            needNewDigit = False
#            whichSpot = x
#            break

#    # if we need a new digit, then we set
#    # all of the digits to 1 otherwise let i be the
#    # index of the digit that we increased and v be the
#    # new value, we set
#    # all of the digits with index greater than i
#    # to the value v
#    if (needNewDigit):
#        for x in xrange(len(arr)):
#            arr[x] = 1
#        arr.append(1)
#    else:
#        val = arr[whichSpot]
#        for x in xrange(whichSpot, len(arr)):
#            arr[x] = val

#    # return the edited array
#    return arr

#def getNextDecreasingNumber(inputArr):

#    # make a deep copy of the input array
#    arr = list(inputArr)

#    # ensure that the number is a decreasing number
#    isDecreasing = True
#    for x in xrange(len(arr)-1):
#        if(arr[x] < arr[x+1]):
#            isDecreasing = False
            
#    if not isDecreasing:
#        return -1

#    # find the next digit to increase
#    needNewDigit = True
#    whichSpot = 0
#    for x in xrange(len(arr)-1, 0, -1):
#        if (arr[x] < arr[x-1]):
#            arr[x] += 1
#            needNewDigit = False
#            whichSpot = x
#            break
#        if(x == 1): # reached the front of the number
#            if(arr[0] < 9):

#                # increment the first digit
#                arr[0]+=1
#                needNewDigit=False;


#    # if we need a new digit, then we set
#    # all of the digits to 0 and add a 1 to the front
#    # of the list otherwise we set all of the digits
#    # to the right of the digit that has increased to zero
#    if (needNewDigit):
#        for x in xrange(len(arr)):
#            arr[x] = 0
#        arr.append(0)
#        arr[0] = 1
#    else:                
#        # set the rest of the numbers to zero
#        for y in xrange(whichSpot+1,len(arr)):
#            arr[y] = 0

#    # return the edited array
#    return arr

#def getProportionOfBouncyNumbers(n):
#    totalNumbers = n+1
    
#    # initial numbers
#    increasing = [1,1]
#    numIncreasing = 10
#    decreasing = [1,1]
#    numDecreasing = 10

#    # get next non bouncy number
#    increasing = getNextIncreasingNumber(increasing)
#    decreasing = getNextDecreasingNumber(decreasing)
#    valIncreasing = sum([increasing[len(increasing)-i-1]*(10**i) for i in xrange(len(increasing))])
#    valDecreasing = sum([decreasing[len(decreasing)-i-1]*(10**i) for i in xrange(len(decreasing))])
#    if(valDecreasing

#    # determine proportion of bouncy to non-bouncy

#    while():
#    nonBouncyNumbers = 