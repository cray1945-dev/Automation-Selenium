import allure
import pyautogui
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from environment import userMitra, passMitra, img_path, note
import time
from environment import username, password, discussion_post, img_path


@allure.feature('PWA Talent Pool')
@allure.story('Tab Diskusi')
@allure.title('Test Case : Post feed with image')
@allure.severity(allure.severity_level.NORMAL)
def test_post_feed_img():
    with allure.step('Step 1: Cookie Verification'):
        # test logic for login with cookie
        browser = webdriver.Chrome()
        browser.get('https://app.myrobin.tech/en')
    
        cookieBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[5]/div/div[2]/button[2]'))
        )
        cookieBtn.click()
        pass

    with allure.step('Step 2: Login'):
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

    with allure.step('Step 3: go to discussion tab'):
        # test logic post discussion
        sectionDiskusi = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[3]/div/a[4]/button/span'))
        )
        sectionDiskusi.click()
        pass

    with allure.step('Step 4: Click pencil button'):
        pencilBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/div[4]/div/button/img'))
        )
        pencilBtn.click()
        pass

    with allure.step('Step 5: Fill up the feed field'):
        field_diskusi = WebDriverWait(browser,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/span/form/span/div[1]/div[1]/textarea'))
        )
        field_diskusi.send_keys(discussion_post)
        pass

    with allure.step('Step 6: upload the image'):
        imgBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/span/form/div/div/div/div/button[1]/img'))
        )
        imgBtn.click()

        time.sleep(2)

        pyautogui.write(img_path)  # Replace with the actual path to your image
        pyautogui.press('enter')  # Press Enter to confirm the file select

        sendBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/span/form/div[3]/button'))
        )
        sendBtn.click()
        pass
    
    with allure.step('Step 7: Verification Feed'):
        # test logic verification
        newBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/div[2]/button'))
        )
        newBtn.click()

        time.sleep(5)

        # Find an element by its locator (e.g., XPath, ID, etc.)
        example_element = browser.find_element("xpath", '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div/div[1]/button/div[2]/div[1]/p')

        # Get the text value of the element
        actual_value = example_element.text

        # Expected value that you want to assert against
        expected_value = "postingan diskusi"

        # Assertion to check if the actual value matches the expected value
        assert actual_value == expected_value, f"Assertion failed: Expected '{expected_value}', but got '{actual_value}'"
        print(f"Assertion Passed: Expected '{expected_value}' and got '{actual_value}")

        pass

    with allure.step('Step 8: Click option button'):
        # test logic verification
        optionBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div/div[1]/button/div[1]/div/div[2]/button/img'))
        )
        optionBtn.click()
        pass

    with allure.step('Step 9: Click hapus button'):
        delBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div/div[1]/button/div[1]/div/div[2]/div/button[3]'))
        )
        delBtn.click()
        pass

    with allure.step('Step 10: Click no on confirmation button'):
        noBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[3]/div[2]/div/div[2]/button[2]'))
        )
        noBtn.click()
        pass
    
    with allure.step('Step 11: Click yes on confirmation button'):
        # test logic verification
        optionBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div/div[1]/button/div[1]/div/div[2]/button/img'))
        )
        optionBtn.click()

        delBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div/div[1]/button/div[1]/div/div[2]/div/button[3]'))
        )
        delBtn.click()

        yesBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[3]/div[2]/div/div[2]/button[1]'))
        )
        yesBtn.click()
        
        print (f"Discussion got deleted")                                                   
        browser.quit()
        pass

