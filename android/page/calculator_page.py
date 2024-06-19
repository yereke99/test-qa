from selenium.webdriver.common.by import By

class CalculatorPage:
    input_xpath = (By.ID, "input")
    output_xpath = (By.ID, "output")
    button_clear_xpath = (By.ID, "button_clear")
    button_bracket_left_xpath = (By.ID, "button_bracket_left")
    button_bracket_right_xpath = (By.ID, "button_bracket_right")
    button_division_xpath = (By.ID, "button_division")
    button_0_xpath = (By.ID, "button_0")
    button_1_xpath = (By.ID, "button_1")
    button_2_xpath = (By.ID, "button_2")
    button_3_xpath = (By.ID, "button_3")
    button_4_xpath = (By.ID, "button_4")
    button_5_xpath = (By.ID, "button_5")
    button_6_xpath = (By.ID, "button_6")
    button_7_xpath = (By.ID, "button_7")
    button_8_xpath = (By.ID, "button_8")
    button_9_xpath = (By.ID, "button_9")
    button_multiply_xpath = (By.ID, "button_multiply")
    button_subtraction_xpath = (By.ID, "button_subtraction")
    button_addition_xpath = (By.ID, "button_addition")
    button_percent_xpath = (By.ID, "button_percent")
    button_dot_xpath = (By.ID, "button_dot")
    button_equals_xpath = (By.ID, "button_equals")

    def __init__(self, driver):
        self.driver = driver

    def select_button(self, option):
        button_map = {
            '0': self.button_0_xpath,
            '1': self.button_1_xpath,
            '2': self.button_2_xpath,
            '3': self.button_3_xpath,
            '4': self.button_4_xpath,
            '5': self.button_5_xpath,
            '6': self.button_6_xpath,
            '7': self.button_7_xpath,
            '8': self.button_8_xpath,
            '9': self.button_9_xpath,
            '+': self.button_addition_xpath,
            '-': self.button_subtraction_xpath,
            '/': self.button_division_xpath,
            '*': self.button_multiply_xpath,
            '%': self.button_percent_xpath,
            '=': self.button_equals_xpath,
            'c': self.button_clear_xpath
        }
        self.driver.find_element(*button_map[str(option)]).click()

    def click_to(self, option):
        for op in str(option):
            self.select_button(op)

    def operate(self, a, operation, b):
        self.click_to("c")
        self.click_to(a)
        self.click_to(operation)
        self.click_to(b)
        self.click_to("=")

    def is_result_equal(self, result):
        res = self.driver.find_element(*self.output_xpath).text
        print("result is = " + res)
        return str(result) in res

    def check_error_message(self, error_message):
        # Assuming the error message is displayed in the output field
        res = self.driver.find_element(*self.output_xpath).text
        print("error message = " + res)
        return error_message in res

    def open_app(self):
        self.driver.activate_app('com.pscretn.calc')
