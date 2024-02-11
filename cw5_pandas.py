import pandas as pd

# wczytanie danych z pliku CSV do DataFrame
df = pd.read_csv('dane_csv.csv')

# wyswietlnie pierwszych 5 wierszy
print("=========================== HEAD =====================")
print(df.head())

# wyswietlnie informacji > ile jest niepustych danych
print("=========================== INFO =====================")
print(df.info())

# policzyc srednia wieku
print("=========================== Sredni wiek =====================")
print(df['Wiek'].mean())

# policzyc srednia wieku per płeć
print("=========================== Sredni wiek - płeć =====================")
print(df.groupby('Plec')['Wiek'].mean())

df.to_csv('nowe_dane.csv', index=False)
