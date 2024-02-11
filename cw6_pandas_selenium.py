import pandas as pd
from selenium import webdriver
import time
import string
import random

df = pd.read_csv('dane_csv.csv')

df1 = df.query('Plec=="M"')
#print(df1)

# tworze nową kolumne o nazwie 'Nazwa', porzbną do rejetracji użytkowników
df['Nazwa'] = df['Imie'] + '.' + df['Nazwisko'] + '.' + str(random.randint(0, 100)) + '@domena.pl'


# >> zadanie domowe
def haslo(dlugosc_hasla):
    haslo = ''
    for _ in range(dlugosc_hasla):
        # dodawnie losowych liczb
        # haslo += str(random.randint(0, 10))
        # dodawać losowe znaki
        haslo += random.choice(string.ascii_letters)

    return haslo

df['Haslo'] = df[('Imie')] + haslo(8)

df1 = df.query('Wiek>=18')
print(f'Rozmiar tabeli: {df1.shape}')
print(f'Liczba wierszy: {df1.shape[0]}')

