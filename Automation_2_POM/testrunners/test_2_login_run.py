import pytest

from Automation_2_POM.environment.configure_environment import Setup
from Automation_2_POM.test_cases.login_tc import Login
import test_1_registration_run as registration
import Automation_2_POM.Utilities.json_factories as json_factory

driver = None
registration_json_directory = "C:\\Users\\Asif\\Desktop\\Practice\\Python\\Pytest 2\\Automation_2_POM\\jsons\\registration.json"


@pytest.fixture(scope="function",autouse=True)
def test_setup():
    global driver
    setup = Setup()
    driver = setup.setup("Chrome")
    yield
    driver.close()


@pytest.mark.run(order=1)
def test_valid_login():
    global driver,registration_json_directory
    driver.get("https://demo.nopcommerce.com/")
    email = json_factory.readJson(registration_json_directory,"email_address")
    passwrd = json_factory.readJson(registration_json_directory, "password")
    login = Login(email,passwrd)
    login.login(driver)
