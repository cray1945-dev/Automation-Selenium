import allure
import pyautogui
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from environment import*
from PIL import Image

@allure.step("Capture screenshot")
def capture_screenshot(driver, name="screenshot"):
    screenshot_path = f"spv.png"
    allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)
    driver.save_screenshot(screenshot_path)
    return screenshot_path

@allure.step("Crop and save image")
def crop_and_save_image(image_path, coordinates, output_path):
    img = Image.open(image_path)
    cropped_img = img.crop(coordinates)
    cropped_img.save(output_path)
    img.close()

def test_capture_ss():
    with allure.step('Step 5 : Login SPV'):
            browser = webdriver.Chrome()
            browser.get('https://spv.myrobin.tech/')

            userSPV = WebDriverWait(browser,20).until(
                EC.presence_of_element_located((By.XPATH,'//*[@id="form-login"]/div[1]/div/input'))
            )
            userSPV.send_keys(spvYogya)

            passSPV = browser.find_element("xpath",'//*[@id="form-login"]/div[2]/div/input')
            passSPV.send_keys(passYogya)

            loginSPV = WebDriverWait(browser,20).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@id="form-login"]/button'))
            )
            loginSPV.click()
            pass

    with allure.step('Step 6 : Click Tab Permintaan'):
            requestTab = WebDriverWait(browser,20).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/div[3]/div/div[3]'))
            )
            requestTab.click()
            pass

    with allure.step('Click Tab Izin'):
            izinTab = WebDriverWait(browser,20).until(
                EC.element_to_be_clickable((By.XPATH,'//*[@id="__layout"]/div/section/button[2]'))
            )
            izinTab.click()
            pass

    with allure.step("Capture and attach screenshot"):
            screenshot_path = capture_screenshot(browser, name="full_screenshot")

    with allure.step("Crop and save screenshot"):
            crop_and_save_image(screenshot_path, (100, 100, 500, 500), "cropped_screenshot.png")

    with allure.step("Close the WebDriver"):
            browser.quit()