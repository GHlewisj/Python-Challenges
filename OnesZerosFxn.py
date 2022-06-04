#!/usr/bin/Python27

#JadaLewis 6/4/22

#Function to extract the consecutive 1's from a given string of 1's and 0's

def ones_zeros(number_seq):

	if type(number_seq) != str:
		exit('Error: Check input')

	for i in range(0,len(number_seq)):
		if number_seq[i] not in '10':
			exit('Error: Check input')


	print 'Input= ' + `number_seq`


	ones = []

	for i in range(0,len(number_seq)):
		if number_seq[i] == str(1):
			ones.append(i)


	ones_2 = [ones[0]]

	ones_3 = []
			
	for i in range(0,len(ones)-1):
		if ones[i+1] == ones[i] + 1:
			ones_2.append(ones[i+1])
			ones_3.append(ones_2)
		elif ones[i+1] != ones[i] + 1:
			ones_2 = [ones[i+1]]

		
	ones_4 = []

	for i in range(0,len(ones_3)):
		if ones_3[i] not in ones_4:
			ones_4.append(ones_3[i])


	run_of_ones = []

	for i in range(0,len(ones_4)):
		run_of_ones.append(number_seq[ones_4[i][0]:(ones_4[i][len(ones_4[i])-1])+1])

	
	print '1\'s occur at positions ',

	for i in range(0,len(ones)):
		print ones[i] ,

	if run_of_ones != []:
		print '\nThe consecutive 1\'s are ' + `run_of_ones` + '\n'
	elif run_of_ones == []:
		print 'There are no consecutive 1\'s in the sequence(s) \n'



#Test the fxn	

ones_zeros('111100111000')