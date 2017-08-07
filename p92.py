import math

count = 0
nums = set()
for a in range(1,1001):
	x = a
	while(x != 1 and x != 89):
		sum = 0
		for ch in str(x):
			temp = int(ch)
			sum += temp*temp
		x = sum
	if(x == 89):
		count += 1
		if(a <= 567):
			nums.add(a)
	
for a in range(8):
	for b in range(8):
		for c in range(8):
			for d in range(8):
				for e in range(8):
					for f in range(8):
						for g in range(8):
							for h in range(8):
								for i in range(8):
									check = a+b+c+d+e+f+g+h+i
									if(check < 8):
										x = a+4*b+9*c+16*d+25*e+36*f+49*g+64*h+81*i										
										if(x in nums and check > 3):
											print str(a)+" "+str(b)+" "+str(c)+" "+str(d)+" "+str(e)+" "+str(f)+" "+str(g)+" "+str(h)+" "+str(i)
											count += math.factorial(a+b+c+d+e+f+g+h+i) / math.factorial(a) / math.factorial(b) / math.factorial(c) / math.factorial(d) / math.factorial(e) / math.factorial(f) / math.factorial(g) / math.factorial(h) / math.factorial(i)												
print count