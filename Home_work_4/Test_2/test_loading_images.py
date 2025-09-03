import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("browser")
class TestLoadingImages:

    def test_third_image_alt_is_award(self, browser):
        # 1. Переходим на сайт
        browser.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

        # 2. Ждём, пока появится 4 изображения (или хотя бы 3)
        wait = WebDriverWait(browser, 15)
        wait.until(
            lambda driver: len(driver.find_elements(By.CSS_SELECTOR, "#image-container img")) >= 3
        )

        # 3. Находим все изображения внутри контейнера
        images = browser.find_elements(By.CSS_SELECTOR, "#image-container img")

        # 4. Берём третье изображение (индекс 2)
        assert len(images) >= 3, "На странице должно быть как минимум 3 изображения"
        third_image = images[2]

        # 5. Проверяем, что его alt = "award"
        alt_text = third_image.get_attribute("alt")
        assert alt_text == "award", f"Ожидался alt='award', но получен: '{alt_text}'"