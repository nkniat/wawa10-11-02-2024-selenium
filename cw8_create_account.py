import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def test_create_account_pass():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://seleniumdemo.com/?page_id=7")

    email = str(random.randint(0,1000)) + "tesowymail@wp.pl"

    driver.find_element('id', 'reg_email').send_keys(email)
    driver.find_element('id', 'reg_password').send_keys('fajnenowehaslo')
    driver.find_element('name', 'register').send_keys(Keys.ENTER)

    #assert driver.find_element('xpath', '//*[@id="page-7"]/div/section/div/div/nav/ul/li[6]/a').is_displayed()
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()

    time.sleep(10)


def test_create_account_failed():

    msg = "Error: An account is already registered with your email address. Please log in"

    # szkic
    # assert msg in driver.find_element('xpath', "//ul[@class='woocommerce-error']").text
