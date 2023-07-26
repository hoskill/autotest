import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Отключение видимости WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome()

driver.get("https://elibrary.ru/authors.asp")
time.sleep(1)
profiles = []

# Добавить выбор ПЕДа
try:
    choose_button = driver.find_element(By.XPATH, '//*[@id="show_param"]/table[3]/tbody/tr[2]/td[2]/div')
    choose_button.click()
    time.sleep(1)
    driver.switch_to.frame("fancybox-frame")

    time.sleep(1)

    org_name = driver.find_element(By.CSS_SELECTOR, '#qwd')
    org_name.click()
    org_name.send_keys('ТГПУ')

    time.sleep(1)

    city = driver.find_element(By.XPATH, '//*[@id="town"]')
    city.click()
    city.send_keys('Томск')
    city.send_keys(Keys.ENTER)

    time.sleep(1)

    tspu = driver.find_element(By.XPATH, '/html/body/center/form/table[2]/tbody/tr/td[2]/a')
    tspu.click()

    driver.switch_to.default_content()

    button = driver.find_element(By.CSS_SELECTOR, ".butred:last-child")
    button.click()

    # Добавить пагинацию
    next_page = driver.find_element(By.XPATH, '//*[@id="pages"]/table/tbody/tr/td[12]/a')

    # Получаем ссылки
    info = driver.find_elements(By.CSS_SELECTOR, 'a[href^="author_profile.asp?id="]')
    for each in info:
        link = each.get_attribute('href')
        print(link)
        profiles.append(link)

finally:
    print(len(profiles))
    time.sleep(5)
    driver.close()
    driver.quit()

# while //*[@id="pages"]/table/tbody/tr/td[12]/a !=//*[@id="pages"]/table/tbody/tr/td[13]/a
