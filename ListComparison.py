#!/usr/bin/Python27

#JL 6/4/21

#Create and print two lists of random numbers and the length of each list

from random import randint

a = randint(1,25)
print a
lst_a = []
for i in range(a):
	lst_a.append(randint(0,i))
lst_a.sort()
print lst_a

print

b = randint(1,25)
print b
lst_b = []
for i in range(b):
	lst_b.append(randint(0,i))
lst_b.sort()
print lst_b

print


#Compare the list a with list b
#Use the shorter list as the comparator
#Create and print a list of numbers that are the same in both lists without duplicates

lst_a_new = []
lst_b_new = []
if len(lst_a) > len(lst_b):
	for i in range(len(lst_b)):
		if lst_b[i] in lst_a and lst_b[i] != lst_b[i-1]:
			lst_b_new.append(lst_b[i])
	print lst_b_new
elif len(lst_a) < len(lst_b):
	for i in range(len(lst_a)):
		if lst_a[i] in lst_b and lst_a[i] != lst_a[i-1]:
			lst_a_new.append(lst_a[i])
	print lst_a_new
