from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x,y):
    return str(int(x) + int(y))
try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/selects1.html')
    x_element = browser.find_element(By.ID, "num1")
    x_calc = x_element.text
    y_element = browser.find_element(By.ID, "num2")
    y_calc = y_element.text

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(calc(x_calc,y_calc))

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
finally:
    time.sleep(10)
    browser.quit()
