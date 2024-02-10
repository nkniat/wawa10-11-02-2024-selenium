from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://www.kurs-selenium.pl/")

city = driver.find_element("xpath", "//span[text()='Search by Hotel or City Name']")
city.click()
city = driver.find_element("xpath", "//*[@id='select2-drop']/div/input")
city.send_keys("Dubai")
city = driver.find_element("xpath", "//*[@id='select2-drop']/ul/li/ul/li/div/span")
city.click()

checkin = driver.find_element("name", "checkin")
checkin.send_keys("14/02/2024")

checkout = driver.find_element("name", "checkout")
checkout.send_keys("17/02/2024")

travellersInput = driver.find_element("id", "travellersInput")
travellersInput.click()

adultInput = driver.find_element("id", "adultInput")
adultInput.clear()
adultInput.send_keys("3")
childInput = driver.find_element("id", "childInput")
childInput.clear()
childInput.send_keys("1")

#wyszukaj
search = driver.find_element("xpath", "//*[@id='hotels']/form/div[5]/button")
search.click()


time.sleep(500)
driver.quit()