



## 2 tipi di oggetto


 # variabili:  le assegno direttamente a "qualcosa"

variabile = 5  # intero, un numero senza la virgola

parola = "gatto"   #stringa : testo

valore = True  # booleano, può essere true o false

temperatura = 36.7   # float da floating point number, un numero col la virgola

# funzioni -- "Eseguono" cose, sono dinamiche e il risultato che danno può variare su determinate condizioni


input()   # assume il valore dell input dell'user (in stringa)

float()   # fa diventare un float il numero che gli si da (5 --> 5.0)

# alcune funzioni, come print, "fanno cose", questa ad esempio stampa in console ciò che gli viene "dato in pasto"
print()


# le funzioni accettano uno o più PARAMETRI

print("qualcosa")  # printa la stringa "qualcosa"

print(parola, "ciao")  # printerà ognuno degli argomenti, in questo caso la variabile "parola" definita poco sopra e la stringa "ciao"

# le funzioni possono accettare un numero fisso di argomenti oppure anche un numero variabile, dipende dalla funzione
# print ad esempio accetta "n" argomenti, mentre len() ne accetta solo uno

len("ciao")   # ritorna la lunghezza di qualcosa (quanti elementi contiene un insieme, quante lettere ha una stringa)



# I METODI
# sono funzioni che vengono lanciate con come argomento l'oggetto che le "chiama"
# la sintassi per chiamarle è "oggetto.metodo(argomenti)"


"CIAO".isalnum()


x = temperatura/2
