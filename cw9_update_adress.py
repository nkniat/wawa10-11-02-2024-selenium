import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def test_update_adress():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://seleniumdemo.com/?page_id=7")

    email = str(random.randint(0,1000)) + "tesowymail@wp.pl"

    driver.find_element('id', 'reg_email').send_keys(email)
    driver.find_element('id', 'reg_password').send_keys('fajnenowehaslo')
    driver.find_element('name', 'register').send_keys(Keys.ENTER)

    driver.find_element(By.LINK_TEXT, "Addresses").click()
    driver.find_element(By.LINK_TEXT, "Edit").click()

    #wypelnienie formularza
    driver.find_element('id', 'billing_first_name').send_keys('Jasiu')
    driver.find_element('id', 'billing_last_name').send_keys('Kowalski')

    #select - jak wybrac element z listy
    # to do
    Select(driver.find_element('id', 'select2-billing_country-container')).select_by_visible_text("Poland")

    # do dopisania
    # pamietaj o assercji


