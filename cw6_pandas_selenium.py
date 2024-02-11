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

# ==== część Selenium =====

driver = webdriver.Chrome()
driver.get('https://gotujmy.pl/forum')
driver.maximize_window()
driver.implicitly_wait(10)

# akceptacja ciasteczek
accept = driver.find_element('xpath', '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')
accept.click()


# odczytanie wartoćsi konkretnej komórki
#print(df1.iloc[0, 2])

for i in range(df1.shape[0]):
    print("nazwa: " + df1.iloc[i, 4])
    print("haslo: " + df1.iloc[i, 5])

    # przejscie do sekcji: zarejestruj sie
    rejestracja = driver.find_element('xpath', '//*[@id="navTop"]/nav/ul[1]/li[2]/a')
    rejestracja.click()

    #uzupełnienie formularza
    mail = driver.find_element('name', 'cmu_email')
    mail.send_keys(df1.iloc[i, 4])

    mail = driver.find_element('name', 'cmu_email2')
    mail.send_keys(df1.iloc[i, 4])

    haslo = driver.find_element('name', 'cmu_password')
    haslo.send_keys(df1.iloc[i, 4])

    haslo = driver.find_element('name', 'cmu_password2')
    haslo.send_keys(df1.iloc[i, 4])

    # zakonczenie rejestracji
    rejestracja = driver.find_element('xpath', '//*[@id="user_register_form"]/fieldset/footer/button')
    rejestracja.click()

    time.sleep(5)

driver.quit()
