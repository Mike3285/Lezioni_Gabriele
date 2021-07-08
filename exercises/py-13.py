# Write a py prgram to tell if the string is palindromo (reverse)
import string


def is_palindrome(porco_cane: str):
    for i in string.punctuation:
        if i in porco_cane:
            porco_cane = porco_cane.replace(i, "")

    porco_cane = porco_cane.replace(" ", "")
    lista_lettere = list(porco_cane)
    lista_contraria = lista_lettere.copy()
    lista_contraria.reverse()
    if lista_contraria == lista_lettere:
        print('E palindromo')
        return True
    else:
        print('Non e palindromo')
        return False
