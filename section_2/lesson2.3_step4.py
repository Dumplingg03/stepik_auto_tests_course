from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element(By.TAG_NAME, "button").click()
    alert = browser.switch_to.alert
    alert.accept()
    span_x = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']")
    x = span_x.text
    answer = browser.find_element(By.TAG_NAME, "input").send_keys(calc(x))

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
finally:
    time.sleep(10)
    browser.quit()