#!/usr/bin/python27

#JadaLewis 7/8/22

#Function to check if a given input string1 can be built from string2

def can_build(txt1,txt2):

	if type(txt1) != str and type(txt2) != str:
		exit('Error: Input values must be strings')

	print 'Input = ' + txt1 + ' , ' + txt2 + '\n'

	txt1_lc = txt1.lower()
	txt2_lc = txt2.lower()

	lst_txt1 = list(txt1_lc)
	lst_txt2 = list(txt2_lc)

	lst_txt1_unique = []

	for i in range(0,len(lst_txt1)):
		if i not in lst_txt1_unique:
			lst_txt1_unique.append(i)

	total = 0

	for i in range(0,len(lst_txt1_unique)):
		if lst_txt2.count(i) == lst_txt1.count(i) or lst_txt2.count(i) > lst_txt1.count(i):
			total += 1

	if total == len(lst_txt1_unique):
		print '\''+ txt1 + '\'' + ' can be built from the letters in ' + '\''+ txt2 + '\''
		return True
	elif total != len(lst_txt1_unique):
		print '\''+ txt1 + '\'' + ' can not be built from the letters in ' + '\''+ txt2 + '\''
		return False


#Test the fxn

can_build('Data Analyst','Data Science Analyst')