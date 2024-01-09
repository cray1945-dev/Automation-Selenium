import allure
import pyautogui
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from environment import userMitra, passMitra, img_path, note

@allure.feature('PWA Mitra')
@allure.story('Absen')
@allure.title('Test Case : Absensi Upload Photo')
@allure.severity(allure.severity_level.NORMAL)

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