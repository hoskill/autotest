import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("https://elibrary.ru/authors.asp")
time.sleep(1)
button = driver.find_element(By.CSS_SELECTOR, ".butred:last-child")
button.click()
time.sleep(10)

driver.quit()