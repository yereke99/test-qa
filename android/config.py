import pytest
from appium import webdriver

APPIUM_SERVER_PATH = 'http://172.20.19.214:4723/wd/hub'
current_device = {
    "platformName": "Android",
    "deviceName": "emulator-5554"
}


@pytest.fixture(scope="class")
def mobile_driver():
    driver = webdriver.Remote(APPIUM_SERVER_PATH, current_device)
    yield driver
    driver.quit()
