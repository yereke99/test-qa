import pytest
import allure
from allure_commons.types import Severity
from appium import webdriver
from android.config import mobile_driver
from android.page.calculator_page import CalculatorPage

@allure.title('Calc')
@pytest.mark.filterwarnings("ignore:cannot collect test class 'TestForm' because it has a __init__ constructor")
@allure.severity(Severity.BLOCKER)
class TestForm:
    
    @pytest.fixture(scope="class")
    def calculator_page(self, mobile_driver):
        driver = mobile_driver
        calculator_page = CalculatorPage(driver)
        calculator_page.open_app()
        yield calculator_page
        # Teardown code if needed

    @pytest.mark.parametrize("a, operation, b, result", [
        (7, "+", 3, 10),
        (8, "-", 2, 6),
        (10, "/", 2, 5),
        (5, "*", 5, 25),
        (9999, "/", 11, 909)
    ])
    def test_make_equity(self, calculator_page, a, operation, b, result):
        with allure.step('Operate'):
            calculator_page.operate(a, operation, b)
        with allure.step('Assertion'):
            assert calculator_page.is_result_equal(result)

    @pytest.mark.parametrize("a, operation, b, result", [
        (7, "+", 3, 11),  # Incorrect result
        (8, "-", 2, 7),   # Incorrect result
        (10, "/", 2, 4),  # Incorrect result
        (5, "*", 5, 20),  # Incorrect result
        (9999, "/", 11, 900)  # Incorrect result
    ])
    def test_negative_cases(self, calculator_page, a, operation, b, result):
        with allure.step('Operate'):
            calculator_page.operate(a, operation, b)
        with allure.step('Assertion'):
            assert not calculator_page.is_result_equal(result)

    @pytest.mark.parametrize("a, operation, b, error_message", [
        (7, "/", 0, "Division by zero"),  # Division by zero error
        (8, "^", 2, "Unsupported operator"),  # Unsupported operator error
        (10, "%", 2, "Unsupported operator")  # Unsupported operator error
    ])
    def test_additional_negative_cases(self, calculator_page, a, operation, b, error_message):
        with allure.step('Operate'):
            calculator_page.operate(a, operation, b)
        with allure.step('Assertion'):
            assert calculator_page.check_error_message(error_message)
