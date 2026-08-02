from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, "trollface")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, "input_value")
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(x.text))
    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()
    time.sleep(5)
finally:
    browser.quit()