from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--start-maximized")

service = Service(executable_path="C:\\Users\\ICH\\Downloads\\geckodriver-v0.36.0-win64\\geckodriver.exe")
driver = webdriver.Firefox(service=service, options=options)


def close_visible_modals(timeout=5):
    """Закрывает все видимые модальные окна."""
    end_time = time.time() + timeout
    while time.time() < end_time:
        buttons = driver.find_elements(By.TAG_NAME, "button")
        clicked = False
        for btn in buttons:
            try:
                if btn.is_displayed() and btn.is_enabled():
                    if "закрыть" in btn.text.lower() or "×" in btn.text:
                        driver.execute_script("arguments[0].click();", btn)
                        clicked = True
                        time.sleep(0.3)
            except:
                continue
        if not clicked:
            break


def click_cookie_button(timeout=15):
    """Находит и нажимает кнопку 'ПОДТВЕРДИТЬ'."""
    try:
        # Находим любые элементы с текстом "ПОДТВЕРДИТЬ"
        elements = driver.find_elements(By.XPATH, "//*[contains(normalize-space(.), 'ПОДТВЕРДИТЬ')]")
        print("Нашёл элементов с текстом 'ПОДТВЕРДИТЬ':", len(elements))
        for i, el in enumerate(elements):
            try:
                print(i, "| тег:", el.tag_name, "| текст:", el.text)
            except:
                pass

        # Ждём пока кнопка станет кликабельной
        btn = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, "//*[normalize-space(text())='ПОДТВЕРДИТЬ']"))
        )

        # Скроллим и жмём через JS
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", btn)
        print("Кнопка ПОДТВЕРДИТЬ нажата!")

        time.sleep(1)
        return True
    except Exception as e:
        print("Не удалось нажать кнопку ПОДТВЕРДИТЬ:", e)
        return False


try:
    driver.get("https://itcareerhub.de/ru")
    time.sleep(1)

    # Закрываем все модалки
    close_visible_modals()

    # Пробуем кликнуть куки
    click_cookie_button()

    # Ищем и кликаем ссылку "Способы оплаты"
    payment_link = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Способы оплаты"))
    )
    payment_link.click()
    time.sleep(1)

    # Ещё раз закрываем модалки и куки
    close_visible_modals()
    click_cookie_button()

    # Ждём раздел
    payment_section = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Способы оплаты')]/.."))
    )

    driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", payment_section)
    time.sleep(1)

    driver.save_screenshot("full_window.png")
    print("Скриншот сохранен как full_window.png")

finally:
    driver.quit()
