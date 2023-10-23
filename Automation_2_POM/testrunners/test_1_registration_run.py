from Automation_2_POM.environment.configure_environment import Setup
import pytest

from Automation_2_POM.test_cases.registration_tc import Registration

driver = None
login_email = None
login_password = None


@pytest.fixture(scope="function",autouse=True)
def test_setup():
    global driver
    setup = Setup()
    driver = setup.setup("Chrome")
    yield
    driver.close()


@pytest.mark.run(order=1)
def test_register_user():
    global login_email,login_password,driver
    driver.get("https://demo.nopcommerce.com/")
    registration = Registration()
    registration.registration(driver)
    print(f'The global email is: {Registration.login_email}')
    login_email = Registration.login_email
    login_password = Registration.login_password
