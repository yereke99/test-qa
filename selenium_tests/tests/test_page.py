import sys
import os


# Добавьте корневую директорию проекта в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '/Users/yerek/PyPro/yerek-kcell-test-task')))

# Выведите текущие пути
print(sys.path)

from selenium import webdriver  # Импортируйте webdriver из selenium, а не из selenium_tests
from selenium_tests.pages.Form_pages import FormPage  # Обновите путь к FormPage

from time import sleep

import allure
import pytest


class TestDemo:

    @allure.feature("Позитивный тест на проверку добавления пользователя")
    @pytest.mark.positive
    def test_set_form(self, driver):
        page = FormPage(driver)

        with allure.step("Заполнение формы"):
            page.fill_form(
                first_name='Yerek',
                last_name='Yerkinbekuly',
                user_email='erkinbekly@gmail.com',
                gender='Male',
                user_number='7471850499',
                date_of_birth='02.12.1999',
                subjects=["Maths", "Science"],
                hobies=["Sports", "Reading"],
                picture=f"{os.getcwd()}/photo/run.jpeg",
                current_address="г. Алматы, ул. Шашкина 14",
            )
        with allure.step("Клик на подтверждение"):
            page.submit()

        # Проверить, есть окно успеха
        assert page.is_success_message() == True

    @allure.feature("Не ввели имя, не появилось окно успеха")
    @pytest.mark.positive
    def test_set_form_without_name(self, driver):
        page = FormPage(driver)

        with allure.step("Заполнение формы"):
            page.fill_form(
                first_name='',
                last_name='Yerkinbekuly',
                user_email='erkinbekly@gmail.com',
                gender='Male',
                user_number='7471850499',
                date_of_birth='02.12.1999',
                subjects=["Maths", "Science"],
                hobies=["Sports", "Reading"],
                picture=f"{os.getcwd()}/photo/run.jpeg",
                current_address="г. Алматы, ул. Шашкина 14",
            )
        with allure.step("Клик на подтверждение"):
            page.submit()

        # Проверить, что нет окна успеха
        assert page.is_success_message() == False

    @allure.feature("Не выбрали гендер, не появилось окно успеха")
    @pytest.mark.positive
    def test_set_without_gender(self, driver):
        page = FormPage(driver)

        with allure.step("Заполнение формы"):
            page.fill_form(
                first_name='Yerek',
                last_name='Yerkinbekuly',
                user_email='erkinbekly@gmail.com',
                gender='',
                user_number='7471850499',
                date_of_birth='02.12.1999',
                subjects=["Maths", "Science"],
                hobies=["Sports", "Reading"],
                picture=f"{os.getcwd()}/photo/run.jpeg",
                current_address="г. Алматы, ул. Шашкина 14",
            )
        with allure.step("Клик на подтверждение"):
            page.submit()

        # Проверить, что нет окна успеха
        assert page.is_success_message() == False

    @allure.feature("Не нажали на submit, не появилось окно успеха")
    @pytest.mark.positive
    def test_set_form_without_submit(self, driver):
        page = FormPage(driver)

        with allure.step("Заполнение формы"):
            page.fill_form(
                first_name='',
                last_name='Yerkinbekuly',
                user_email='erkinbekly@gmail.com',
                gender='Male',
                user_number='7471850499',
                date_of_birth='02.12.1999',
                subjects=["Maths", "Science"],
                hobies=["Sports", "Reading"],
                picture=f"{os.getcwd()}/photo/run.jpeg",
                current_address="г. Алматы, ул. Шашкина 14",
            )

        # Проверить, что нет окна успеха
        assert page.is_success_message() == False

    @allure.feature("Ввели не полный номер, не появилось окно успеха")
    @pytest.mark.positive
    def test_set_form_without_full_number(self, driver):
        page = FormPage(driver)

        with allure.step("Заполнение формы"):
            page.fill_form(
                first_name='Yerek',
                last_name='Yerkinbekuly',
                user_email='erkinbekly@gmail.com',
                gender='Male',
                user_number='747185',
                date_of_birth='02.12.1999',
                subjects=["Maths", "Science"],
                hobies=["Sports", "Reading"],
                picture=f"{os.getcwd()}/photo/run.jpeg",
                current_address="г. Алматы, ул. Шашкина 14",
            )

        with allure.step("Клик на подтверждение"):
            page.submit()

        # Проверить, что нет окна успеха
        assert page.is_success_message() == False

    @allure.feature("Ввели неправильную почту, не появилось окно успеха")
    @pytest.mark.positive
    def test_set_form_without_valid_email(self, driver):
        page = FormPage(driver)

        with allure.step("Заполнение формы"):
            page.fill_form(
                first_name='',
                last_name='Yerkinbekuly',
                user_email='erkinbeklygmail.com',
                gender='Male',
                user_number='7471850499',
                date_of_birth='02.12.1999',
                subjects=["Maths", "Science"],
                hobies=["Sports", "Reading"],
                picture=f"{os.getcwd()}/photo/run.jpeg",
                current_address="г. Алматы, ул. Шашкина 14",
            )

        with allure.step("Клик на подтверждение"):
            page.submit()

        # Проверить, что нет окна успеха
        assert page.is_success_message() == False


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()
    yield driver
    driver.quit()
