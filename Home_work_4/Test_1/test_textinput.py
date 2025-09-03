import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("browser")
class TestTextInput:

    def test_button_text_changes_to_input_value(self, browser):
        # 1. Переходим на сайт
        browser.get("http://uitestingplayground.com/textinput")

        # 2. Находим поле ввода и вводим текст
        input_field = browser.find_element(By.CSS_SELECTOR, "input#newButtonName")
        input_field.clear()
        input_field.send_keys("ITCH")

        # 3. Находим кнопку и нажимаем
        button = browser.find_element(By.CSS_SELECTOR, "button#updatingButton")
        button.click()

        # 4. Ждём, что текст кнопки изменился на "ITCH"
        wait = WebDriverWait(browser, 10)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "button#updatingButton"), "ITCH"))

        # 5. Проверяем текст кнопки
        assert button.text == "ITCH", f"Ожидался текст 'ITCH', но был: '{button.text}'"