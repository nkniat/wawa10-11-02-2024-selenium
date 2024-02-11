import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def test_log_in_pass():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element('id', 'username').send_keys('mojenowekonto@wp.pl')
    driver.find_element('id', 'password').send_keys('mojenowehaslo')
    driver.find_element('name', 'login').send_keys(Keys.ENTER)

    #assert driver.find_element('xpath', '//*[@id="page-7"]/div/section/div/div/nav/ul/li[6]/a').is_displayed()
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()

    time.sleep(10)

def test_log_in_failed():
    pass