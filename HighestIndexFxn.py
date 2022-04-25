#!/usr/bin/Python27

#JL 4/25/22

#Function to return the letter with the highest alphabet index of a given string

def highest_index(word):
	
	if type(word) != str:
		exit('Error: Input value must be a string')

	print 'Input string = ' + word

	alphabet = 'abcdefghijklmnopqrstuvwxyz'

	alphabet_lst = list(alphabet)
	
	L=[]

	for letter in word:
		letter_index = alphabet.index(letter)
		L.append([letter_index,letter])

	dictionary = dict(L)

	k_sort = sorted(dictionary.keys())
	
	highest = str(k_sort[len(k_sort)-1]) + dictionary[k_sort[len(k_sort)-1]]

	print highest


#test the fxn

highest_index('function')