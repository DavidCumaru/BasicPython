# > CONDITIONAL STRUCTURE

age = 20

if age >= 18:
    print('You are of legal age.')
else:
    print('you are underage.')

"""
Imagine that you want to print "Approved", if the student has an average greater than or equal to 7, and "Disapproved", if the average is less than 7.
"""

average = float(input('Enter student average: '))

if average >= 7:
    print('You were approved!!')
elif average >=5:
    print('The student must recover the grade!')
else:
    print('You failed!')

average = 10
presence = 100

if average >= 7 and presence >= 70:
    print('Approved!')
else:
    print('Disapproved!')
