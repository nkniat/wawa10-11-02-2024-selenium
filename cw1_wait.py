from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait  # do oczekiwania na dany element
from selenium.webdriver.support import expected_conditions as EC  # do ustawienia warunków ozekiwania na element
from selenium.webdriver.common.by import By
import time  # do sleep'a

# inicjalizacja przeglądarki
driver = webdriver.Chrome()

# Implicity wait - działa na wszystkie elementy na stronie
# driver.implicitly_wait(10)

# otwarcie okna przeglądarki
driver.get('https://www.w3schools.com/')

# wielkosc przegladarki
#driver.set_window_size(300, 150)
driver.maximize_window()

# lokalizacja przycisku 'akceptuj'
accept = driver.find_element("id", "accept-choices")
accept.click()

# wybranie menu 'Tutorials'
menu = driver.find_element("id", "navbtn_tutorials")
#menu.click()  # dwa sposoby
webdriver.ActionChains(driver).move_to_element(menu).perform()
webdriver.ActionChains(driver).move_to_element(menu).click().perform()

# wybranie tutoriala 'learn HTML'
# HTMLTutorial = driver.find_element("xpath", "//*[@id='tutorials_html_css_links_list']/div[1]/a[1]")
HTMLTutorial = driver.find_element("xpath", "//a[@title='HTML Tutorial']")
HTMLTutorial.click()

# oczekiwanie aż element menu "Input Types" się pojawi
# explicit wait
wait = WebDriverWait(driver, 10, 0.5)
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="leftmenuinnerinner"]/a[43]')))
# dwfiniowane własnego warunk - sprawdzanie długości listy
#wait.until(lambda x: len(x.find_elements("xpath", "//*[@id='leftmenuinnerinner']/a[43]")))

# Input types
InputTypes = driver.find_element("xpath", "//*[@id='leftmenuinnerinner']/a[43]")
InputTypes.click()

# Przesuniecie (wizualne) do danego elementu na stronie
InputFirstName = driver.find_element("name", "firstname")
actions = webdriver.ActionChains(driver).move_to_element(InputFirstName).perform()

# Input Submit
InputFirstName = driver.find_element("name", "firstname")
print(InputFirstName.get_attribute("value"))

# zatrzymaj się na chwilkę
# sleep może być użyty wielokrotnie, zatrzymuje skrypt w danym momencie na określoną ilość czasu
time.sleep(500)

# zamknij przeglądarkę
driver.quit()
