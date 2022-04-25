#!/usr/bin/Python27

#JL 4/25/22

#Function to parse an encoded string and convert to a dictionary object

import re

def encoded_parse(sentence):
	
	if type(sentence) != str:
		exit('Error: Input value must be a string')

	sentence_lst = re.split('[0]+' , sentence)

	words = ['first_name' , 'last_name' , 'id']

	L = []

	for i in range(0,len(sentence_lst)):
		L.append([words[i],sentence_lst[i]])

	dictionary = dict(L)

	print dictionary


#test the fxn

encoded_parse('John000Doe000123')

encoded_parse('michael0smith04331')