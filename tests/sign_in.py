from selenium.webdriver.common.by import By
from tests.locators import LoginLocators as ll
from tests.locators import MainPageLocators as mpl

LOGIN_PAGE = 'https://stellarburgers.nomoreparties.site/login'
MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'
REGISTRATION_PAGE = 'https://stellarburgers.nomoreparties.site/register'
FORGOT_PASSWORD_PAGE = 'https://stellarburgers.nomoreparties.site/forgot-password'
EMAIL = 'hermione@gmail.com'
PASSWORD = 'dramione'


def test_login_from_main_page_success(driver):
    driver.get(MAIN_PAGE)
    driver.find_element(*mpl.LOGIN_OR_ORDER_BUTTON).click()
    submit_login_form(driver, EMAIL, PASSWORD)
    assert is_login_successful(driver)


def test_login_from_my_account_success(driver):
    driver.get(MAIN_PAGE)
    driver.find_element(*mpl.MY_ACCOUNT_BUTTON).click()
    submit_login_form(driver, EMAIL, PASSWORD)
    assert is_login_successful(driver)


def test_login_from_registration_form_success(driver):
    driver.get(REGISTRATION_PAGE)
    driver.find_element(*ll.LOGIN_LINK).click()
    submit_login_form(driver, EMAIL, PASSWORD)
    assert is_login_successful(driver)


def test_login_from_password_retrieval_page_success(driver):
    driver.get(FORGOT_PASSWORD_PAGE)
    driver.find_element(*ll.LOGIN_LINK).click()
    submit_login_form(driver, EMAIL, PASSWORD)
    assert is_login_successful(driver)


def submit_login_form(driver, email, password):
    driver.find_element(*ll.LOGIN_FIELD).send_keys(email)
    driver.find_element(*ll.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*ll.SUBMIT_BUTTON).click()


def is_login_successful(driver):
    driver.implicitly_wait(2)
    message = driver.find_element(By.XPATH,
                                  ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text
    return message == "Оформить заказ"
