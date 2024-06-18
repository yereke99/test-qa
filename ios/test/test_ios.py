import pytest
import allure
from allure_commons.types import Severity

from ios.page.calculator_page import CalculatorPage  # Assuming you have a CalculatorPage class for iOS

@allure.title('iOS Calculator Tests')
class TestIOSCalculator:

    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize("a, operation, b, result", [(7, "+", 3, 10),
                                                         (8, "-", 2, 6),
                                                         (10, "/", 2, 5),
                                                         (5, "*", 5, 25),
                                                         (9999, "/", 11, 909)])
    def test_positive_cases(self, ios_driver, a, operation, b, result):
        driver = ios_driver

        calculator_page = CalculatorPage(driver)
        with allure.step('Open app'):
            calculator_page.open_app()
        with allure.step('Operate'):
            calculator_page.operate(a, operation, b)
        with allure.step('Assertion'):
            assert calculator_page.is_result_equal(result)

    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize("a, operation, b, result", [(7, "+", 3, 11),
                                                         (8, "-", 2, 7),
                                                         (10, "/", 2, 4),
                                                         (5, "*", 5, 20),
                                                         (9999, "/", 11, 900)])
    def test_negative_cases_incorrect_results(self, ios_driver, a, operation, b, result):
        driver = ios_driver

        calculator_page = CalculatorPage(driver)
        with allure.step('Open app'):
            calculator_page.open_app()
        with allure.step('Operate'):
            calculator_page.operate(a, operation, b)
        with allure.step('Assertion'):
            assert not calculator_page.is_result_equal(result)

    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize("a, operation, b, error_message", [(7, "/", 0, "Division by zero"),
                                                                (8, "^", 2, "Unsupported operator"),
                                                                (10, "%", 2, "Unsupported operator")])
    def test_negative_cases_errors(self, ios_driver, a, operation, b, error_message):
        driver = ios_driver

        calculator_page = CalculatorPage(driver)
        with allure.step('Open app'):
            calculator_page.open_app()
        with allure.step('Operate'):
            calculator_page.operate(a, operation, b)
        with allure.step('Assertion'):
            assert calculator_page.check_error_message(error_message)

    @allure.severity(Severity.NORMAL)
    def test_negative_case_invalid_input(self, ios_driver):
        driver = ios_driver

        calculator_page = CalculatorPage(driver)
        with allure.step('Open app'):
            calculator_page.open_app()
        with allure.step('Operate'):
            calculator_page.operate("abc", "+", 2)  # Invalid input
        with allure.step('Assertion'):
            assert calculator_page.check_error_message("Invalid input")

    @allure.severity(Severity.NORMAL)
    def test_negative_case_missing_operands(self, ios_driver):
        driver = ios_driver

        calculator_page = CalculatorPage(driver)
        with allure.step('Open app'):
            calculator_page.open_app()
        with allure.step('Operate'):
            calculator_page.operate("", "+", "")  # Missing operands
        with allure.step('Assertion'):
            assert calculator_page.check_error_message("Missing operands")
