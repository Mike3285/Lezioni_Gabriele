# Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit, and print out the converted temperature.

# define a ctemp variable based on user input
ctemp = input('Enter temperature in Celsius degrees: ')

# convert the ctemp input into a float type
ctemp = float(ctemp)

# define the variable ftemp based on the conversion formula
ftemp = (ctemp * 9/5) + 32

# print output as a string and the ftemp
print('In Fahrenheit degrees that is:',ftemp)
