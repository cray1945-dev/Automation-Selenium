import allure
import pyautogui
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
from environment import userMitra, passMitra, img_path, note

@allure.feature('PWA Mitra')
@allure.story('Absen')
@allure.title('Test Case : Absensi Upload Photo')
@allure.severity(allure.severity_level.NORMAL)

def capture_screenshot(driver, name="screenshot"):
    screenshot_path = f"spv.png"
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
date = generate_numeric_date()


def test_absensi():
    with allure.step('Step 1 : Login'):
        browser = webdriver.Chrome()
        browser.get('https://mitra.myrobin.tech')

        user_mitra_field = WebDriverWait(browser,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="form-login"]/div[1]/div[2]/input'))
        )
        user_mitra_field.send_keys(userMitra)

        pass_mitra_field = WebDriverWait(browser,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="form-login"]/div[2]/div[2]/input'))
        )
        pass_mitra_field.send_keys(passMitra)

        loginBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="form-login"]/button'))
        )
        loginBtn.click()
        
        time.sleep(5)
        pass

    with allure.step('Step 2 : Click absen masuk'):
        masukBtn = browser.find_element("xpath",'//*[@id="__layout"]/div/div[2]/div[1]/div[5]/div[1]/button[1]/div/div')
        browser.execute_script("arguments[0].click();", masukBtn)
        
        pass

    with allure.step('Step 3 : Click lanjut absensi and upload photo'):
        lanjut_in_btn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/div/div[1]/div/button'))
        )
        lanjut_in_btn.click()
        time.sleep(2)

        pyautogui.write(img_path)  # Replace with the actual path to your image
        pyautogui.press('enter')  # Press Enter to confirm the file select
        pass

    with allure.step('Step 5 : FIll notes and click rekam waktu'):
        note_in_field = WebDriverWait(browser,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="__layout"]/div/div[2]/form/section[1]/textarea'))
        )
        note_in_field.send_keys(note)

        rekam_in_btn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[2]/form/section[2]/button'))
        )
        rekam_in_btn.click()

        selesai_in_btn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[2]/div[4]/div[2]/div/div[2]/button'))
        )
        selesai_in_btn.click()

        time.sleep(5)
        pass


    with allure.step('Step 6 : Click button absen keluar'):
        keluarBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[2]/div[1]/div[5]/div[1]/button[1]/div/div'))
        )
        browser.execute_script("arguments[0].click();", keluarBtn)
        pass

    with allure.step('Step 7 : Click lanjut absensi and upload photo'):
        lanjut_out_btn =  WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/div/div[1]/div/button'))
        )
        lanjut_out_btn.click()

        time.sleep(2)

        pyautogui.write(img_path)  # Replace with the actual path to your image
        pyautogui.press('enter')  # Press Enter to confirm the file select
        
        pass

    with allure.step('Step 8 : Fill Notes and click rekam waktu'):
        note_out_field = WebDriverWait(browser,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="__layout"]/div/div[2]/form/section[1]/textarea'))
        )
        note_out_field.send_keys(note)

        rekam_out_btn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[2]/form/section[2]/button'))
        )
        rekam_out_btn.click()

        selesai_out_btn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[2]/div[4]/div[2]/div/div[2]/button'))
        )
        selesai_out_btn.click()

        time.sleep(5)
        pass

    with allure.step('Negative Case : Leave Request'):
        izinBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[2]/div[1]/div[5]/div[1]/button[3]'))
        )
        browser.execute_script("arguments[0].click();", izinBtn)
        time.sleep(5)
        pass

    with allure.step('Step 1 : isi form untuk izin'):
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
        leave_date.send_keys(date)

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

        browser.execute_script("window.scrollTo(10, document.body.scrollHeight);")
        pass

    with allure.step('Step 2 : Click ajukan izin'):
        ajukanBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[2]/div[2]/div/div/form/div[9]/button'))
        )
        browser.execute_script("arguments[0].click();", ajukanBtn)
        time.sleep(2)
        screenshot_path = capture_screenshot(browser, name="full_screenshot")
        pass