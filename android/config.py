import pytest
from appium import webdriver

@pytest.fixture(scope='module')
def mobile_driver():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Pixel_6_API_UpsideDownCakes',  # Update with your emulator or device name
        'app': '/app/build/outputs/apk/debug/apk-debug.apk',  # Update this with the correct path to your APK
        'automationName': 'UiAutomator2'
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    yield driver
    driver.quit()
