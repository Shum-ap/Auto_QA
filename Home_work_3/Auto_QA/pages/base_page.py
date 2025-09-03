# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Элемент не найден: {locator}")

    def wait_for_clickable(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Элемент не кликабелен: {locator}")

    def click(self, locator, timeout=10):
        """Безопасный клик: сначала обычный, потом — через JS"""
        element = self.wait_for_clickable(locator, timeout)
        try:
            # Пробуем обычный клик
            element.click()
        except Exception:
            # Если не получилось — кликаем через JS
            print("⚠️ Используем JavaScript для клика")
            self.driver.execute_script("arguments[0].click();", element)

    def get_text(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    def wait(self, seconds):
        import time
        time.sleep(seconds)