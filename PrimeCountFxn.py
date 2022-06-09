#!/usr/bin/Python27

#JadaLewis 6/9/22

#Function to calculate the prime numbers ranging from 1 through a given number n

def is_prime(n):
	
	if type(n) != int:
		exit('Error: Check input')

	result = 0

	for i in range(1,n+1):
		if n % i == 0:
			result += 1
		elif n % i != 0:
			result += 0

	if n == 1:
		return True
	elif n > 1 and result == 2:
		return True
	elif n > 1 and result > 2:
		return False


def count_prime(n):

	if type(n) != int:
		exit('Error: Check input')
	elif n == 0:
		exit('Error: Input value must be greater than 0')

	print 'Input= ' + str(n)

	result = 0

	number = 1

	primes = []

	while result < n:

		if is_prime(number) == True:
			result += 1
			primes.append(number)

		number += 1
	
	if n == 1:
		print 'The first prime number is: ' + `primes` + '\n'
	elif n > 1:
		print 'The first ' + str(n) + ' prime numbers starting with 1 are: ' + `primes` + '\n'


#Test the fxn

count_prime(1)

count_prime(10)

count_prime(20)