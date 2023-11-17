#program tworzy tabele i dodaje pytania do pliku csv
import pandas as pd

df=pd.DataFrame()
df['Pytanie']=['Jak ma na imię Sebastian?']
df['Odpowiedz A']=['Sebastian']
df['Odpowiedz B']=['Kamil']
df['Odpowiedz C']=['Piotr']
df['Odpowiedz D']=['Paweł']
df['Prawidlowe_odp']=['A']


df.loc[len(df)]={
        'Pytanie':'Ile to 2+2?',
        'Odpowiedz A':'2',
        'Odpowiedz B':'3',
        'Odpowiedz C':'4',
        'Odpowiedz D':'5',
        'Prawidlowe_odp':'C'
    }
df.loc[len(df)]={
        'Pytanie':'Co jest stolicą polski?',
        'Odpowiedz A':'Katowice',
        'Odpowiedz B':'Warszawa',
        'Odpowiedz C':'Barcelona',
        'Odpowiedz D':'Madryt',
        'Prawidlowe_odp':'B'
    }


df.to_csv('Pytania.csv')