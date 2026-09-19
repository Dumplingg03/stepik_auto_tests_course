from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")

    x_element = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    checkbox_robot = browser.find_element(By.CSS_SELECTOR, "input[id='robotCheckbox']")
    checkbox_robot.click()

    checkbox_robots = browser.find_element(By.CSS_SELECTOR, "input[id='robotsRule']")
    checkbox_robots.click()

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()