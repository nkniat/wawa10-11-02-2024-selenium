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

# przejscie do HTML Tag List
TagList = driver.find_element("xpath", "//*[@id='leftmenuinnerinner']/a[67]")
TagList.click()

# przejscie do <input>
InputMenu = driver.find_element("xpath", "//*[@id='leftmenuinnerinner']/div/a[59]")
InputMenu.click()

# przejscie do 'disable'
Disable = driver.find_element("xpath", "//*[@id='main']/table[2]/tbody/tr[8]/td[1]/a")
Disable.click()

# klikniecie 'try it yourself'
TryIt = driver.find_element("xpath", "//*[@id='main']/div[2]/a")
TryIt.click()

# sprawdzenie, gdzie jest skryp, w którym oknie
print("Aktualne okno: " + driver.title)

# obecne okno
currentWindowName = driver.current_window_handle

# wszystkie okna
windowsNames = driver.window_handles

# przełączenie do nowego okna
for window in windowsNames:
    if window != currentWindowName:
        driver.switch_to.window(window)

print("Okno po przełączeniu: " + driver.title)

# przelączenie się do iframe - strony wewnatrz strony
driver.switch_to.frame(driver.find_element("id", "iframeResult"))

# wypełnienie pola input fname - first name
FirstName = driver.find_element("id", "fname")
FirstName.send_keys("Natalia")

# wypełnienie pola input lname - last name
LastName = driver.find_element("id", "lname")
if LastName.is_enabled():
    LastName.send_keys("Burda")
else:
    print("Nie da się wpisać")

# zamkniecie bieżącej zakładki
driver.close()
driver.switch_to.window(currentWindowName)
print("Okno po zamknieciu: " + driver.title)

# cofniecie się
driver.back()

# przejście do checkboxa
CheckBox = driver.find_element("xpath", "//*[@id='main']/table[2]/tbody/tr[6]/td[1]/a")
CheckBox.click()

TryIt = driver.find_element("xpath", "//*[@id='main']/div[2]/a")
TryIt.click()

# obecne okno
currentWindowName = driver.current_window_handle

# wszystkie okna
windowsNames = driver.window_handles

# przełączenie do nowego okna
for window in windowsNames:
    if window != currentWindowName:
        driver.switch_to.window(window)

print("Okno po przełączeniu: " + driver.title)

# przelączenie się do iframe - strony wewnatrz strony
driver.switch_to.frame(driver.find_element("id", "iframeResult"))

# zaznaczanie checkboxa - to tylko zwykłe klikanie
car = driver.find_element("name", "vehicle2")
car.click()

if car.is_selected():
    print("Jest zaznaczone")

# zamkniecie bieżącej zakładki
driver.close()
driver.switch_to.window(currentWindowName)
print("Okno po zamknieciu: " + driver.title)

# zatrzymaj się na chwilkę
# sleep może być użyty wielokrotnie, zatrzymuje skrypt w danym momencie na określoną ilość czasu
time.sleep(500)

# zamknij przeglądarkę
driver.quit()
