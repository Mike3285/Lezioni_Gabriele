# I SET
# Definizione: Un set è un insieme di elementi, disordinato e mutabile, ma molto efficiente e veloce

# CREAZIONE

mioset_a = {1, 2, 3, 4}  # per assegnazione diretta
mioset_b = set()  # Usando la funzione generatrice

# Ma non posso crearne uno vuoto:
mioset_vuoto = {}  # Creerà un dizionario vuoto!

# Con almeno un elemento e una virgola, creerà un set (non vedendo i ":" gli sarà chiaro che è un set e non un dict!)
mioset_c = {1, }  # set

# Gli elementi di un set sono e devono essere UNICI. Se un iterabile con elementi ripetuti viene trasformato in un set,
# il set risultante avrà una sola istanza dell'elemento che si ripete

mioset_d = {1, 2, 3, 4, 4, 4, 5}  # possiamo anche assegnarlo se vogliamo...
# ... ma sarà uguale a {1, 2, 3, 4, 5}!

# Un set quindi può essere molto utile per trovare gli elementi unici di un qualcosa!

mialista = [1, 2, 3, 4, 5, 34, 5, 6, 7, 3, 34, 4, 56, 2, 1]

set_mialista = set(mialista)  # trasformo in un set

unici_mialista = list(set_mialista)  # ritrasformo in lista
print(unici_mialista)  # printa [1, 2, 3, 4, 5, 34, 6, 7, 56]


# Più velocemente, in una riga posso anche fare:
mialista_b = [1, 5, 23, 4, 12, 23, 21, 1, 21, 2, 12, 12, 23]
#Trasformo in set e ritrasformo in lista
unici_b = list(set(mialista_b))


# Gli elementi di un set sono DISORDINATI e PRIVI DI INDICE, possiamo comunque iterare su di loro ma non possiamo uasre
# gli indici per accedere agli elementi o a dei sub-set (slicing)

# Posso aggiungere due set tramite operatore di intersezione
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x3 = x1 | x2
# x3 corrisponderà a {'baz', 'quux', 'qux', 'bar', 'foo'}

# il metodo .intersection invece ci tornerà un set contenente gli elementi comuni tra il set su cui viene chiamato e
# e quello dato in pasto al metodo
x4 = x1.intersection(x2)
# x4 corrisponderà a {"baz"}


# il metodo .difference invece ci tornerà un set contenente gli elementi NON comuni tra il set su cui viene chiamato e
# e quello dato in pasto al metodo
x5 = x1.difference(x2)
# x5 -> {'foo', 'bar'}

# se vogliamo invece gli elementi NON comuni tra entrambi, quindi sia su x1 che su x2, useremo il metodo ".symmetric_differece"

# Possiamo comunuqe utilizzare len() per calcolarne il numero di elementi contenuti

# si usano quando abbiamo necessità di performance e non ci interessa l'ordine degli elementi o mantenere i duplicati


# RICORDA .pop funziona anche sui set, ma non avendo indici o key a cui fare riferimento, rimuove un elemento casuale!