# I DIZIONARI
# Definizione: Una tupla è un insieme di coppie "chiave -> valore", che si usa per rappresentare dati più complessi e
# per accedere agli elementi tramite un collegamento più logico che il solo indice. Le chiavi sono uniche, i valori
# possono anche essere duplicati

# Creazione

# assegnazione diretta

miodiz_a = {"miachiave": "miovalore"}
miodiz_b = {"miachiave": 2}
miodiz_c = {3: "cavolo"}
miodiz_d = {7: "cane", "banana": 15}
miodiz_e = {}  # vuoto, assegnazione diretta
miodiz_f = dict()  # vuoto, assegnazione tramite constructor
# volendo dict accetta anche una lista di tuple, rappresentanti i suoi pair key value
MLB_team = dict(
    [
     ('Colorado', 'Rockies'),
     ('Boston', 'Red Sox'),
     ('Minnesota', 'Twins'),
     ('Milwaukee', 'Brewers'),
     ('Seattle', 'Mariners')
    ]
)
# restrictions: i valori possono essere oggeetti python qualunque, posso dare a ogni valore l'oggetto che voglio
# le chiavi possono essere QUASI tutto quello che voglio: devono per forza essere oggetti IMMUTABILI, quindi non possono
# essere liste, tuple, altri dizionari  o set


# key                    #value che è una lista!
miodiz_g = {"lista_regali": ["auto", "frigorifero", "vestiti"]}
# possiamo usarli per rappresentare anche cose piuttosto complesse!

programmatore = {
    "dati_anagrafici": {
        "nome": "mauro",
        "etò": 25,
    },
    "auto_posseduta": {
        "marca": "volvo",
        "ruote": 4,
        "ABS_presente": True,
    }
}

# Per accedere a un valore "annidato" in un dict, quindi magari a un dict dentro un dict, posso usare la stessa notazione
# che uso per accedere a un elemento
print(programmatore["dati_anagrafici"]["nome"]) # per accedere a "mauro" del dict qui sopra

# Questo è un dict rappresentante un programmatore. Ha due key, i cui value sono altri dizionari, a loro volta composti
# da coppie di key:value!


## ACCESSO AI DATI
# Per accedere a un VALORE di un dizionario, possiamo usare una notazione simile a quella delle liste, solo usando la
# sua key piuttosto che l'indice!

miodiz_h = {"nome": "gabriele", "età": 30}
print(miodiz_h["nome"])  # printerà "gabriele"
# Allo stesso modo, possiamo riassegnare un valore
miodiz_h["nome"] = "mauro"
# Il valore di "nome" è appena stato riassegnato, ora miodiz_h è = a  {"nome":"mauro", "età": 30}

# Questo ci fa anche capire che quindi non possono essere assegnate due key identiche, se ci provo il valore andrà a
# sostituire quello già presente

# I valori possono invece essere ripetuti!
uomo = {"gambe": 2, "braccia": 2}

# Per aggiungere una coppia chiave:valore a un dict possiamo:
# assegnare direttamente la nuova chiave al suo valore
uomo["dita"] = 10
# Oppure usanre il metodo "update", che permette di aggiungere un dizionario a un altro
dati_nuovi = {"capelli": "tanti", "vestiti": 5}
uomo.update(dati_nuovi)  # aggiungerà gli elementi di "dati_nuovi" a "uomo"
# Se nei dati nuovi è presente una KEY uguale, il dato verrà aggiornato

# OPERAZIONI SPECIALI

# Un dict ci permette di accedere a 3 iterabili speciali, uno con tutte le key, uno con tutte le value,
# e uno con le key e le value espresse come tuple! Per accederci possiamo usare i seguenti metodi:
chiavi = uomo.keys()  # conterrà un oggetto list-like con tutte le key
valori = uomo.values()  # conterrà un oggetto list-like con tutti i valori
coppie = uomo.items()  # conterrà tutte le coppie sotto  forma di tupla

# .items() ci permette di iterare in un colpo solo sulle coppie di key value, perchè di norma quando itero su un dict
# con un ciclo di for vengono prese in considerazione solo le KEY!!!
# questa cosa non è valida solo quando itero, ma proprio quando uso il dizionario stesso come iterabile
# la parola chiave "in" ci permette di verificare l'appartenenza di un oggetto a un iterabile

# Oltre a chiamare la value direttamente con miodizionario[key] posso usare anche il metodo .get(key)
# la differenza è che se cerco di accedere tramite miodizionario[key] se non trova la key mi darà errore, mentre se uso get
# mi tornerà il valore di default (che devo fornire io alla funzione)
uomo["gambe"]  # mi tornerà il valore di gambe
uomo["scarpe"] # scarpe non esiste, mi tornerà errore!!!! cosa posso fare?
# posso usare get, per verificare se la key esiste e eventualmente dargli un valore di default da prendersi nel caso che non la trovi
uomo.get("scarpe", 2)   # il primo elemento da dare a get è la key che vorremmo estrarre, il secondo il valore da prendersi se non la trova

# come in una lista possiamo poi anche usare il metodo .pop, solo che al posto che un indice gli daremo in pasto una key
# il metodo pop, come per le liste, rimuove la key corrispondente e la sua value dal nostro dict, ma ce la ritorna,
# permettendoci di salvarla da qualche parte


