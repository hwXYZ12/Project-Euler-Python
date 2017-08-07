import math
import copy
import sys

# MAX_PERIMETER = 10000
# x = 2
# total = 0
# while(x <= MAX_PERIMETER):
	# # case 1
	# p = 3*x+1
	# s = p/2.0
	# area = (s-x)*math.sqrt(s*(s-(x+1)))
	# if(area % 1 == 0 and p<=MAX_PERIMETER):
		# print x
		# print p
		# print "case 1"
		# total += p
		
	# # case 2
	# p = 3*x-1
	# s = p/2.0
	# area = (s-x)*math.sqrt(s*(s-(x-1)))
	# if(area % 1 == 0 and p<=MAX_PERIMETER):
		# print x
		# print p
		# print "case 2"
		# total += p
		
	# x += 1

# print total
	
	
MAX_PERIMETER = math.pow(10, 9)
total = 0
n = 1
while (n*n <= MAX_PERIMETER):
	# case 1
	m2 = 1.0 + 3*n*n
	m = math.sqrt(m2)
	if(m % 1 == 0):
		a = m2 - n*n
		b = 2*m*n
		c = m2 + n*n
		p = 3*c+1
		print a
		print b
		print c
		if(p <= MAX_PERIMETER):
			total += p

	# case 2
	if(n > 1):
		b = n*n - 1
		c = 2*b + 1
		a = math.sqrt(c*c - b*b)
		if(a % 1 == 0):
			p = c+c+2*b
			print a
			print b
			print c
			if(p <= MAX_PERIMETER):
				total += p
		
	n += 1
	
print total

# a = m^2 - n^2
# b = 2mn
# c = m^2 + n^2
# ----
# 2a-1 = c (case 1)
# 2m^2-2n^2 - 1 = m^2 + n^2
# m^2 - 3n^2 = 1
# m^2 = 1 + 3n^2
# ----
# x = c

# 2b+1 = c (case 2)
# 2*2mn + 1 = m^2 + n^2
# m^2 + n^2 - 2mn = 2mn + 1
# (m-n)^2 - 2mn - 1 = 0
# x^2 - b - 1 = 0
# b = x^2 - 1
# ----
# x = c



