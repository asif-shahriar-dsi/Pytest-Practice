# from selenium import webdriver

from Practice.project.testcases.Registration import Registration
import Practice.project.environment.configure as setupEnvironment
import pytest

LOGIN_EMAIL = None
LOGIN_PASSWORD = None
# driver = None


@pytest.fixture(scope="function", autouse=True)
def test_setup():
    global driver
    setup = setupEnvironment.Setup()
    driver = setup.setup("Edge")
    yield driver
    driver.close()


@pytest.mark.run(order=1)
def test_registration():
    global LOGIN_EMAIL, LOGIN_PASSWORD
    driver.get("https://demo.nopcommerce.com")
    registration = Registration()
    registration.registration(driver)
    LOGIN_EMAIL = registration.login_email
    LOGIN_PASSWORD = registration.login_password

# @pytest.mark.run(order=2)
# def test_login():
#     login = Login(LOGIN_EMAIL, LOGIN_PASSWORD)
#     login.login()

#
# testrun = Run(Setup.firstMethod)
# testrun.test_registration()
# testrun.test_login()
