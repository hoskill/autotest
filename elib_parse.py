import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

profile_links = []


def connect(background_mode: bool = False) -> None:
    """Отключение видимости WebDriver, изменение настроек браузера, подключение к библиотеке
    Для перевода браузера в фоновый режим передайте 0 """

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    if not background_mode:
        options.add_argument("--headless=new")
        print('Браузер работает в фоновом режиме...')
    else:
        print('Браузер работает в обычном режиме...')

    global driver
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://elibrary.ru/authors.asp")
        print("Подключено...")
        time.sleep(1)
    except Exception as e:
        print(f'Произошла ошибка при подключении... {e}')
        driver.close()
        driver.quit()


def get_employee(university: str = "ТГПУ", town: str = "Томск") -> None:
    """Выбор университета и получение списка преподавателей
    По умолчанию: университет - ТГПУ, город - Томск"""

    try:
        choose_button = driver.find_element(By.XPATH, '//*[@id="show_param"]/table[3]/tbody/tr[2]/td[2]/div')
        choose_button.click()
        time.sleep(1)
        driver.switch_to.frame("fancybox-frame")

        time.sleep(1)

        org_name = driver.find_element(By.CSS_SELECTOR, '#qwd')
        org_name.click()
        org_name.send_keys(university)
        time.sleep(1)
        print('Организация выбрана...')

        cities = driver.find_element(By.XPATH, '//*[@id="town"]')
        cities.click()
        cities.send_keys(town)
        cities.send_keys(Keys.ENTER)
        time.sleep(1)
        print('Город выбран...')

        org_button = driver.find_element(By.XPATH, '/html/body/center/form/table[2]/tbody/tr/td[2]/a')
        org_button.click()
        time.sleep(1)
        print('Организация найдена...')

        driver.switch_to.default_content()
        time.sleep(1)

        search_button = driver.find_element(By.CSS_SELECTOR, ".butred:last-child")
        search_button.click()
        time.sleep(1)
        print('Список сотрудников получен...')

    except Exception as e:
        print(f'Произошла ошибка при получении сотрудников... {e}')
        driver.close()
        driver.quit()


def get_links_by_page() -> None:
    """Сбор ссылок со страницы"""
    try:
        data = driver.find_elements(By.CSS_SELECTOR, 'a[href^="author_profile.asp?id="]')
        for employee in data:
            link = employee.get_attribute('href')
            profile_links.append(link)
        print('Ссылки с данной страницы успешно собраны...')
    except Exception as e:
        print(f'Произошла ошибка во время сбора ссылок... {e}')
        driver.close()
        driver.quit()


def get_all_links(background_mode: bool = False, university: str = "ТГПУ", town: str = "Томск"):
    """Сбор ссылок всех сотрудников из библиотеки"""
    connect(background_mode)
    get_employee(university, town)
    get_links_by_page()
    print(profile_links)
    print(len(profile_links))
