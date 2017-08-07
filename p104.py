import math

def isRightPandigital(x):
	check = set()

	# check that the least significant nine digits
	# are pandigital
	x = int(math.floor(x))
	while(x > 0):
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
while(True):
	newNum = previous + current
	newNum %= last9
	count += 1
	check1 = isRightPandigital(newNum)

	if check1:
		# now we check if the specific Fib
		# num is left pandigital
		phi = (1 + math.sqrt(5))/2
		logApprox = count * math.log(phi,10) - math.log(math.sqrt(5), 10)
		logApprox2 = logApprox - math.floor(logApprox)
		print logApprox2
		approx3 = 10 ** logApprox2
		print approx3
		approx4 = round(approx3* (10 ** 8))
		print approx4
		check2 = isRightPandigital(approx4)
		if check2:
			break

	previous = current
	current = newNum
		
print count