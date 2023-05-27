#!/usr/bin/python38

#JL 5/14/23

#Function to calculate the sum of the negative integers contained within a string of chars

def negative_sum(word):

	if type(word) != str:
		exit('Error: Input must be a string')

	word = word.split()

	count = 0
	neg = []

	for i in range(0,len(word)):

		if '-' in word[i]:
			#print (word[i])
			neg.append(int(word[i]))
			count += int(word[i])

	
	for i in range(0,len(neg)-1):
		print (str(neg[i]) + ' + ', end='')

	print (str(neg[len(neg)-1]) + ' = ' + str(count))


#Test the fxn
	
negative_sum('& 6 $ -11 0 !^ -2 -6')