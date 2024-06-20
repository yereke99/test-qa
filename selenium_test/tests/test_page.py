import os

from selenium_test.pages.Form_pages import FormPage  # Обновите путь к FormPage
from selenium_test.config import driver

from time import sleep

import allure
import pytest


class TestSelenium:

    @allure.feature("New User addition")
    @pytest.mark.positive
    def test_set_form(self, driver):
        page = FormPage(driver)

        with allure.step("Fill form"):
            page.set_data_to_form(
                name='Yerek',
                surname='Yerkinbekuly',
                email='erkinbekly@gmail.com',
                sex='Male',
                phonenumber='7471850499',
                date_of_birth='02.12.1999',
                subjects=["Maths", "Science"],
                hobbies=["Sports", "Reading"],
                image=f"{os.getcwd()}/photo/run.jpeg",
                address="г. Алматы, ул. Шашкина 14",
            )
        with allure.step("Click to submit"):
            page.submit()
        assert page.is_success() == True

    @allure.feature("Invalid email")
    @pytest.mark.positive
    def test_set_form_without_valid_email(self, driver):
        page = FormPage(driver)

        with allure.step("Fill form"):
            page.set_data_to_form(
                name='',
                surname='Yerkinbekuly',
                email='erkinbeklygmail.com',
                sex='Male',
                phonenumber='7471850499',
                date_of_birth='02.12.1999',
                subjects=["Maths", "Science"],
                hobbies=["Sports", "Reading"],
                image=f"{os.getcwd()}/photo/run.jpeg",
                address="г. Алматы, ул. Шашкина 14",
            )

        with allure.step("Click to submit"):
            page.submit()
        assert page.is_success() == False

    @allure.feature("Invalid gender")
    @pytest.mark.positive
    def test_set_without_gender(self, driver):
        page = FormPage(driver)

        with allure.step("Fill form"):
            page.set_data_to_form(
                name='Yerek',
                surname='Yerkinbekuly',
                email='erkinbekly@gmail.com',
                sex='',
                phonenumber='7471850499',
                date_of_birth='02.12.1999',
                subjects=["Maths", "Science"],
                hobbies=["Sports", "Reading"],
                image=f"{os.getcwd()}/photo/run.jpeg",
                address="г. Алматы, ул. Шашкина 14",
            )
        with allure.step("Click to submit"):
            page.submit()
        assert page.is_success() == False

    @allure.feature("Invalid number")
    @pytest.mark.positive
    def test_set_form_without_full_number(self, driver):
        page = FormPage(driver)

        with allure.step("Fill form"):
            page.set_data_to_form(
                name='Yerek',
                surname='Yerkinbekuly',
                email='erkinbekly@gmail.com',
                sex='Male',
                phonenumber='747185',
                date_of_birth='02.12.1999',
                subjects=["Maths", "Science"],
                hobbies=["Sports", "Reading"],
                image=f"{os.getcwd()}/photo/run.jpeg",
                address="г. Алматы, ул. Шашкина 14",
            )

        with allure.step("Click to submit"):
            page.submit()
        assert page.is_success() == False

    @allure.feature("Form doesn't submitted")
    @pytest.mark.positive
    def test_set_form_without_submit(self, driver):
        page = FormPage(driver)

        with allure.step("Fill form"):
            page.set_data_to_form(
                name='',
                surname='Yerkinbekuly',
                email='erkinbekly@gmail.com',
                sex='Male',
                phonenumber='7471850499',
                date_of_birth='02.12.1999',
                subjects=["Maths", "Science"],
                hobbies=["Sports", "Reading"],
                image=f"{os.getcwd()}/photo/run.jpeg",
                address="г. Алматы, ул. Шашкина 14",
            )

        assert page.is_success() == False

    @allure.feature("No name")
    @pytest.mark.positive
    def test_set_form_without_name(self, driver):
        page = FormPage(driver)

        with allure.step("Fill form"):
            page.set_data_to_form(
                name='',
                surname='Yerkinbekuly',
                email='erkinbekly@gmail.com',
                sex='Male',
                phonenumber='7471850499',
                date_of_birth='02.12.1999',
                subjects=["Maths", "Science"],
                hobbies=["Sports", "Reading"],
                image=f"{os.getcwd()}/photo/run.jpeg",
                address="г. Алматы, ул. Шашкина 14",
            )
        with allure.step("Click to submit"):
            page.submit()
        assert page.is_success() == False
