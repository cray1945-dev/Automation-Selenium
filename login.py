import allure
import pytest
from selenium import webdriver
import pyautogui
from environment import username, password, discussion_post, img_path, xpath_cookieBtn
import time

@allure.feature('PWA Talent Pool')
@allure.story('Home')
@allure.title('Test Case : Login')
@allure.severity(allure.severity_level.NORMAL)
def test_login():
    with allure.step('Step 1: Click yes on verification cookie'):
        browser = webdriver.Chrome()
        browser.get('https://app.myrobin.tech/en')

        time.sleep(2)

        cookieBtn = browser.find_element('xpath',xpath_cookieBtn)
        cookieBtn.click()
        pass


    with allure.step('Step 2: Click button Masuk'):
        masukBtn = browser.find_element("xpath",'//*[@id="__layout"]/div/div[2]/div/div[2]/div[2]/div/div/div/button[1]/p')
        masukBtn.click()

        time.sleep(2)
        pass

    with allure.step('Step 3: Fill user and password'):
        userField = browser.find_element("xpath",'//*[@id="__layout"]/div/div[1]/div/div/div[2]/span/form/span[1]/input')
        userField.send_keys(username)

        passField = browser.find_element("xpath",'//*[@id="__layout"]/div/div[1]/div/div/div[2]/span/form/span[2]/div/input')
        passField.send_keys(password)

        pass

    with allure.step('Step 3: Click button login'):
        loginBtn = browser.find_element("xpath",'//*[@id="__layout"]/div/div[1]/div/div/div[2]/span/form/div/div/div/button/p')
        loginBtn.click()

        time.sleep(2)
        pass

    