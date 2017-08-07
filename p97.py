import math

ret = 1
MOD = long(math.pow(10,10))
for x in range(7830457):
	ret *= 2
	ret %= MOD
	
ret *= 28433
ret %= MOD

ret += 1
ret %= MOD

print ret