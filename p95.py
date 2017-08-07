import math
import pdb

ARRAY_SIZE = int(math.pow(10, 6))
divisorSum = {}

# build dictionary of divisor sums for the first
# ARRAY_SIZE integers
for x in range(1, ARRAY_SIZE+1):
	divisorSum[x] = 1

for x in range(2, ARRAY_SIZE+1):
	for j in range(2, int(math.floor(ARRAY_SIZE/x))+1):
		divisorSum[x*j] += x

# now find the largest amicable chain and its
# smallest element
maxChainLength = 2
minElementOfMaxChain = 220
for x in range(1, ARRAY_SIZE+1):
	next = divisorSum[x]
	chainLength = 1
	currentChain = {}
	currentElement = 1
	currentChain[x] = currentElement
	while(next!=1):
		# ensure that all elements are less than the ARRAY_SIZE
		if(next > ARRAY_SIZE):
			next=1
			break
		next = divisorSum[next]
		if(next in currentChain):
			break
		currentElement += 1
		currentChain[next] = currentElement
	if(next!=1):
		chainLength = currentElement - currentChain[next]+1
		if(maxChainLength < chainLength):
			maxChainLength = chainLength
			smallestElement = next
			check = divisorSum[next]
			if(check < smallestElement):
				smallestElement = check
			while(check!=next):
				check = divisorSum[check]
				if(check < smallestElement):
					smallestElement = check
			minElementOfMaxChain = smallestElement
		
print minElementOfMaxChain
		

	