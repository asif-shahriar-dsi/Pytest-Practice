from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from faker import Faker
import project.utilities.JsonFactories as jsonFactories
from project.environment.configure import Setup


class Registration:
    login_email = None
    login_password = None

    def __init__(self):
        self.fake = Faker()
        self.setup = Setup()

    def registration(self, driver):
        wait = WebDriverWait(driver, 15)
        assert "nopCommerce demo store" == driver.title

        btnRegister = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Register")))
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
        self.login_email = self.fake.email()
        email.send_keys(self.login_email)

        newsLetter = driver.find_element(By.NAME, "Newsletter")
        if newsLetter.is_selected():
            newsLetter.click()

        inputPass = driver.find_element(By.NAME, "Password")
        confirmPass = driver.find_element(By.NAME, "ConfirmPassword")
        driver.execute_script("arguments[0].scrollIntoView();", inputPass)
        self.login_password = self.fake.password(10)

        inputPass.send_keys(self.login_password)
        confirmPass.send_keys(self.login_password)

        submit = wait.until(ec.element_to_be_clickable((By.XPATH,
                                                        "//button[@id='register-button']")))
        submit.click()

        # successMessage = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "result")))
        # message = successMessage.text
        # assert message == "Your registration completed"

        assert 'Your registration completed' in driver.page_source
        jsonFactories.writeJson("C:\\Users\\Asif\\Desktop\\Practice\\Python\\Pytest 2\\project\\Json_files\\registration.json", "email_address", self.login_email)
        jsonFactories.writeJson("C:\\Users\\Asif\\Desktop\\Practice\\Python\\Pytest 2\\project\\Json_files\\registration.json", "passwrd", self.login_password)

        driver.close()
