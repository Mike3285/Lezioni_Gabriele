# data una frase e una sola lettera print la parte di stringa prima della lettera

print('Insert a string')
input_string = input('>>>')

print('Insert a character')
input_char = input('>>>')

final_string = input_string.split(input_char)
print(final_string[0])