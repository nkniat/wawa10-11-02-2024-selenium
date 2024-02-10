from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://www.kurs-selenium.pl/")

time.sleep(500)
driver.quit()