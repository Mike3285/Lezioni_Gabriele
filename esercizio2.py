# input una lista di numeri ritorna solo quelli pari
# 1,2,3,4,5,6,7,8,9,10

print('inserisci una lista di numeri separati da virgole')
first_list = input('>>>')
# print(first_list)

iterable_list = first_list.split(',')
# print(iterable_list)

int_list = []
for e in iterable_list:
    a = int(e)
    int_list.append(a)

# print(int_list)

for i in int_list:
    if i % 2 == 0:
        print(i)
    else:
        pass




