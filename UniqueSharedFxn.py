#!/usr/bin/Python27

#JL 5/9/22

#Function to determine the unique and shared characters between two strings

def unique_letters(word1,word2):

	word1_lst = list(word1)
	word1_lst.sort()

	word2_lst = list(word2)
	word2_lst.sort()

	shared_char = []
	word1_unique = []
	word2_unique = []

	if len(word1_lst) > len(word2_lst):
		
		for i in range(0,len(word2_lst) - 1):
			
			if word2_lst[i] != word2_lst[i+1] and word2_lst[i] in word1:
				shared_char.append(word2_lst[i])
			else:
				word2_unique.append(word2_lst[i])
		
		if word2_lst[len(word2_lst)-1] != word2_lst[len(word2_lst)-2] and word2_lst[len(word2_lst)-1] in word1:
			shared_char.append(word2_lst[len(word2_lst)-1])

		else:
			word2_unique.append(word2_lst[len(word2_lst)-1])

		
		shared_str = ''

		for i in range(0,len(shared_char)):
			shared_str += shared_char[i]
		
		for i in range(0,len(word1_lst)):

			if word1_lst[i] not in shared_str:
				word1_unique.append(word1_lst[i])


	elif len(word2_lst) > len(word1_lst):
		
		for i in range(0,len(word1_lst) - 1):
			
			if word1_lst[i] != word1_lst[i+1] and word1_lst[i] in word2:
				shared_char.append(word2_lst[i])
			else:
				word1_unique.append(word1_lst[i])
		
		if word1_lst[len(word1_lst)-1] != word1_lst[len(word1_lst)-2] and word1_lst[len(word1_lst)-1] in word2:
			shared_char.append(word1_lst[len(word1_lst)-1])

		else:
			word1_unique.append(word1_lst[len(word1_lst)-1])

		
		shared_str = ''
		for i in range(0,len(shared_char)):
			shared_str += shared_char[i]
		
		for i in range(0,len(word2_lst)):

			if word2_lst[i] not in shared_str:
				word2_unique.append(word2_lst[i])


	print 'Input = ' + word1 + '' + word2
	print 'Shared characters = ' + `shared_char`
	print 'Word1 unique characters = ' + `word1_unique`
	print 'Word2 unique characters = ' + `word2_unique`


#Test the fxn

unique_letters('sharp','soap')