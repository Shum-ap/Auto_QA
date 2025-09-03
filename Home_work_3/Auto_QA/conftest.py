# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = "https://itcareerhub.de/ru"

@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()