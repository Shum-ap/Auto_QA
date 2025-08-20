import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_main_page_has_news_content(driver):
    # Правильный URL — без пробелов!
    driver.get("https://itcareerhub.de/ru")

    # Явное ожидание загрузки body
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Получаем весь текст страницы
    page_text = driver.find_element(By.TAG_NAME, "body").text

    # Проверяем наличие ключевых новостей и дат
    assert "Опубликовано: 27 ноября 2024" in page_text
    assert "NEW🔥 IT-профессия для гуманитариев найдена!" in page_text
    assert "UX/UI дизайнер - самая креативная профессия" in page_text
    assert "Опубликовано: 7 января 2025" in page_text
    assert "С Новым 2025 годом, друзья!" in page_text
    assert "Опубликовано: 16 мая 2025" in page_text
    assert "В кампусе IT Career Hub прошла встреча" in page_text