from selenium.webdriver.common.by import By

class CalcPage:
    input_selector = (By.ID, "input")
    output_selector = (By.ID, "output")
    button_clear_selector = (By.ID, "button_clear")
    button_bracket_left_selector = (By.ID, "button_bracket_left")
    button_bracket_right_selector = (By.ID, "button_bracket_right")
    button_division_selector = (By.ID, "button_division")
    button_0_selector = (By.ID, "button_0")
    button_1_selector = (By.ID, "button_1")
    button_2_selector = (By.ID, "button_2")
    button_3_selector = (By.ID, "button_3")
    button_4_selector = (By.ID, "button_4")
    button_5_selector = (By.ID, "button_5")
    button_6_selector = (By.ID, "button_6")
    button_7_selector = (By.ID, "button_7")
    button_8_selector = (By.ID, "button_8")
    button_9_selector = (By.ID, "button_9")
    button_multiply_selector = (By.ID, "button_multiply")
    button_subtraction_selector = (By.ID, "button_subtraction")
    button_addition_selector = (By.ID, "button_addition")
    button_percent_selector = (By.ID, "button_percent")
    button_dot_selector = (By.ID, "button_dot")
    button_equals_selector = (By.ID, "button_equals")

    def __init__(self, driver):
        self.driver = driver

    def select_button(self, option):
        button_map = {
            '0': self.button_0_selector,
            '1': self.button_1_selector,
            '2': self.button_2_selector,
            '3': self.button_3_selector,
            '4': self.button_4_selector,
            '5': self.button_5_selector,
            '6': self.button_6_selector,
            '7': self.button_7_selector,
            '8': self.button_8_selector,
            '9': self.button_9_selector,
            '+': self.button_addition_selector,
            '-': self.button_subtraction_selector,
            '/': self.button_division_selector,
            '*': self.button_multiply_selector,
            '%': self.button_percent_selector,
            '=': self.button_equals_selector,
            'c': self.button_clear_selector
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
        res = self.driver.find_element(*self.output_selector).text
        print("result is = " + res)
        return str(result) in res

    def check_error_message(self, error_message):
        # Assuming the error message is displayed in the output field
        res = self.driver.find_element(*self.output_selector).text
        print("error message = " + res)
        return error_message in res

    def open_app(self):
        self.driver.activate_app('com.pscretn.calc')
