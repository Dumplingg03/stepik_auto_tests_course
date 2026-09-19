from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    firstName = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys("Dmitry")
    
    lastName = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys("Ivanov")

    email = browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("gfg@mail.ru")



    element = browser.find_element(By.CSS_SELECTOR, "input[type='file']")

    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


finally:
    time.sleep(10)
    browser.quit()