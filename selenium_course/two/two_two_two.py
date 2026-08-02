from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "input_value")
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(x.text))    
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    button.click()
    time.sleep(20)

finally:
    browser.quit()