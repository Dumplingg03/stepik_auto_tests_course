from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = calc(x_element.text)

    input_form = browser.find_element(By.TAG_NAME, "input")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_form)
    input_form.send_keys(x)

    checkbox_robot = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    checkbox_robot.click()

    robots_rule = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    robots_rule.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()