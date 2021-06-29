# prendi una stringa da input e rimuovi la lettere all'index richiesto dal secondo input

print('Insert a string')
input_string = input('>>>')
print('Chose an index')
string_index = int(input('>>>'))

string_list = list(input_string)
new_list = string_list.pop(string_index)

final_string = ''
for e in string_list:
    final_string = final_string + e

print(final_string)