from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.crawler-test.com")
print(driver.title)
driver.quit()