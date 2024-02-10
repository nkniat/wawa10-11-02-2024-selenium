from selenium import webdriver

import time  # do sleep'a

# inicjalizacja przeglądarki
driver = webdriver.Chrome()
driver.maximize_window()

# Implicity wait - działa na wszystkie elementy na stronie
driver.implicitly_wait(10)

# otwarcie okna przeglądarki
driver.get('https://www.facebook.com/')

# zaakceptuj zgody
accept = driver.find_element("xpath", "/html/body/div[3]/div[2]/div/div/div/div/div[4]/button[2]")
accept.click()

#logowanie
user = "natas.knt@gmail.com"

with open('dane.txt', 'r') as myfile:
    password = myfile.read().replace('\n', '')

# uzupełnienie danymi
loginInput = driver.find_element("id", "email")
loginInput.send_keys(user)

passInput = driver.find_element("id", "pass")
passInput.send_keys(password)

# klikniecie login
logMyIn = driver.find_element("name", "login")
logMyIn.click()

# zatrzymaj się na chwilkę
# sleep może być użyty wielokrotnie, zatrzymuje skrypt w danym momencie na określoną ilość czasu
time.sleep(500)

# zamknij przeglądarkę
driver.quit()