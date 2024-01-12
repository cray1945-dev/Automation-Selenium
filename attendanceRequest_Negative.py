import allure
import pyautogui
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import datetime
from PIL import Image
from environment import*

@allure.feature('PWA Mitra')
@allure.story('Leave Request')
@allure.title('Test Case : Requesting Leave')
@allure.severity(allure.severity_level.NORMAL)

def capture_screenshot(driver, name="screenshot"):
    screenshot_path = f"request absen.png"
    allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)
    driver.save_screenshot(screenshot_path)
    return screenshot_path

def generate_numeric_date():
    # Get today's date
    today = datetime.date.today()

    # Format the date as YYYY-MM-DD
    formatted_date = today.strftime("%Y-%m-%d")

    return formatted_date

# Example usage
date_value = generate_numeric_date()

def test_leave_request():
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
        pass

    with allure.step('Step 2 : Click Tab Absensi'):
        absensiTab = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[4]/div/div/a[2]'))
        )
        absensiTab.click()
    
    with allure.step('Step 3 : Clik button permintaan absensi'):
        permintaanBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[2]/div[2]/div[5]/div/button'))
        )
        permintaanBtn.click()
        pass

    with allure.step('Step 4 : isi form permintaan absensi'):
        date = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[2]/div[2]/div[6]/div/div/div/div[2]/form/div[1]/div/div/div[2]/div/div/input'))
        )
        date.click()

        dateSelect = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'[title="{date_value}"]')) #find the attribute with title
        )
        dateSelect.click()

        office = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.ID,'jobPartnerId'))
        )
        select_yogya = Select(office)
        select_yogya.select_by_visible_text('Chef Yogyakarta')
        selected_value1 = select_yogya.first_selected_option.get_attribute("value")
        expected_value1 = '64f5925e1088390007b6e7a7'

        hourIn = WebDriverWait(browser,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="attendFrom"]'))
        )
        hourIn.send_keys('07',Keys.TAB,'00') # keys for using tab like on keyboard

        hourOut = WebDriverWait(browser,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="attendTo"]'))
        )
        hourOut.send_keys('15',Keys.TAB,'00')

        overTime = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[2]/div[2]/div[6]/div/div/div/div[2]/form/div[4]/div/select'))
        )
        browser.execute_script("arguments[0].click();", overTime)
        select1 = Select(overTime)
        select1.select_by_visible_text('1')
        selected_value2 = select1.first_selected_option.get_attribute("value")
        expected_value2 = '1'

        note = WebDriverWait(browser,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="attendanceNotes"]'))
        )
        note.send_keys('catatan request absensi automation')

        kirimBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[2]/div[2]/div[6]/div/div/div/div[2]/form/div[7]/button'))
        )
        kirimBtn.click()
        time.sleep(1)
        pass

    with allure.step('Negative Case : Absen masuk on a day that has attendance Request'):

        berandaTab = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[4]/div/div/a[1]'))
        )
        browser.execute_script("arguments[0].click();", berandaTab)

        mskBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[2]/div[1]/div[5]/div[1]/button[1]'))
        )
        browser.execute_script("arguments[0].click();", mskBtn)
        time.sleep(2)
        screenshot_path = capture_screenshot(browser, name="full_screenshot")
        pass
