from selenium import webdriver
import time

# inicjalizacja przeglądarki
driver = webdriver.Chrome()

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
HTMLTutorial = driver.find_element("xpath", "//*[@id='tutorials_html_css_links_list']/div[1]/a[1]")
HTMLTutorial.click()

# zatrzymaj się na chwilkę
time.sleep(500)

# zamknij przeglądarkę
driver.quit()
