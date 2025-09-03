import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    # Настройка опций браузера
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")

    # Запускаем Chrome
    driver = webdriver.Chrome(options=options)

    yield driver  # передаём драйвер в тест

    driver.quit()  # закрываем браузер после теста