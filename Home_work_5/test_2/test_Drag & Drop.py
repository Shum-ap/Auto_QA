import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_drag_and_drop_image(driver):
    """Тест перетаскивания изображения в корзину."""

    driver.get("https://www.globalsqa.com/demoSite/practice/droppable/photo-manager.html")

    gallery_items = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery li"))
    )
    trash_element = driver.find_element(By.ID, "trash")

    initial_gallery_count = len(gallery_items)
    initial_trash_count = len(driver.find_elements(By.CSS_SELECTOR, "#trash li"))

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", gallery_items[0])
    time.sleep(0.5)

    actions = ActionChains(driver)
    actions.drag_and_drop(gallery_items[0], trash_element).perform()
    time.sleep(1)

    final_gallery_count = len(driver.find_elements(By.CSS_SELECTOR, "#gallery li"))
    final_trash_count = len(driver.find_elements(By.CSS_SELECTOR, "#trash li"))

    assert final_trash_count == initial_trash_count + 1, f"Ожидалась 1 фотография в корзине, найдено: {final_trash_count}"
    assert final_gallery_count == initial_gallery_count - 1, f"Ожидалось 3 фотографии в галерее, найдено: {final_gallery_count}"

    print("✅ Тест пройден: Фотография успешно перемещена в корзину.")
    print(f"   - Фотографий в корзине: {final_trash_count}")
    print(f"   - Фотографий в галерее: {final_gallery_count}")