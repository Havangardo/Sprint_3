from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from sign_in import submit_login_form
from tests.locators import LoginLocators as ll
from tests.locators import MainPageLocators as mpl

LOGIN_PAGE = 'https://stellarburgers.nomoreparties.site/login'
EMAIL = 'hermione@gmail.com'
PASSWORD = 'dramione'


def test_sign_out_authorised_user_success(driver):
    driver.get(LOGIN_PAGE)
    submit_login_form(driver, EMAIL, PASSWORD)
    driver.find_element(*mpl.MY_ACCOUNT_BUTTON).click()
    driver.implicitly_wait(2)
    driver.find_element(*ll.LOGOUT_BUTTON).click()
    # Wait for the login page to load
    WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, ".// h2[text() = 'Вход']")))
    assert driver.current_url == LOGIN_PAGE
