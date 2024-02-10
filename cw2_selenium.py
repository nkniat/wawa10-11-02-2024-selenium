from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait  # do oczekiwania na dany element
from selenium.webdriver.support import expected_conditions as EC  # do ustawienia warunków ozekiwania na element
from selenium.webdriver.common.by import By
import time  # do sleep'a

# inicjalizacja przeglądarki
driver = webdriver.Chrome()

# Implicity wait - działa na wszystkie elementy na stronie
driver.implicitly_wait(10)

# otwarcie okna przeglądarki
driver.get('https://www.w3schools.com/')

# wielkosc przegladarki
driver.maximize_window()

# lokalizacja przycisku 'akceptuj'
accept = driver.find_element("id", "accept-choices")
accept.click()

# wybranie menu 'Tutorials'
menu = driver.find_element("id", "navbtn_tutorials")
webdriver.ActionChains(driver).move_to_element(menu).perform()
webdriver.ActionChains(driver).move_to_element(menu).click().perform()

# wybranie tutoriala 'learn HTML'
HTMLTutorial = driver.find_element("xpath", "//a[@title='HTML Tutorial']")
HTMLTutorial.click()




# zatrzymaj się na chwilkę
# sleep może być użyty wielokrotnie, zatrzymuje skrypt w danym momencie na określoną ilość czasu
time.sleep(500)

# zamknij przeglądarkę
driver.quit()
