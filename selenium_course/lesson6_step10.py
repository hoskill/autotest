from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # input_1name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    # input_1name.send_keys("Ivan")
    # input_2name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    # input_2name.send_keys("Petrov")
    # input_email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
    # input_email.send_keys("PetIV@mail.ru")
    # input_phone = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.first")
    # input_phone.send_keys("89925562940")
    # input_address = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.second")
    # input_address.send_keys("Levonova")
    inputs = browser.find_elements(By.CSS_SELECTOR, "input:required")
    for input in inputs:
        input.send_keys('test')


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()