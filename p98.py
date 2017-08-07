import math
import copy
import string

# get word list
wordFile = open('p098_words.txt', 'r')

# parse words into a list of words
words = wordFile.read().split(",")

# clean the words
for i in range(len(words)):
	words[i] = words[i][1:len(words[i])-1]

# get the length of the largest word in the list
maxWordLength = 0
for x in words:
	l = len(x)
	if l > maxWordLength:
		maxWordLength = l

# populate a list with enough lists to separate all of
# the given words into separate lists based off of their length
listOfWordLists = []
for i in range(maxWordLength):
	newList = []
	listOfWordLists.append(newList)

# split all of the words in the list of words
# into a partition based on the length of each word
for x in words:
	l = len(x)
	listOfWordLists[l-1].append(x)

# for each partition of words we want to find all possible anagrams
# within the list of words
# to do this we place every word in a dictionary using it's sorted result as the key
anagramSets = []
for i in range(len(listOfWordLists)):
	# we perform this operation on each possible word length
	newAnagramDict = {}
	for w in listOfWordLists[i]:
		sortedWord = ''.join(sorted(w))
		if sortedWord in newAnagramDict:
			s = newAnagramDict[sortedWord]
		else:
			s = set()
		if not (w in s):
			s.add(w)

		newAnagramDict[sortedWord] = s

	# add dictionary of anagrams to the list
	# of anagram sets
	anagramSets.append(newAnagramDict)

# reduce the set of anagrams that we're looking at by
# eliminating all of the sets of size 1 in each dictionary
for i in range(len(anagramSets)):
	keysToRemove = set()
	for key in anagramSets[i]:
		if len(anagramSets[i][key]) < 2:
			# mark that key to be removed from the set
			keysToRemove.add(key)

	for x in keysToRemove:
		del anagramSets[i][x]

print anagramSets

# for each anagram set check whether or not a square anagram pair
# exists using the words in the set
largest = 0
for i in range(len(anagramSets)):
	for key in anagramSets[i].keys():
		for word in anagramSets[i][key]:
			# determine whether or not a digital substitution
			# can be used to produce a square number using
			# one of the words in the set
			# to do this, we loop over the square numbers
			# that are possible using the size of the word
			# in question
			l = len(word)
			for x in range(int(math.ceil(math.sqrt(math.pow(10, l-1)))),
						   int(math.ceil(math.sqrt(math.pow(10, l))))):
				sq = x*x
				digits = list(str(sq))
				wordAsList = list(word)
				mapCharToDigit = {}
				mappingFailed = False
				assigned = set()
				for j in range(l):
					if(wordAsList[j] in mapCharToDigit):
						'''We have already come across this character and
						assigned it a digit, we must then
						ensure that it matches the digit at the same location
						in the number and if it doesn't then we know we cannot
						map this word to the square number'''
						if(mapCharToDigit[wordAsList[j]] != digits[j]):
							# mapping failed
							mappingFailed = True
							break
					else:
						'''We must ensure that the mapping doesn't assign
						the same digit twice'''
						if(digits[j] in assigned):
							# mapping failed
							mappingFailed = True
							break
						else:

							'''Must also ensure that we don't map any leading zeros!'''
							# TODO
							mapCharToDigit[wordAsList[j]] = digits[j]
							assigned.add(digits[j])

				if(not mappingFailed):
					for word2 in anagramSets[j][key]:
						# don't check the same words against
						# each other
						if not (word == word2):
							# apply the digital substitution that had been
							# determined earlier
							word2AsList = list(word2)
							num = 0
							for k in range(l):
								num += int(mapCharToDigit[word2AsList[l-k-1]]) * int(math.pow(10, k))

							# is the number a perfect square?
							if math.sqrt(num) % 1 == 0:
								print str(sq)+" "+str(num)
								print word+" "+word2
								# we've found a square anagram pair!
								# check if either are larger than our current
								# largest square number that we've seen in any pair
								# so far
								if num > sq:
									temp = num
								else:
									temp = sq
								if temp > largest:
									largest = temp

print largest

# returns all the words within a given set
# that are anagrams of a given word
# def getAnagrams(words, whichWord):
# 	characterCount = {}
# 	characters = list(string.ascii_uppercase)
# 	for c in characters:
# 		characterCount[c] = 0
# 	for character in whichWord:
# 		characterCount[character] += 1
#
# 	ret = []
# 	for x in words:
# 		if(whichWord != x):
# 			characterCount2 = {}
# 			for c in list(string.ascii_uppercase):
# 				characterCount2[c] = 0
# 			for character in x:
# 				characterCount2[character] += 1
#
# 			matches = True
# 			for i in list(string.ascii_uppercase):
# 				if(characterCount[i] != characterCount2[i]):
# 					matches = False
#
# 			if (matches):
# 				ret.append(x)
#
# 	return ret
#
# def permsOfK(l, k):
# 	ret = []
# 	if (k > 1):
# 		for x in l:
#
# 			# get perms of list - 1 elements
# 			smallList = copy.copy(l)
# 			smallList.remove(x)
# 			listOfLists = permsOfK(smallList, k-1)
# 			for smallerList in listOfLists:
# 				smallerList.append(x)
# 				ret.append(smallerList)
#
# 		return ret
#
# 	for x in l:
# 		ret.append([x])
# 	return ret
#
#
# # do some pre-computation
# permsLists = {}
# for i in range(1,10):
# 	permsLists[i] = permsOfK([1,2,3,4,5,6,7,8,9], i)
#
# # generate all possible digital substitutions
# # for a given word that does not violate
# # 'leading zeroes are not permitted, neither may a different
# # letter have the same digital value as another letter.'
# largest = 0
# for w in words:
#
# 	print w
#
# 	# remove duplicate letters from the word
# 	noDups = list(set(w))
#
# 	# skip any word that has more than 9
# 	# unique digits
# 	if (len(noDups) > 9):
# 		continue
#
# 	# generate a list of all possible permutations
# 	# of n distinct digits where n is the length of noDups
# 	listOfPerms = permsLists[len(noDups)]
#
# 	for p in listOfPerms:
# 		letterToDigit = {}
# 		for x in range(len(noDups)):
# 			letterToDigit[noDups[x]] = p[x]
#
# 		# get w after the given digital substitution
# 		num = 0
# 		for x in range(len(w)):
# 			# start from right to left
# 			num+= letterToDigit[w[len(w)-x-1]]*long(math.pow(10, x))
#
# 		# check if w is a square number
# 		if(math.sqrt(num) % 1 == 0):
# 			# check this specific digital substitution against
# 			# the other words in the list and in particular ensure
# 			# that those words are anagrams of w
#
# 			# get the anagrams of w
# 			anagrams = getAnagrams(words, w)
#
# 			# check if any of the anagrams of w
# 			# produce a perfect square using the current
# 			# digital substitution
# 			for a in anagrams:
# 				# get the anagram number after the substitution
# 				num2 = 0
# 				for x in range(len(a)):
# 					# start from right to left
# 					num2 += letterToDigit[w[len(a)-x-1]]*long(math.pow(10, x))
#
# 				# check if the anagram after substitution is
# 				# a perfect square
# 				if(math.sqrt(num2) % 1 == 0):
# 					# we found an anagram square pair!!
#
# 					# check which square is larger
# 					if(num > num2):
# 						temp = num
# 					else:
# 						temp = num2
# 					if(temp > largest):
# 						largest = temp
#
# print largest
	

	
	
# def numToList(x):
	# n = x
	# ret = []
	# while(n!=0):
		# next=n%10
		# ret.append(next)
		# n=n//10
	# ret.reverse()
	# return ret

# def listToNum(l):
	# l.reverse()
	# ret = 0
	# for i in range(len(l)):
		# ret += long(math.pow(10, i))*l[i]
	# return ret

# # get word list
# wordFile = open('p098_words.txt', 'r')

# # parse words into a list of words
# words = wordFile.read().split(",")

# # clean the words and get the largest
# # possible square value
# max = 0
# for i in range(len(words)):
	# length = len(words[i])
	# words[i] = words[i][1:length-1]
	# if(length > max):
		# max = length
# # reduce max by 2 double quote characters
# max -= 2

# pdb.set_trace()

# # use largest word length to determine the
# # size of the largest possible perfect square that we
# # may need to compute
# #SQUARE_CONST = int(math.ceil(math.sqrt(math.pow(10,max))))
# SQUARE_CONST = int((math.pow(10,5)))
# squares = set()
# for x in range(1,SQUARE_CONST+1):
	# squares.add(x*x)

# # build dictionary that takes a perfect square 
# # which has been sorted to
# # it's permutations which are also perfect squares
# perfectSquarePerms = {}
# for a in squares:

	# # sort the number by digit
	# l = numToList(a)
	# l.sort()
	# x = listToNum(l)
				
	# # Has x been seen already?
	# if(x in perfectSquarePerms):
		# s = perfectSquarePerms[x]
	# else:
		# s = set()
		
	# s.add(a)
	# perfectSquarePerms[a] = s

# pdb.set_trace()
# # search for anagram word pairs
# # and return the largest value of any perfect square
# # found in any perfect square anagram word pair
# largest = 0
# for x in range(len(words)):
	# word = words[x]
	
	# # check if any perfect squares can be produced
	# # by assigning a digit to each letter of the
	# # given word
	# length = len(word)
	# cap = math.pow(10, length)
	# count = 0
	# while(squares[count] <= cap):
		
		# assignmentFailed = False
		# listForm = numToList(squares[count])
		# assignDigitToLetter = {}
		# assignLetterToDigit = {}
		# if(len(squares[count]) == len(word)):
			
						
			# for d in range(len(listForm)):
				# digit = listForm[d]
				# letter = word[d]
				# if(digit in assignDigitToLetter):
					# # we've already assigned this digit
					# # a letter
					# # check that the assigned letter matches
					# # the letter that we're currently viewing
					# # in the word
					# if(assignDigitToLetter[digit] != letter):
						# # go to the next perfect square
						# assignmentFailed = True
						# break
				# else:
					# # we know that this digit hasn't been
					# # assigned yet but we need to ensure
					# # that the letter that we are assigning
					# # it to has not already been used
					# if(letter in assignLetterToDigit):
						# # make sure that the digit that this
						# # letter is assigned to is the same
						# # as the digit that we're looking at
						# # currently
						# if(assignLetterToDigit[letter] != digit):
							# assignmentFailed = True
							# break
					# else:
						# # the digit hasn't been assigned yet
						# # AND the letter hasn't been assigned yet
						# # so we pair them
						# assignDigitToLetter[digit] = letter
						# assignLetterToDigit[letter] = digit
		
		# if(not assignmentFailed):
			
			# # get permuted perfect squares
			# sorted = listToNum(listForm.sort())
			# if(sorted in perfectSquarePerms):
				# # permuted perfect squares exist!!
				# # check if any of them can be represented using
				# # the same assignment of letters and
				# # digits
				# for p in perfectSquarePerms[sorted]:
					# # don't check the number against itself
					# if( p != squares[count]):
						# # get the word that results from the
						# # digit to letter assignment
						# newWord = ""
						# pAsList = numToList(p)
						# for y in range(len(pAsList)):
							# newWord += str(assignDigitToLetter[pAsList[y]])
							
						# # if that word is contained in our list
						# # of words then we have found a square anagram
						# # word pair!
						# if(newWord in words):							
							# # we can then check which of the perfect squares
							# # is larger and check that value against the
							# # current largest perfect square
							# if(squares[count] > p):
								# temp = squares[count]
							# else:
								# temp = p
							
							# if(largest < temp):
								# largest = temp
						
			
		
		# count += 1
		
# print largest


	
