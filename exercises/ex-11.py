# Write a py function that takes a list of words and returns the longest word and its length


# DA SVOLGERE


def get_longest(lista_parole: list):
    lunghezza_maggiore = 0
    for elemento in lista_parole:
        lunghezza_parola = len(elemento)
        if lunghezza_parola > lunghezza_maggiore: # trovata fin ora
            lunghezza_maggiore = max(lunghezza_parola, lunghezza_maggiore) # mi aggiorni la lunghezza maggiore con quella nuova appena trovata
            parola_maggiore = elemento  # e ti ricordi che parola

    print(f"La stringa più lunga è {parola_maggiore}, composta da {lunghezza_maggiore} caratteri")



def get_longest_in_phrase(frase: str):
    lista_parole = frase.split(' ')
    lunghezza_maggiore = 0
    for elemento in lista_parole:
        lunghezza_parola = len(elemento)
        if lunghezza_parola > lunghezza_maggiore: # trovata fin ora
            lunghezza_maggiore = max(lunghezza_parola, lunghezza_maggiore) # mi aggiorni la lunghezza maggiore con quella nuova appena trovata
            parola_maggiore = elemento  # e ti ricordi che parola

    print(f"La parola più lunga è {parola_maggiore}, composta da {lunghezza_maggiore} lettere")


