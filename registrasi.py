import allure
import pyautogui
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from environment import*

@allure.feature('PWA Talent Pool')
@allure.story('Registrasi')
@allure.title('Test Case : Registrasi')
@allure.severity(allure.severity_level.NORMAL)

def test_registrasi():
    with allure.step('step 1: Click yes/no button cookie'):
        browser = webdriver.Chrome()
        browser.get('https://app.myrobin.tech/en')

        cookieBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[5]/div/div[2]/button[2]'))
        )
        cookieBtn.click()
        pass

    with allure.step('step 2: Click button daftar'):
        daftarBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[2]/div/div[2]/div[2]/div/div/div/button[2]/p'))
        )
        daftarBtn.click()
        pass

    with allure.step('step 3: Click button daftar akun'):
        daftar_akunBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[2]/div/div/div[3]/button[1]'))
        )
        daftar_akunBtn.click()
        pass

    with allure.step('step 4 : Click Fill the field and click button daftar akun'):
        emailField = WebDriverWait(browser,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="email"]'))
        )
        emailField.send_keys(email_regis)

        tlpnField = WebDriverWait(browser,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="phone"]'))
        )
        tlpnField.send_keys(telp_regis)

        passField = WebDriverWait(browser,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="password"]'))
        )
        passField.send_keys(pass_regis)

        daftarBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[2]/div/div[3]/span/form/div/div/div[1]/button'))
        )
        daftarBtn.click()
        pass

    with allure.step('step 5 : Fill the data diri form'):
        nameField = WebDriverWait(browser,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/span/form/div[1]/span[1]/div/input'))
        )
        nameField.send_keys(name_regis)

        domisiliField = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="domicile_city_id"]/button'))
        )
        domisiliField.click()

        regionField = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="domicile_city_id"]/div/div/div[2]/button[3]'))
        ) 
        browser.execute_script("arguments[0].click();", regionField)

        alamatField = WebDriverWait(browser,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="address"]'))
        )
        alamatField.send_keys(alamat_regis)

        # Field not clickable   
        TTLField = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="birthdate"]/button'))
        )
        browser.execute_script("arguments[0].click();", TTLField)

        simpanBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="birthdate"]/div/div/div/div[2]/button[2]'))
        )
        simpanBtn.click()

        sexField = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="gender"]/button'))
        )
        browser.execute_script("arguments[0].click();", sexField)

        femaleField = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="gender"]/div/div/button[2]/p'))
        )
        browser.execute_script("arguments[0].click();", femaleField)

        lanjutBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/span/form/div[2]/div/div/button'))
        )
        lanjutBtn.click()
        pass

    with allure.step('step 6 : Choose preferensi pekerjaan'):
        prefImg = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/div[4]/div[1]/button[1]/div[1]/img'))
        )
        prefImg.click()

        continueBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/form/div/div/div/button'))
        )
        browser.execute_script("arguments[0].click();", continueBtn)
        pass

    with allure.step('step 7 : choose community'):
        allcomBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/div[1]/div[2]/button/p'))
        )
        allcomBtn.click()

        gabungBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/form/div/div/div/button'))
        )
        browser.execute_script("arguments[0].click();", gabungBtn)
        pass

    with allure.step('step 8 : follow other user'):
        alluserBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/div[3]/button'))
        )
        alluserBtn.click()

        lewatiBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[2]/form/div/div/div/button'))
        )
        browser.execute_script("arguments[0].click();", lewatiBtn)
        pass

    with allure.step('step 9 : welcome to myrobin'):
        berandaBtn = WebDriverWait(browser,20).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[1]/div[3]/a'))
        )
        berandaBtn.click()

        time.sleep(5)
        pass