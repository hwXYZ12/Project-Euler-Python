import math
import pdb

# represents a 2D matrix of possibility sets of a potential
# Su Doku solution as well as a particular guess for a value
# in addition to the coordinates of that guess
class Guess:
	
	def __init__(self, possibilities, whichCoord, guess):
		self.possibilities = possibilities
		self.whichCoord = whichCoord
		self.guess = guess

# get initial board state from file
puzzles = open('p096_sudoku.txt', 'r')

# Determines whether or not a particular value in a row, column,
# or box can only appear in one spot. If this is the case, then
# we can replace that spot with the particular value described.
# Returns true or false depending on whether or not a new value
# had been deduced.
def reduceIndirectly(possibilities):	

	hasChanged = False
	# check each row, column, and box to see
	# if an element can only appear in one subdivision
	# in that case, that possibility set is reduced to
	# that single element
	
	# check rows first
	for x in range(9):
		for y in range(9):		
			union = set()
			for w in range(9):
				if(w != y):
					union |= possibilities[x][w]
			dif = possibilities[x][y] - union
			if(len(dif) == 1):
				elem = next(iter(dif))
				newSet = set()
				newSet.add(elem)
				possibilities[x][y] = newSet
				hasChanged = True
												
	# check columns next
	for y in range(9):
		for x in range(9):
			union = set()
			for w in range(9):
				if(w != x):
					union |= possibilities[w][y]
			dif = possibilities[x][y] - union
			if(len(dif) == 1):
				elem = next(iter(dif))
				newSet = set()
				newSet.add(elem)
				possibilities[x][y] = newSet
				hasChanged = True
					
	# check boxes last
	for x in range(9):
		for y in range(9):
			xp = x//3
			yp = y//3
			union = set()
			for a in range(3*xp, 3*xp+3):
				for b in range(3*yp, 3*yp+3):
					
					if(not (a==x and b==y)):
						union |= possibilities[a][b]
						
			dif = possibilities[x][y] - union
			if(len(dif) == 1):
				elem = next(iter(dif))
				newSet = set()
				newSet.add(elem)
				possibilities[x][y] = newSet
				hasChanged = True
				
	return hasChanged


# reduces possibility sets of each element of the grid
# using only the determined elements of the corresponding
# row, column, and box
# constitutes a fixed-point algorithm that will always halt
# and doesn't return 
def reduceDirectly(possibilities):
	# iterate over the set(s) of possibilities until
	# the set(s) of possibilities haven't changed
	hasChanged = True
	while(hasChanged):
		hasChanged = False
		for x in range(0,9):
			for y in range(0,9):
				
				# look at the row of the point; (x,0) to (x, 8)
				# and remove possibilities that aren't possible
				for w in range(9):
					if(len(possibilities[x][w]) == 1):
						elem = next(iter(possibilities[x][w]))
						if (elem in possibilities[x][y]
							and len(possibilities[x][y]) != 1):
							possibilities[x][y].remove(elem)
							hasChanged = True
						
				# look at the column of the point; (0,y) to (8, y)
				# and remove possibilities that aren't possible
				for w in range(9):
					if(len(possibilities[w][y]) == 1):
						elem = next(iter(possibilities[w][y]))					
						if (elem in possibilities[x][y]
							and len(possibilities[x][y]) != 1):
							possibilities[x][y].remove(elem)
							hasChanged = True
											
				# look at the box of values containing the point
				# which is tricky to define properly in terms of x and y
				# and remove possibilities that aren't possible
				
				# compute x/3 and y/3
				xp = x//3
				yp = y//3
				for a in range(3*xp, 3*xp+3):				
					for b in range(3*yp, 3*yp+3):
						if(len(possibilities[a][b]) == 1):
							elem = next(iter(possibilities[a][b]))						
							if (elem in possibilities[x][y]
								and len(possibilities[x][y]) != 1):
								possibilities[x][y].remove(elem)
								hasChanged = True

# infers as much information from the given set of possibilities
# checks whether the puzzle has been solved and returns
# this result
def reducePossibilities(possibilities):
	hasChanged = True
	while(hasChanged):
		reduceDirectly(possibilities)
		hasChanged = reduceIndirectly(possibilities)
		
	# check that all possibilities are of size 1
	check = True
	for x in range(0,9):
		for y in range(0,9):
			print "("+str(x)+","+str(y)+"): "
			print possibilities[x][y]
			if(len(possibilities[x][y]) != 1):
				check = False
	
	return check				
								
sum = 0
# loop over 50 puzzles
for p in range(6):

	# generate all intial possibilities
	possibilities = [[set(range(1,10)) for x in range(9)] for y in range(9)]

	# read in a new puzzle from the input
	boardState = [[0 for x in range(0,9)] for y in range(0,9)]
	puzzles.readline() # first line is grid number
	for x in range(0,9):
		line = puzzles.readline()
		print line
		for i in range(0, 9):
			boardState[x][i] = int(line[i])
			
	# update possibilities with initial board state
	for x in range(0,9):
		for y in range(0,9):
			if(boardState[x][y] != 0):
				newSet = set()
				newSet.add(boardState[x][y])
				possibilities[x][y] = newSet
				
	# backtracking algorithm
	stackOfGuesses = []
	complete = reducePossibilities(possibilities)
	
	# check whether a grid position ends up with no possibilities
	
	if(not complete):
		# get a minimal set from the set of possibilities
		# (that is, we hope that there is a spot in the semi-solved
		# state that has 2 possible choices and we want to select one)
		min = 9
		whichX = 0
		whichY = 0
		for x in range(9):
			for y in range(9):
				z = len(possibilities[x][y])
				if(z>1 and
					z<min):
					min = z
					whichX = x
					whichY = y
					
		# choose one of the elements of the set
		elem = next(iter(possibilities[whichX][whichY]))
		
		# create a guess and push it on the stack
		stackOfGuesses.append(Guess(possibilities, (whichX, whichY), elem))
	
		# alter possibilities using the guessed value
		newSet = set()
		newSet.add(elem)
		possibilities[whichX][whichY] = newSet
		
		# reduce using the guess
		complete = reducePossibilities(possibilities)
		
		# recurse here....
		if(not complete):
			...
		
				
	elem = next(iter(possibilities[0][0]))
	# print elem
	sum += 100*elem
	elem = next(iter(possibilities[0][1]))
	# print elem
	sum += 10*elem
	elem = next(iter(possibilities[0][2]))
	# print elem
	sum += elem
		
		
print sum
				
	