#!/usr/bin/Python27

#JadaLewis 6/9/22

#Function to find the smallest positive integer missing from a given number list


def find_missing_posint(number_lst):

	if type(number_lst) != list:
		exit('Error: Check input')

	for i in range(0,len(number_lst)):
		if type(number_lst[i]) != int:
			exit('Error: List values must be integers')


	print 'Input= ' + `number_lst`

	number_lst.sort()

	number_lst_unique_pos = []

	for i in range(0,len(number_lst)):
		if number_lst[i] > 0 and number_lst[i] not in number_lst_unique_pos:
			number_lst_unique_pos.append(number_lst[i])

	
	present = [number_lst_unique_pos[0]]

	absent = []

	for i in range(1,len(number_lst_unique_pos)-1):
		if number_lst_unique_pos[i] == number_lst_unique_pos[i-1] + 1:
			present.append(number_lst_unique_pos[i])
		elif number_lst_unique_pos[i] != number_lst_unique_pos[i-1] + 1:
			present.append(number_lst_unique_pos[i])
			absent.append(number_lst_unique_pos[i-1] + 1)
	
	result = min(absent)

	print 'The smallest positive integer missing from the input list is ' + str(result) + '\n'


#Test the fxn

find_missing_posint([-2,6,5,4,-1,7,1,3,6,6,-2,9,10,2,2])