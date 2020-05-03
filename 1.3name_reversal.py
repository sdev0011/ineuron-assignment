''' Write a Python program to accept the user's first and last name and 
then getting them printed in
the the reverse order with a space between first name and last name.'''

first = input('first name :')
last = input('last name:')

print(first[::-1]+" "+last[::-1])


''' output
sdev@satyam MINGW64 ~/Desktop/Ineuron pythoon/1st assignment (master)
$ python name_reversal.py
first name :satyam
last name:mishra
maytas arhsim
'''