#!/usr/bin/Python27

#JadaLewis 6/9/22

#Function to determine the day of the week n days from a given day

def n_days(wkday,n):

	if type(wkday) != list:
		exit('Error: Check input')

	print 'Input= ' + `wkday` + ',' + str(n) + '\n'


	d = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

	r = n % 7


	for i in range(0,len(wkday)):
		
		print 'Today is ' + wkday[i]
		strt_pos = d.index(wkday[i])
		
		if n < 7 and n + strt_pos < 6:
			end_pos = d[strt_pos + n]
		elif n < 7 and n + strt_pos > 6:
			a = 6 - strt_pos
			b = r - a
			end_pos = d[b-1]
		elif (n == 7 or n > 7) and r == 0:
			end_pos = d[strt_pos]
		elif (n == 7 or n > 7) and r != 0:
			a = 6 - strt_pos
			b = r - a
			end_pos = d[b-1]
		elif (n == 7 or n > 7) and r != 0 and r + strt_pos > 6:
			end_pos = d[strt_pos + r]
		
		print 'In ' + str(n) + ' days, it will be ' + end_pos + '\n'


#Test the fxn

n_days(['Thursday','Tuesday'],13)