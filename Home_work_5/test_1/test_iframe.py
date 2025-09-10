import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_text_in_iframe(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    wait = WebDriverWait(driver, 10)

    # Находим iframe
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    print(f"\nНашли iframe -> {iframe.get_attribute('src')}")

    # Переключаемся в iframe
    driver.switch_to.frame(iframe)

    # Проверяем весь текст внутри body
    body_text = driver.find_element(By.TAG_NAME, "body").text
    print(f"\nТекст внутри iframe:\n{body_text}")

    assert "semper posuere integer et senectus justo curabitur." in body_text, \
        "❌ Текст не найден внутри iframe!"
    print("\n✅ Текст найден внутри iframe!")
