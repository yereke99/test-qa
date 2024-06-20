import pytest
from selenium import webdriver  # Импортируйте webdriver из selenium, а не из selenium_tests


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()
    yield driver
    driver.quit()
