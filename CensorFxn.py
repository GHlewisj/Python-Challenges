#!/usr/bin/Python27

#JL 4/25/22

#Function to replace substrings of a string with a given char

def censor(sentence,L,sub_char):

	if type(sentence) != str or type(L) != list or type(sub_char) != str:
		exit('Error: Check input value types')
	
	L2 = []

	L3 = []

	for i in range(0,len(L)):
		start_pos = sentence.find(L[i])
		end_pos = start_pos + len(L[i])
		L2.append(start_pos)
		L3.append(end_pos)

	#print L2
	#print L3
	

	for i in range(0,len(L3)):
		sentence = sentence.replace(sentence[L2[i]:L3[i]], sub_char*len(sentence[L2[i]:L3[i]]))
		
	print sentence


#Test the fxn
	
censor('Today is not Wednesday', ['Today','not'], '-')