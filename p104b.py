import math

def isLeftPandigital(x):

    y = math.log(x, 10)
    y = y - math.floor(y)
    y = (10**y)*math.pow(10,8)

    return isRightPandigital(int(y))

def isRightPandigital(x):
    check = set()

    # check that the least significant nine digits
    # are pandigital
    x = int(math.floor(x))
    while (x > 0):
        digit = x % 10
        x = x // 10
        if digit in check:
            return False
        else:
            check.add(digit)

    # ensure 0 isn't looked at
    if 0 in check:
        return False

    return len(check) == 9


previous = 1
current = 1
count = 2
last9 = math.pow(10, 9)
f1 = 1
f2 = 1
prevCount = 2
while (True):
    newNum = previous + current
    newNum %= last9
    count += 1
    check1 = isRightPandigital(newNum)

    if check1:
        # compute full fibonacci number and check
        # if it is left pandigital
        while(prevCount != count):
            t = f2
            f2 = f1 + f2
            f1 = t
            prevCount += 1

        if isLeftPandigital(f2):
            break

    previous = current
    current = newNum

print count