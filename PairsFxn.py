#!/usr/bin/Python27

#JadaLewis 6/3/22

#Function to generate a list of pairs utilizing the inner and outer elements a given number list

def pairs(numbers):
	
	if type(numbers) != list:
		exit('Error: Check input')

	for i in range(0,len(numbers)):
		if type(numbers[i]) != int:
			exit('Error: List values can only contain integers')

	print 'Input= ' + `numbers`

	pair_lst = []

	if len(numbers) % 2 != 0:
		for i in range (0,len(numbers)/2):
			pair_lst.append([numbers[i],numbers[len(numbers)-1-i]])
		pair_lst.append([numbers[len(numbers)/2],numbers[len(numbers)/2]])

	elif len(numbers) % 2 ==0:
		for i in range (0,len(numbers)/2):
			pair_lst.append([numbers[i],numbers[len(numbers)-1-i]])

	print 'Output= ' + `pair_lst` + '\n'


#Test the fxn

for i in range(2,9):
	pairs(range(1,i))
