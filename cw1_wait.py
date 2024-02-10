from selenium import webdriver
import time

# inicjalizacja przeglądarki
driver = webdriver.Chrome()

# otwarcie okna przeglądarki
driver.get('https://www.google.com')

# zatrzymaj się na chwilkę
time.sleep(10)

# zamknij przeglądarkę
driver.quit()
