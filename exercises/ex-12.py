# Transform ex-2.py into a def


def paycalc(a, b):
    '''
    a function to calculate total pay based on hours and pay rate
    :param a: total hours worked
    :param b: pay per hour
    :return: resulting pay
    '''

    pay = (a * b)
    return pay

print('Enter your hours worked and your pay rate')

hours = float(input('Hours: '))
rate = float(input('Rate: '))

print(paycalc(hours, rate))
