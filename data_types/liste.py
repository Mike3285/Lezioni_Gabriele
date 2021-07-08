# LE LISTE
# Definizione: Una lista è un insieme ordinata di elementi, ognuno identificato da un indice.
# Su python è rappresentata dagli elementi separati da virgole e chiusi tra []

#### CREARE UNA LISTA

# Assegnazione diretta

#   i           0        1       2
mia_lista = ["ciao", "prova", "test"]
#  -i         -3       -2       -1

# Funzione di creazione

mia_lista2 = list()  # Creerà una lista vuota, accetta un iterabile per creare la lista a partire da un iterabile

# NB: Iterabile è qualsiasi elemento si possa esprimere come una "collezione" o un "insieme" di sottoelementi
# Adesso mialista2 = []

# Operazioni di base
# Aggiungi elemento

mia_lista2.append("qualcosa")

# Rimuovi elemento (rimuove la prima istanza che trova dell'elem che gli dai)

mia_lista2.remove("qualcosa")

# "pop" -- "Prendi e tira via" -- Prende un elemento alla posizione N dalla lista e lo rimuove, ma la funzione lo ritorna
n = 1
elemento_rimosso = mia_lista2.pop(n)

## OPERAZIONI FONDAMENTALI
# sommma di liste

c = [1, 2, 3] + [2, 5, 7]

# produrrà   [1, 2, 3, 2, 5, 7]

# NON SI PUò FARE IL CONTRARIO [1, 2, 3 , 4, 5] - [1, 2, 3]

# Check di contenuto

d = [1, 2, 3, "cane"]
# Con "in" possiamo verificare che l'elemento a sx dell'"in" sia contenuto nell'iterabile a dx, risponde con un bool
x = 2 in d

## ACCESSO AGLI ELEMENTI

# Per accedere a un elemento uso la sintassi mia_lista[indice_che_mi_serve]     mia_lista[i]

#   i           0        1       2
prova_lista = ["ciao", "prova", "test"]
#  -i         -3         -2       -1

# per accedere a "prova" posso individuare il suo indice e usare il metodo descritto sopra

elemento_che_voglio = prova_lista[1]
elemento_che_voglio = prova_lista[-2]
# queste due diciture sono equivalenti, sto solo prendendo l'elemento partendo a contare gli indici dall'inizio o dalla fine

# Posso riassegnare un valore "prendendolo" come qui sopra e usando l'operatore di assegnazione "="

prova_lista[1] = "gatto"

# ora  prova_lista è ["ciao", "gatto", "test"] perchè ho riassegnato il valore presente al suo index 1


# Se invece mi servisse una "sottolista" di una lista, posso usare lo "slicing" ovvero la posso "affettare"
# Per affettare una lista specifico l'indice da cui voglio iniziare il mio "taglio" e quello a cui il taglio deve terminare, separandoli con :
# Esempio: mia_lista[a:b]
# Indice iniziale è incluso, indice finale escluso

#                     0    1    2    3    4    5
lista_da_tagliare = ['a', 'b', 'c', 'd', 'e', 'f']
#                    -6   -5   -4   -3   -2   -1

sottolista_da_b_a_e = lista_da_tagliare[1:5]

# Se non specifico uno dei due indici, la lista verrà affettata da quell'i in poi o fino a quell'i

mezza_lista = lista_da_tagliare[3:]        # da 3 in poi
altra_mezza_lista = lista_da_tagliare[:3]  # fino a 3
# coi meno avrei ottenuto il risultato sempre verso "destra"

# LUNGHEZZA DI UNA LISTA
# Per python è facile sapere quanti elementi contiene una lista, il calcolo impiega tempo identico indipendentemente
# dal numero di elementi contenuti perchè va a vedersi direttamente quanta memoria occupa

# per ottenere la lunghezza di una lista si usa "len()"

squadre = ["Juventus", "Inter", "Milan", "Roma"]
len(squadre)    # mi ritornerà un intero, 4

# ESEMPIO
# Provo a trovare la metà di una lista di cui non conosco il numero di elementi
# Uso len per trovare quanti elementi contiene
# L'intero dato dalla lunghezza della lista / 2 sarà uguale all'indice dell'elemento presente a metà lista!

lista_indefinita = list()

lunghezza_lista_indefinita = len(lista_indefinita)   # intero
indice_di_mezzo = int(lunghezza_lista_indefinita/2)

# NB notare i ":" che servono ad ottenere la fetta da quell'index in poi
mezza_lista_indefinita = lista_indefinita[indice_di_mezzo :]






