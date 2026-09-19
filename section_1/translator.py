from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://translate.yandex.ru/")

    browser.implicitly_wait(10)

    text_to_translate = input("Введите текст для перевода:")
    text_area =  browser.find_element(By.ID, 'fakeArea')
    text_area.send_keys(text_to_translate)
    time.sleep(5)
    answer = browser.find_element(By.CSS_SELECTOR, '#dstTextField span').text
    print(answer)
finally:
    time.sleep(10)
    browser.quit()
