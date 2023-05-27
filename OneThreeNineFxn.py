#!/usr/bin/python38

#JL 5/14/23

#Function to calculate the number of 1's, 3's , and 9's required to sum to a random integer n

import random

def onethreenine(n):

	if n >= 9:
		nines = int((n-(n % 9))/9)
	else:
		nines = 0

	
	if n > 3 and n > 9:
		threes = int(((n-(9*nines)) - (n % 3)) / 3)
	elif n >= 3 and n < 9:
		threes = int((n - (n % 3)) / 3)
	else:
		threes = 0


	if n > 1 and n > 3 and n > 9:
		ones = int((n-(9*nines + 3*threes)) / 1)
	elif n > 1 and n < 3 and n < 9:
		ones = int(n / 1)
	else:
		ones = 0
	

	print (str(nines) + ' nine(s), ' + str(threes) + ' three(s), and ' + str(ones) + ' one(s) are required to sum to ' + str(n))


#Test the fxn

number = random.randrange(0,27)
onethreenine(number)
