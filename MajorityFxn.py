#!/usr/bin/Python27

#JL 4/22/22

#Function to determine the majority element of a list

import random

def majority(L):
	
	print 'Input = ' + `L`
	
	if type(L) != list:
		exit('Error: Input must be a list')

	elif len(L) < 2:
		exit('Error: Input list must contain 2 or more elements')

	
	L.sort()
	
	L_count = []


	#Count unique eLements in the list

	for i in range(0,len(L)-1):
		if L[i] != L[i+1]:
			count = L.count(L[i])
			L_count.append((L[i],count))

	if L[len(L)-1] != L[len(L)-2] or L[len(L)-1] == L[len(L)-2]:
		count = L.count(L[len(L)-1])
		L_count.append((L[len(L)-1],count))

	
	#Convert the list to a dictionary and check for majority

	dictionary_count = dict(L_count)
	
	N = len(L)
	
	result = 0

	for element in dictionary_count:
		if dictionary_count[element] > N/2:
			print 'Majority = ' + element
			result += 1

		else:
			result += 0

	if result == 0:
		print 'There is no majority'


#Create a randomly generated list and test the fxn

vowels = 'AEIOU'

test_list = []

for i in range(1,random.randint(2,6)):
	test_list.append(random.choice(vowels))

majority(test_list)