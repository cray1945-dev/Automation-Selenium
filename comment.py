import allure
import pyautogui
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from environment import userMitra, passMitra, img_path, note
import time
from environment import username, password, discussion_post, img_path, feed_comment


@allure.feature('PWA Talent Pool')
@allure.story('Tab Diskusi')
@allure.title('Test Case : comment on feed')
@allure.severity(allure.severity_level.NORMAL)
def test_comment():
    with allure.step('Step 1 : Cookie Verification'):
        # test logic for login with cookie
        browser = webdriver.Chrome()
        browser.get('https://app.myrobin.tech/en')
    
        cookieBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[5]/div/div[2]/button[2]'))
        )
        cookieBtn.click()
        pass

    with allure.step('Step 2 : Login'):
        masukBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[2]/div/div[2]/div[2]/div/div/div/button[1]/p'))
        )
        masukBtn.click()

        userField = WebDriverWait(browser,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="__layout"]/div/div[1]/div/div/div[2]/span/form/span[1]/input'))    
        )
        userField.send_keys(username)

        passField = WebDriverWait(browser,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="__layout"]/div/div[1]/div/div/div[2]/span/form/span[2]/div/input'))
        )
        passField.send_keys(password)

        loginBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div/div/div[2]/span/form/div/div/div/button/p'))
        )
        loginBtn.click()
        pass

    with allure.step('Step 3 : go to discussion tab'):
        # test logic post discussion
        sectionDiskusi = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[3]/div/a[4]/button/span'))
        )
        sectionDiskusi.click()
        pass

    with allure.step('Step 4 : Click komentar'):
        komentarBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div/div[1]/button/div[5]/div/p'))
        )
        browser.execute_script("arguments[0].click();", komentarBtn)
        pass

    with allure.step('step 5: Fill the comments field'):
        commentField = WebDriverWait(browser,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div/textarea'))
        )
        commentField.send_keys(feed_comment)

        accBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div/div[2]/div/button[2]/span'))
        )
        accBtn.click()

        time.sleep(5)
        pass