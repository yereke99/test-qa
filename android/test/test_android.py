import pytest
import allure
from allure_commons.types import Severity
from appium import webdriver
from android.config import mobile_driver
from android.page.calculator_page import CalcPage


@allure.title('Калькулятор')
@pytest.mark.filterwarnings("ignore:cannot collect test class 'TestForm' because it has a __init__ constructor")
@allure.severity(Severity.BLOCKER)
class TestCalculator:

    @pytest.fixture(scope="class")
    def calc_page(self, mobile_driver):
        driver = mobile_driver
        calc_page = CalcPage(driver)
        calc_page.open_app()
        yield calc_page
        # Teardown code if needed

    @pytest.mark.parametrize("x, operation, y, equal", [
        (7, "+", 3, 10),
        (8, "-", 2, 6),
        (10, "/", 2, 5),
    ])
    def test_make_equity(self, calc_page, x, operation, y, equal):
        with allure.step('Operate'):
            calc_page.operate(x, operation, y)
        with allure.step('Assertion'):
            assert calc_page.is_result_equal(equal)

    @pytest.mark.parametrize("x, operation, y, equal", [
        (7, "+", 3, 11),  # Incorrect result
        (8, "-", 2, 7),  # Incorrect result
        (10, "/", 2, 4),  # Incorrect result
    ])
    def test_negative_cases(self, calc_page, x, operation, y, equal):
        with allure.step('Operate'):
            calc_page.operate(x, operation, y)
        with allure.step('Assertion'):
            assert not calc_page.is_result_equal(equal)

    @pytest.mark.parametrize("x, operation, y, error_message", [
        (7, "/", 0, "Division by zero"),  # Division by zero error
        (8, "^", 2, "Unsupported operator"),  # Unsupported operator error
        (10, "%", 2, "Unsupported operator")  # Unsupported operator error
    ])
    def test_additional_negative_cases(self, calc_page, x, operation, y, error_message):
        with allure.step('Operate'):
            calc_page.operate(x, operation, y)
        with allure.step('Assertion'):
            assert calc_page.check_error_message(error_message)
