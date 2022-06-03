#!/usr/bin/Python27

#JadaLewis 6/3/22

def sort_byLetters(lst):

	if type(lst) != list:
		exit('Error: Check Input')

	for i in range(0,len(lst)):
		if type(lst[i]) != str:
			exit('Error: Check Input')

	print 'Input= ' + `lst`

	alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


	lst_new = []

	for i in range(0,len(lst)):
		for n in range(0,len(lst[i])):
			if lst[i][n] in alphabet:
				lst[i][n].lower()
				lst_new.append((lst[i][n],lst[i]))

	lst_new_dict = dict(lst_new)
	
	lst_new_dict_keys = lst_new_dict.keys()

	lst_new_dict_keys.sort()


	final = []

	for key in lst_new_dict_keys:
		final.append(lst_new_dict[key])

	print 'Output= ' + `final` + '\n'


#Test the fxn

sort_byLetters(['932c','832u32','2344b'])
sort_byLetters(['99a','78b','c2345','11d'])
sort_byLetters(['572Z','5y5','304q2'])