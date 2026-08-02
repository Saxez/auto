from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = " https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")
    sum = str(int(num1.text) + int(num2.text))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()
   
    time.sleep(20)

finally:
    browser.quit()