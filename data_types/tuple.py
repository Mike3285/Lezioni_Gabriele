# LE TUPLE
# Definizione: Una tupla è un insieme di elementi, con un comportamento molto simile alla lista.
# A differenza di una lista però, non possiamo modificare gli elementi presenti in una tupla, ma possiamo comunque
# modificare la tupla stessa, aggiungendo o rimuovendo elementi

# Creazione

miatupla_a = ()  # Creazione tupla vuota
miatupla_b = (1, 2, 3, 4, 5)  # Creazione di una tupla con alcuni elementi
miatupla_c = tuple()  # Creazione tramite funzione generator

# ATTENZIONE ALLA SINTASSI!
# Per python una cosa tra parentesi è una tupla.... Oppure un operazione matematica, come "2*(9+5)"! Come fa a distinguere?

A = (5)  # La vede come un operazione matematica, print(A) darà fuori 5

B = (5,)  # Con la virgola, la vede come una tupla: print(B) printerà (5,)

# Nulla vieta anche di fare tuple di tuple!

C = ((1, 2, 3), ("a", "b", "c"))  # due tuple, una di interi e una di stringhe, contenute in una tupla

# Operazioni di base
# Aggiungi elemento
# Essendo immutabili non possiamo aggiungere elementi a una tupla, ma possiamo usare un piccolo trucchetto:
# Siccome le tuple supportano l'addizione, possiamo "estendere" una tupla data con gli elementi aggiuntivi che ci interessano
# purche lì mettiamo sempre sotto forma di un altra tupla!!!

tupla_a = ("cane", "gatto", 7)
tupla_b = ("gallina", 5, "auto")

tupla_c = tupla_a + tupla_b  # Questo è valido, tupla_c sarà = a ("cane", "gatto", 7, "gallina", 5, "auto")

### ACCESSO AGLI ELEMENTI

# Possiamo accedere agli elementi di una tupla tramite i loro indici
# 0      1    2
tupla_d = ("gallina", 5, "auto")  # tupla_d[2] sarà "auto"
# ...  Esattamente come per le liste!
## SLICING
# Come per le liste le tuple supportano lo slicing
# tupla_d (1:) ci darà tutti gli elementi da indice 1 in poi quindi (5, "auto")

# Come per le liste, len(miatupla) ci tornerà il numero di elementi contenuti nella tupla.

# Possiamo anche contare quante volte un particolare elemento compare all'interno di una di esse, usando il metodo .count(elemento)

# Possiamo convertire ogni iterabile "compatibile" in una tupla usando il metodo costruttore tuple()

mialista = [1, 2, 3, 4, 5]
miatupla_nuova = tuple(mialista)  # ora è una tupla con gli elementi di mialista

# Perchè tutte queste differenze?
# Non dovendo "ricordare" che ogni elemento potrebbe cambiare, le tuple sono MOLTO più efficienti dal punto di vista delle performance

