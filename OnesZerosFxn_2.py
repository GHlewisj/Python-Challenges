#!/usr/bin/Python27

#JadaLewis 6/4/22

#Function to extract consecutive 1's and 0's from a given string of 1's and 0's, and check if there are consecutive 1's followed by consecutive 0's of the same length

import re

def ones_zeros(number_seq):

	if type(number_seq) != str:
		exit('Error: Check input')

	for i in range(0,len(number_seq)):
		if number_seq[i] not in '10':
			exit('Error: Check input')


	print 'Input= ' + number_seq

	
	run_of_ones = []

	run_of_zeros = []
	
	number_seq_lst = list(number_seq)
	
	number_seq_new = ''
	for i in range(0,len(number_seq)-1):
		if number_seq[i] == number_seq[i+1]:
			number_seq_new += number_seq[i] 
		elif number_seq[i] != number_seq[i+1]:
			number_seq_new += number_seq[i]
			number_seq_new += '-'
	number_seq_new += number_seq[len(number_seq)-1]


	number_seq_new_2 = re.split('-', number_seq_new)
	

	for i in range(len(number_seq_new_2)):
		if '1' in number_seq_new_2[i]:
			run_of_ones.append(number_seq_new_2[i])
		elif '0' in number_seq_new_2[i]:
			run_of_zeros.append(number_seq_new_2[i])


	if run_of_ones != []:
		print 'The consecutive 1\'s are ' + `run_of_ones`
	elif run_of_ones == []:
		print 'There are no consecutive 1\'s in the sequence'

	if run_of_zeros != []:
		print 'The consecutive 0\'s are ' + `run_of_zeros`
	elif run_of_zeros == []:
		print 'There are no consecutive 0\'s in the sequence'

	
	run_of_ones_zeros = []

	for i in range(len(number_seq_new_2)-1):
		if '1' in number_seq_new_2[i] and len(number_seq_new_2[i]) == len(number_seq_new_2[i+1]):
			run_of_ones_zeros.append([number_seq_new_2[i],number_seq_new_2[i+1]])
	
	
	if run_of_ones_zeros != []:
		print 'The consecutive 1\'s w/ repeating 0\'s of the same length are ' + `run_of_ones_zeros`
	elif run_of_ones_zeros == []:
		print 'There are no consecutive 1\'s w/ repeating 0\'s of the same length'


#Test the fxn

ones_zeros('1111001100')