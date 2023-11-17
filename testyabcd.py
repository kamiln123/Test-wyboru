#program pobiera z pliku csv pytanie, z odpowiedziami abcd
#po wpisaniu odpowiedzi pokazuje czy jest prawidłowa czy nie

import pandas as pd
import random

df=pd.read_csv("Pytania.csv")

while True:
    #wybieranie pytania
    wiersz=df.iloc[random.randint(0,len(df)-1)]

    #zadawnie pytania
    print(f"\n{wiersz['Pytanie']}")
    print("Odpowiedzi:")
    print(f"A {wiersz['Odpowiedz A']}")
    print(f"B {wiersz['Odpowiedz B']}")
    print(f"C {wiersz['Odpowiedz C']}")
    print(f"D {wiersz['Odpowiedz D']}")

    #sprawdzanie odpowiedzi
    x=input("Podaj prawidłową odpowiedź, aby przerwać wpisz 0: ")
    if x == '0':
        break
    elif x.upper() == wiersz['Prawidlowe_odp']:
        print('Dobra odpowiedź')
    else:
        print("Zła odpowiedź")
        print(f"Prawidłowa odpowiedź to {wiersz['Prawidlowe_odp']}")
