# Rewrite your pay computation in [ex-2.py] file to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

# define two variables 'total pay' and 'regular rate' based on user input as float
toth = float(input('Enter Hours: '))
regr = float(input('Enter Rate: '))

# define the variable 'regular hours' as 40 hours
regh = 40

# define the variable 'overtime hours' as excess of regular hours
ovth = (toth - regh)

# define the variable 'overtime pay' based on computation
ovtp = ((regh * regr) + (ovth * (regr * 1.5)))

# if statement to print 'overtime pay' if 'total hours' > 40 ; if fasle, print pay based on user inputs
if toth > regh :
    print('Pay:',ovtp)
else :
    print('Pay:',(toth * regr))
