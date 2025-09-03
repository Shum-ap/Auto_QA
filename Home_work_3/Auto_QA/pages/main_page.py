# pages/main_page.py
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class MainPage(BasePage):
    # Логотип
    LOGO = (By.XPATH, "//img[@alt='IT Career Hub']")

    # Ссылки в меню
    MENU_LINKS = {
        "Программы": (By.LINK_TEXT, "Программы"),
        "Способы оплаты": (By.LINK_TEXT, "Способы оплаты"),
        "Новости": (By.LINK_TEXT, "Новости"),
        "О нас": (By.LINK_TEXT, "О нас"),
        "Отзывы": (By.LINK_TEXT, "Отзывы"),
    }

    # Кнопки языков
    LANG_RU = (By.LINK_TEXT, "ru")
    LANG_DE = (By.LINK_TEXT, "de")

    # Кнопка бургера (мобильное меню)
    MOBILE_MENU_BUTTON = (
        By.XPATH,
        "//a[@href='#menuopen'] | //div[contains(@class,'t-menu__burger')]"
    )

    # Локаторы для иконки телефона — с учётом #popup:form-tr3
    PHONE_LOCATORS = [
        (By.XPATH, "//a[contains(@href,'tel')]"),
        (By.XPATH, "//a[contains(@href,'#callback')]"),
        (By.XPATH, "//a[contains(@href,'#popup:form-tr3')]"),  # ключевой!
        (By.XPATH, "//div[contains(@class,'callback')]"),
        (By.XPATH, "//*[contains(text(),'Звонок') or contains(text(),'звонок') or contains(text(),'Позвонить')]")
    ]

    # Текст "Если вы не дозвонились"
    CALLBACK_TEXT = (By.XPATH, "//*[contains(text(),'Если вы не дозвонились')]")

    # --- Методы ---
    def logo_is_visible(self):
        return self.wait_for_element(self.LOGO).is_displayed()

    def menu_link_is_visible(self, name):
        return self.wait_for_element(self.MENU_LINKS[name]).is_displayed()

    def lang_buttons_are_visible(self):
        ru_button = self.wait_for_element(self.LANG_RU).is_displayed()
        de_button = self.wait_for_element(self.LANG_DE).is_displayed()
        return ru_button, de_button

    def click_phone_icon(self):
        """Ищет и кликает по иконке телефона — в шапке или в мобильном меню"""
        driver = self.driver

        def try_click():
            for locator in self.PHONE_LOCATORS:
                try:
                    self.click(locator, timeout=5)
                    print(f"✅ Кликнули по иконке: {locator}")
                    return True
                except TimeoutException:
                    continue
            return False

        # 1. Пробуем в обычной версии
        if try_click():
            return

        print("❌ Иконка не найдена. Открываем мобильное меню...")

        # 2. Пробуем открыть бургер
        try:
            self.click(self.MOBILE_MENU_BUTTON, timeout=10)
            print("🍔 Мобильное меню открыто")
            self.wait(1)  # даем время на анимацию

            if try_click():
                print("✅ Найдено в мобильном меню")
                return
        except TimeoutException:
            print("❌ Не удалось открыть мобильное меню")

        # 3. Ошибка
        driver.save_screenshot("phone_icon_not_found.png")
        raise Exception("Не удалось найти иконку телефона ни в шапке, ни в мобильном меню")

    def get_callback_text(self):
        return self.get_text(self.CALLBACK_TEXT)