# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message.
# If the score is between 0.0 and 1.0, print a grade using the following table:

#  Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F

# ----------------------------------------------------
# SAMPLE EXECUTION
# ----------------------------------------------------
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F
# ----------------------------------------------------

# ----------------------------------------------------
# MY EXECUTION
# ----------------------------------------------------

# define variable score based on user input
score = input('Enter score: ')

# try and except error message on bad user input as string. If error true quits at line 19.
try:
    score = float(score)
except:
    print('Bad score')
    quit()

# if score less than 0.0 or greater than 1.0 is true than print error message
if score < 0.0 or score > 1.0:
    print('Bad Score')
# if above is false than print letter grade based on grading table
elif score >= 0.9:
    print('A')
elif score >= 0.8 and score < 0.9:
    print('B')
elif score >= 0.7 and score < 0.8:
    print('C')
elif score >= 0.6 and score < 0.7:
    print('D')
elif score < 0.6:
    print('F')
