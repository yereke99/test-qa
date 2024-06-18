import pytest
import allure
from allure_commons.types import Severity

from android.page.calculator_page import CalculatorPage

@allure.title('Calc')
@allure.severity(Severity.BLOCKER)
class TestForm:

    # Positive test cases using parameterization
    @pytest.mark.parametrize("a, operation, b, result", [(7, "+", 3, 10),
                                                         (8, "-", 2, 6),
                                                         (10, "/", 2, 5),
                                                         (5, "*", 5, 25),
                                                         (9999, "/", 11, 909)])
    def test_make_equity(self, mobile_driver, a, operation, b, result):
        driver = mobile_driver

        calculator_page = CalculatorPage(driver)
        with allure.step('Open app'):
            calculator_page.open_app()
        with allure.step('Operate'):
            calculator_page.operate(a, operation, b)
        with allure.step('Assertion'):
            assert calculator_page.is_result_equal(result)

    # Negative test cases with errors
    @pytest.mark.parametrize("a, operation, b, result", [(7, "+", 3, 11),  # Incorrect result
                                                         (8, "-", 2, 7),   # Incorrect result
                                                         (10, "/", 2, 4),  # Incorrect result
                                                         (5, "*", 5, 20),  # Incorrect result
                                                         (9999, "/", 11, 900)])  # Incorrect result
    def test_negative_cases(self, mobile_driver, a, operation, b, result):
        driver = mobile_driver

        calculator_page = CalculatorPage(driver)
        with allure.step('Open app'):
            calculator_page.open_app()
        with allure.step('Operate'):
            calculator_page.operate(a, operation, b)
        with allure.step('Assertion'):
            assert not calculator_page.is_result_equal(result)

    # Additional negative test cases
    @pytest.mark.parametrize("a, operation, b, error_message", [(7, "/", 0, "Division by zero"),  # Division by zero error
                                                                (8, "^", 2, "Unsupported operator"),  # Unsupported operator error
                                                                (10, "%", 2, "Unsupported operator")])  # Unsupported operator error
    def test_additional_negative_cases(self, mobile_driver, a, operation, b, error_message):
        driver = mobile_driver

        calculator_page = CalculatorPage(driver)
        with allure.step('Open app'):
            calculator_page.open_app()
        with allure.step('Operate'):
            calculator_page.operate(a, operation, b)
        with allure.step('Assertion'):
            assert calculator_page.check_error_message(error_message)
