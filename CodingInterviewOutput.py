#!/usr/bin/Python27

#JL 5/2/22

#Function to evaluate a job applicant given a list of times L for each question and total time of interview completion
#Write results for each applicant to file

#question format [very easy, very easy, easy, easy, medium, medium, hard, hard]
   #The candidate should have complete all the questions.
   #The maximum time given to complete the interview is 120 minutes.
   #The maximum time given for very easy questions is 5 minutes each.
   #The maximum time given for easy questions is 10 minutes each.
   #The maximum time given for medium questions is 15 minutes each.
   #The maximum time given for hard questions is 20 minutes each.

outfile = open('coding_interview_output.xls' , 'w')

outfile.write('Applicant \t very easy \t very easy \t easy \t easy \t medium \t medium \t hard \t hard \t completion_time \t result \t comment \n')


def interview(L,time_total):
	
	if type(L) != list or type(time_total) != int:
		exit('Error: Incorrect input value types')

	for i in range(0,len(L)):
		outfile.write(`L[i]` + '\t')
	

	if len(L) < 8:
		#print 'Disqualified: All questions not completed \n'
		missing = 8 - len(L)
		sep = '\t' * missing
		outfile.write(sep + str(time_total) + '\t')
		outfile.write ('Disqualified \t All questions not completed \n')

	elif time_total > 120:
		#print 'Disqualified: Time limit for completion exceeded \n'
		outfile.write(str(time_total) + '\t')
		outfile.write ('Disqualified \t Time limit for completion exceeded \n')

	elif L[0] > 5 or L[1] > 5:
		#print 'Disqualified: Time limit for questions 1 and 2 exceeded \n'
		outfile.write(str(time_total) + '\t')
		outfile.write ('Disqualified \t Time limit for questions 1 and 2 exceeded \n')

	elif L[2] > 10 or L[3] > 10 :
		#print 'Disqualified: Time limit for questions 3 and 4 exceeded \n'
		outfile.write(str(time_total) + '\t')
		outfile.write ('Disqualified \t Time limit for questions 3 and 4 exceeded \n')

	elif L[4] > 15 or L[5] > 15:
		#print 'Disqualified: Time limit for questions 5 and 6 exceeded \n'
		outfile.write(str(time_total) + '\t')
		outfile.write ('Disqualified \t Time limit for questions 5 and 6 exceeded \n')

	elif L[6] > 20 or L[7] > 20:
		#print 'Disqualified: Time limit for questions 7 and 8 exceeded \n'
		outfile.write(str(time_total) + '\t')
		outfile.write ('Disqualified \t Time limit for questions 7 and 8 exceeded \n')

	elif len(L) == 8 and L[0] <= 5 and L[1] <= 5 and L[2] <= 10 and L[3] <= 10 and L[4] <= 15 and L[5] <= 15 and L[6] <= 20 and L[7] <= 20:
		#print 'Qualified \n'
		outfile.write(str(time_total) + '\t')
		outfile.write ('Qualified \n')


#Test the fxn
outfile.write ('1 \t')
interview([5, 5, 10, 10, 15, 15, 20, 20], 120)
outfile.write ('2 \t')
interview([2, 3, 8, 6, 5, 12, 10, 18], 64)
outfile.write ('3 \t')
interview([5, 5, 10, 10, 25, 15, 20, 20], 120)
outfile.write('4 \t')
interview([5, 5, 10, 10, 15, 15, 20], 120)
outfile.write('5 \t')
interview([5, 5, 10, 10, 15, 15, 20, 20], 130) 

outfile.close()