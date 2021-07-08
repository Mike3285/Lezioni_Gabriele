# DEFINIZIONE: Una funzione è un pezzetto di codice che viene riprodotto, magari perché lo usiamo più volte o comunque
# per non ripetere mai quello che scriviamo.

# Una funzione è composta da un nome e dei parametri.
# Per creare una funzione dobbiamo usare la parola chiave "def" seguita dal nome che vogliamo dare alla funzione e
# da un paio di ().

# Le () opzionalmente possono contenere eventuali parametri che possiamo dare alla funzione.
# Un parametro è una variabile che viene passata all'interno della funzione.

# Possiamo dargli un nome arbitrario, ma quando chi usa il nostro programma lo eseguirà, il parametro prenderà il valore
# che l'utilizzatore gli da quando chiama la funzione

def saluto(nome="Qualcuno"):
    # Nome in questo momento non è definito. Però possiamo costruire la funzione "immaginando" che nome sia una stringa!
    # Se poi l'utente ci darà una stringa andrà tutto bene, se no darà errore

    print(f"Ciao {nome}!!!")


saluto("Mario")

saluto()


# In questo caso "nome" nella nostra funzione assumerà il valore di "mario", quindi tutto il codice
# contenuto nella nostra funzione sarà eseguito con "mario" al posto di nome


def fai_divisione(n1=10, n2=2):
    # Ai parametri posso dare dei nomi a piacimento, che esisteranno solo all'interno della mia funzione.

    # Quando verrà chiamata il ogni parametro assumerà il valore che gli viene passato durante la chiamata rispettando l'ordine

    # Posso eventualmente specificare con un = un valore predefinito che deve assumere questo parametro nel momento in cui
    # la funzione viene chiamata senza specificarlo.

    # Se non specifico alcun parametro predefinito e chiamo la funzione con un parametro in meno essa andrà in errore

    # Quando la chiamo, posso cambiare l'ordine dei suoi parametri se so come li ho chiamati nella definizione, richiamandoli per nome con l'uguale

    print("i numeri sono", n1, n2)
    if n2 == 0:
        print("Per favore inserire un numero diverso da 0 come divisore")

    else:
        u = n1 / n2
        # Per farmi anche ridare indietro il valore devo usare una nuova parola chiave "return"
        return u
        # Questo statement fa sì che la funzione, quando chiamata, abbia il valore di ritorno definito dopo return


# ESEMPI
fai_divisione()             # Assumerà i valori predefiniti
fai_divisione(10)           # Il primo valore assumerà 10, il secondo il val predefinito
fai_divisione(25, 5)        # Il primo valore assumerà 25, il secondo 5

fai_divisione(n2=5, n1=15)  # Il primo valore sarà 15, il secondo 5
fai_divisione(n2=5)         # Il secondo valore sarà 5, il primo il valore predefinito (10)


# ESTETISMI
# Posso specificare la descrizione di una funzione tramite dei tripli apici subito dopo la func definition
# Questa cosa prende il nome di docstring (stringa di documentazione!) e serve a ricordarmi cosa fa una funzione o a condividere
# il mio codice con altri


def miafunzionediprova(argomento):
    """Questa funzione esegue un print di qualsiasi cosa gli si dia come argomento""" # Questa è la docstring
    print(argomento) # codice interno alla funzione che fa cose


miafunzionediprova()


# Posso anche dare info ai miei colleghi programmatori su cosa una funzione accetti con i :
# e su cosa una funzione ritorni con ->


def funzione_di_prova(argomento) -> int:
    # Qui sto "suggerendo" che l'argomento deve essere un intero e che ritornerò un altro intero
    return argomento * 2
