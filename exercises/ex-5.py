# Rewrite your pay program from [ex-4.py] using try and except so that your program handles non-numeric input
# gracefully by printing a message and exiting the program. The following shows two executions of the program:

# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

# define two variables 'total pay' and 'regular rate' based on user input as float
# try and except placed here as this section is blow-up spot. If error quits at line 15.
try :
    toth = float(input('Enter Hours: '))
    regr = float(input('Enter Rate: '))
except :
    print('Error, please enter numeric input')
    quit()

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
