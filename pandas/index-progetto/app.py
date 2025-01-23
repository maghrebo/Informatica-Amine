import pandas as pd 

# Creazione del dizionario con chiave-valore, dandogli come valore una lista (una mia scelta dichiararlo così ci sono altri metodi)
studenti = {
    "NOMI": ['Amine', 'Ginevra', 'Sofia', 'Chiara', 'Abdul'],
    "MATEMATICA": [7, 8, 8, 7, 5],
    "CHIMICA": [8, 7, 7, 6, 9],
    "ITALIANO": [7, 8, 8, 8, 5]
}

# Creazione del dataframe (df per abbrevviazione generale) utilizzando il dizionario creato in precedenza
df = pd.DataFrame(studenti)


# Stampa in diversi modi per la verifica del funzionamento
print('---------------------------------------------------------------------------------------------------------- STAMPA COMPLETA')
print(df)
print('---------------------------------------------------------------------------------------------------------- STAMPA DELLE PRIME 3 RIGHE')
print(df.head(3))
print('---------------------------------------------------------------------------------------------------------- STAMPA DELLE STATISTICHE PER OGNI RIGA')
print(df.describe())




# ------------------------ ESERCIZIO RIEPILOGATIVO ------------------------------------------

# Creazione del dizionario chiave-valore
dati = {
    "NOME": ['Amine', 'Astor', 'Christian', 'Riccardo', 'Maneth', 'Tommaso'],
    "ETÁ": [18, 18, 18, 20, 18, 18],
    "MEDIA": [7.20, 7.75, 6.80, 7.15, 7.55, 8.15]
}

# Modifica e Creazione del dataframe prendendo il dizionario 'dati'
df = pd.DataFrame(dati)

# Stampa in diversi modi per la verifica del funzionamento
print('------------------------------------------------------------------------- CAMBIO DI DATAFRAME -----------------------------------------------------------------')
print('---------------------------------------------------------------------------------------------------------- STAMPA COMPLETA')
print(df)
print('---------------------------------------------------------------------------------------------------------- STAMPA DELLE ULTIME 2 RIGHE')
print(df.tail(2))
print('---------------------------------------------------------------------------------------------------------- STAMPA DELLE INFORMAZIONI PER IL DATAFRAME')
print(df.info())