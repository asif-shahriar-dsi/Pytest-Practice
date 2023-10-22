import pytest

from Practice.project.testcases.Login import Login
import Test_Run1 as registration
import Practice.project.environment.configure as setupEnvironment
from Practice.project.utilities import JsonFactories

driver = None
registration_directory = "C:\\Users\\Asif\\Desktop\\Practice\\Python\\Pytest 2\\Practice\\project\\Json_files\\registration.json"


@pytest.fixture(scope="function", autouse=True)
def test_setup():
    global driver
    setup = setupEnvironment.Setup()
    driver = setup.setup("Edge")
    yield
    driver.close()


@pytest.mark.run(order=1)
def test_login():
    global driver
    if registration.LOGIN_EMAIL is None:
        login = Login("ambernelson@example.org", "@SG7VTim48")
    else:
        login = Login(registration.LOGIN_EMAIL, registration.LOGIN_PASSWORD)

    driver.get("https://demo.nopcommerce.com")
    login.login(driver)


@pytest.mark.run(order=2)
def test_loginWithInvalidPassword():
    global driver
    login = Login(registration.LOGIN_EMAIL, "bla bla")
    driver.get("https://demo.nopcommerce.com")
    login.login_with_wrong_password(driver)


@pytest.mark.run(order=3)
@pytest.mark.skip(reason="I am skipping this")
def test_login_from_json():
    global driver, registration_directory
    if JsonFactories.readJson(registration_directory, "email_address") is "":
        login = Login("ambernelson@example.org", "@SG7VTim48")
    else:
        login = Login(JsonFactories.readJson(registration_directory, "email_address"),
                      JsonFactories.readJson(registration_directory, "passwrd"))
    driver.get("https://demo.nopcommerce.com")
    login.login(driver)
