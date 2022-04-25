#!/usr/bin/Python27

#JL 8/17/21

#Function to convert the values in a list to integers

def convertlist(n):
	n_new=[]
	for i in range(0,len(n)):
		item_new=int(n[i])
		n_new.append(item_new)
	return n_new


with open('prime.txt', 'r') as prime:

	prime_lines = prime.read()
	lst_prime = prime_lines.split('\n')
	lst_prime_new = convertlist(lst_prime)
	lst_prime_new.sort()

with open('happy.txt', 'r') as happy:

	happy_lines = happy.read()
	lst_happy = happy_lines.split('\n')
	lst_happy_new = convertlist(lst_happy)
	lst_happy_new.sort()


#Compare list prime with list happy
#Use the shorter list as the comparator
#Create and print a list of numbers that are the same in both lists without duplicates

lst_new = []

if len(lst_prime_new) > len(lst_happy_new):
	for i in range(len(lst_happy_new)):
		if lst_happy_new[i] in lst_prime_new and lst_happy_new[i] != lst_happy_new[i-1]:
			lst_new.append(lst_happy_new[i])

elif len(lst_prime_new) < len(lst_happy_new):
	for i in range(len(lst_prime_new)):
		if lst_prime_new[i] in lst_happy_new and lst_prime_new[i] != lst_prime_new[i-1]:
			lst_new.append(lst_prime_new[i])
print lst_new


