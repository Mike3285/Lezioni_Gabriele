# Write a program to prompt the user for hours and rate per hour to compute gross pay.

# define two variables for hours and rate with user input
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

# define the variable pay, and compute the two variables into float type
pay = float(hours) * float(rate)

# print the string 'Pay:' and the variable pay (no space necessary)
print('Pay:',pay)
