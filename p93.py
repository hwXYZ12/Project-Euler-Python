import math
import copy
import sys

def perms(l):
	ret = []
	if (len(l) > 1):
		for x in l:
			# get perms of list - 1 elements
			smallList = copy.copy(l)
			smallList.remove(x)
			listOfLists = perms(smallList)
			for smallerList in listOfLists:
				smallerList.append(x)
				ret.append(smallerList)
		return ret
				
	return [l]

def op(char, a, b):

	if(a == sys.maxint or b == sys.maxint):
		return sys.maxint

	if (char == '+'):
		return a + b
	elif (char == '-'):
		return a - b
	elif (char == '*'):
		return a * b
	elif (char == '/'):
		if(b == 0):
			return sys.maxint
		else:
			return a / b

max = 28
digits = [1,2,3,4]
ops = ['+', '-', '*', '/']
for a in range(0, 10):
	for b in range(a+1, 10):
		for c in range(b+1, 10):
			for d in range(c+1, 10):			
					exprNums = set()
					for x in ops:
						for y in ops:
							for z in ops:
								list = [float(a), float(b), float(c), float(d)]
								listPerms = perms(list)
								for p in listPerms:
									temp = op(y, op(x, p[0], p[1]), op(z, p[2], p[3]))
									if(temp != sys.maxint and temp % 1 == 0):
										# print "( "+str(p[0])+" "+x+" "+str(p[1])+") "+y+" ("+str(p[2])+" "+z+" "+str(p[3])+")"
										exprNums.add(temp)
									temp = op(x, p[0], op(z, op(y, p[1], p[2]), p[3]))
									if(temp != sys.maxint and temp % 1 == 0):
										# print " "+str(p[0])+" "+x+" (("+str(p[1])+" "+y+" "+str(p[2])+") "+z+" "+str(p[3])+")"
										exprNums.add(temp)
									temp = op(x, p[0], op(y, p[1], op(z, p[2], p[3])))
									if(temp != sys.maxint and temp % 1 == 0):
										# print " "+str(p[0])+" "+x+" ("+str(p[1])+" "+y+" ("+str(p[2])+" "+z+" "+str(p[3])+"))"
										exprNums.add(temp)
									temp = op(z, op(y, op(x, p[0], p[1]), p[2]), p[3])
									if(temp != sys.maxint and temp % 1 == 0):
										# print "(("+str(p[0])+" "+x+" "+str(p[1])+") "+y+" "+str(p[2])+") "+z+" "+str(p[3])+""
										exprNums.add(temp)
									temp = op(z, op(x, p[0], op(y, p[1], p[2]) ), p[3])
									if(temp != sys.maxint and temp % 1 == 0):
										# print "("+str(p[0])+" "+x+" ("+str(p[1])+" "+y+" "+str(p[2])+")) "+z+" "+str(p[3])+""
										exprNums.add(temp)	

					count = 1.0
					while(count in exprNums):
						count += 1
						
					# print exprNums
					# print a
					# print b
					# print c
					# print d
					# print (count-1)
						
					exprNums.clear()
						
					if (count > max):
						max = count
						digits[0] = a
						digits[1] = b
						digits[2] = c
						digits[3] = d
															
print max
for i in range(0, 4):
	print digits[i]