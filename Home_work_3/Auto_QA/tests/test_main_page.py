# tests/test_main_page.py
import pytest
from pages.main_page import MainPage


class TestMainPage:
    def test_main_page_elements(self, browser):
        browser.get("https://itcareerhub.de/ru")

        page = MainPage(browser)

        # 1. Проверяем логотип
        assert page.logo_is_visible(), "Логотип не отображается"

        # 2. Проверяем пункты меню
        for name in page.MENU_LINKS.keys():
            assert page.menu_link_is_visible(name), f"Меню '{name}' не отображается"

        # 3. Проверяем кнопки языков
        ru_visible, de_visible = page.lang_buttons_are_visible()
        assert ru_visible, "Кнопка 'ru' не отображается"
        assert de_visible, "Кнопка 'de' не отображается"

        # 4. Кликаем по иконке телефона
        page.click_phone_icon()

        # 5. Проверяем текст в попапе
        callback_text = page.get_callback_text()
        assert "дозвонились" in callback_text.lower(), "Текст 'Если вы не дозвонились' не найден"