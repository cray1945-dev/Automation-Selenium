import allure
import pyautogui
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PIL import Image
from environment import*

@allure.feature('PWA Mitra')
@allure.story('Leave Request')
@allure.title('Test Case : Requesting Leave on the same day')
@allure.severity(allure.severity_level.NORMAL)

def capture_screenshot(driver, name="screenshot"):
    screenshot_path = f"spv.png"
    allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)
    driver.save_screenshot(screenshot_path)
    return screenshot_path

def test_requestLeaveDouble():
    with allure.step('Step 1 : Login into PWA mitra'):
        browser = webdriver.Chrome()
        browser.get('https://mitra.myrobin.tech')

        emailField = WebDriverWait(browser,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="form-login"]/div[1]/div[2]/input'))
        )
        emailField.send_keys(userMitra)
        
        passField = WebDriverWait(browser,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="form-login"]/div[2]/div[2]/input'))
        )
        passField.send_keys(passMitra)

        masukBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="form-login"]/button'))
        )
        masukBtn.click()
        time.sleep(2)
        pass

    with allure.step('Step 2 : Click button ajukan izin'):
        izinBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[2]/div[1]/div[5]/div[1]/button[3]'))
        )
        browser.execute_script("arguments[0].click();", izinBtn)
        time.sleep(5)
        pass

    with allure.step('Step 3 : isi form untuk izin'):
        permission_type = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.ID,'permissionType'))
        )
        select_permission = Select(permission_type)
        select_permission.select_by_visible_text('Izin Tidak Berbayar')
        selected_value1 = select_permission.first_selected_option.get_attribute("value")
        expected_value1 = '0'
        
        leave_type = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.ID,'typeOfLeave'))
        )
        select_leave = Select(leave_type)
        select_leave.select_by_visible_text('automation')
        selected_value2 = select_leave.first_selected_option.get_attribute("value")
        expected_value2 = '6594e83d7429cb1594d79829'
        pass

        total_day = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.ID,'totalDays'))
        )
        select_day = Select(total_day)
        select_day.select_by_visible_text('1 hari')
        selected_value3 = select_leave.first_selected_option.get_attribute("value")
        expected_value3 = '1'

        leave_date = WebDriverWait(browser,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="leaveDate"]/div/input'))
        )
        leave_date.send_keys('2022-12-01')

        fullDay = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="isFullday"]'))
        )
        browser.execute_script("arguments[0].click();", fullDay)

        leave_reason = WebDriverWait(browser,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="reason"]'))
        )
        leave_reason.send_keys('note leave automation')

        upload = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="fileAttachment"]'))
        )
        upload.click()

        time.sleep(3)
        pyautogui.write(img_path) 
        pyautogui.press('enter')
        pass

    with allure.step('Step 4 : Click ajukan izin'):
        ajukanBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[2]/div[2]/div/div/form/div[9]/button'))
        )
        browser.execute_script("arguments[0].click();", ajukanBtn)
        time.sleep(5)
        screenshot_path = capture_screenshot(browser, name="full_screenshot")
        pass