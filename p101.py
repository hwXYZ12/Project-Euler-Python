k = 10
u = lambda n: 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

def tld(x):
	return [x[i] - x[i-1] for i in range(1, len(x))]

seq = [map(u, range(1, k+1))]
for i in range(k):
	seq += [tld(seq[-1])]

print "Sum of FITs for the BOPs", sum(sum(seq, []))