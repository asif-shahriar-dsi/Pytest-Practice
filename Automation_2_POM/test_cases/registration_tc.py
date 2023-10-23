import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from faker import Faker
import Automation_2_POM.locators.registration_locators as registration_locators
import Automation_2_POM.Utilities.json_factories as json_factory




class Registration:
    login_email = None
    login_password = None
    registration_json_directory = "C:\\Users\\Asif\\Desktop\\Practice\\Python\\Pytest 2\\Automation_2_POM\\jsons\\registration.json"

    def __init__(self):
        self.fake = Faker()

    def registration(self, driver):
        wait = WebDriverWait(driver, 15)
        actions = ActionChains(driver)
        assert "nopCommerce demo store" == driver.title

        btnRegister = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, registration_locators.btnRegister)))
        btnRegister.click()
        btnGender = wait.until(ec.element_to_be_clickable((By.ID, "gender-male")))
        btnGender.click()
        driver.find_element(By.ID, "FirstName").send_keys(self.fake.first_name())
        driver.find_element(By.ID, "LastName").send_keys(self.fake.last_name())

        selectDay = Select(driver.find_element(By.NAME, "DateOfBirthDay"))
        selectDay.select_by_visible_text("2")
        selectMonth = Select(driver.find_element(By.NAME, "DateOfBirthMonth"))
        selectMonth.select_by_index(9)
        selectYear = Select(driver.find_element(By.NAME, "DateOfBirthYear"))
        selectYear.select_by_value("1945")

        email = wait.until(ec.element_to_be_clickable((By.NAME, "Email")))
        Registration.login_email = self.fake.email()
        email.send_keys(Registration.login_email)

        newsLetter = driver.find_element(By.NAME, "Newsletter")
        if newsLetter.is_selected():
            newsLetter.click()

        inputPass = driver.find_element(By.NAME, "Password")
        confirmPass = driver.find_element(By.NAME, "ConfirmPassword")
        actions.scroll_to_element(inputPass)
        Registration.login_password = self.fake.password(10)

        inputPass.send_keys(Registration.login_password)
        confirmPass.send_keys(Registration.login_password)

        submit = wait.until(ec.element_to_be_clickable((By.XPATH,
                                                        "//button[@id='register-button']")))
        submit.click()

        assert 'Your registration completed' in driver.page_source

        json_factory.writeJson(Registration.registration_json_directory,"email_address",Registration.login_email)
        json_factory.writeJson(Registration.registration_json_directory, "password", Registration.login_password)



