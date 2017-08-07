import math

# get input
inputFile = open('p099_base_exp.txt', 'r')

# parse input into a list of base-exponent pairs
lines = inputFile.readlines()

# get largest numerical value
whichLine = 0
largest = 0
for i in range(len(lines)):
	split = lines[i].split(",")
	base = split[0]
	exp = split[1]
	check = float(math.log(float(base)))*float(exp)
	if(check > largest):
		largest = check
		whichLine = i
		
print (whichLine+1)
		
	
		
