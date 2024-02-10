from selenium import webdriver

import time  # do sleep'a

# inicjalizacja przeglądarki
driver = webdriver.Chrome()

# Implicity wait - działa na wszystkie elementy na stronie
# driver.implicitly_wait(10)

# otwarcie okna przeglądarki
driver.get('https://www.facebook.com/')

# zatrzymaj się na chwilkę
# sleep może być użyty wielokrotnie, zatrzymuje skrypt w danym momencie na określoną ilość czasu
time.sleep(500)

# zamknij przeglądarkę
driver.quit()