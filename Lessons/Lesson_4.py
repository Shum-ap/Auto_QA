import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    # Инициализация WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # Максимизация окна
    driver.maximize_window()
    # Передача драйвера в тест
    yield driver
    # Закрытие браузера
    driver.quit()
def test_open_cats_page(driver):
    # Открытие сайта
    driver.get("https://suninjuly.github.io/cats.html")
    page_header = driver.find_element(By.CSS_SELECTOR, "[class='jumbotron-heading']")
    assert page_header.text == "Cat memes"