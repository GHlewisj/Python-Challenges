#!/usr/bin/Python27

#JL 4/21/22

#Function to calculate the product of the factorial of the factorial of a given number n

import random
import time

def factorial(a):
	
	total = a

	for i in range(1,a):
		total *= i

	return total


def fact_of_fact(b):
	
	print 'Input = ' + str(b)

	if b == 1:
		exit('Error: Input must be greater than 1')
	
	total = factorial(b)
	
	for i in range(1,b+1):
		total *=  factorial(i)
	
	data = list(reversed(range(1,b+1)))

	for i in range(0 , len(data)-1):
		print `data[i]` + '! *' ,
	
	print `data[len(data)-1]` + '! ' , 
	
	print '= ' + str(total) + '\n'


#Test the fxn

for i in range(1,6):
	print 'Test ' + str(i)
	time.sleep(1)
	fact_of_fact(random.randint(1,6))
	time.sleep(2)