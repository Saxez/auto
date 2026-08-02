from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    firstname = browser.find_element(By.NAME, "firstname")
    firstname.send_keys("Ivan")
    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("Petrov")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("ivan.petrov@example.com")
    element = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'reg.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(20)

finally:
    browser.quit()