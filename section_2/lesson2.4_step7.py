from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))




try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")



    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element(
            (By.ID, "price"), "$100"))
    button = browser.find_element(By.TAG_NAME, "button").click()

    span_x = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']")
    x = span_x.text
    answer = browser.find_element(By.TAG_NAME, "input").send_keys(calc(x))
    button_ans = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
finally:
    time.sleep(10)
    browser.quit()