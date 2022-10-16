from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from sign_in import submit_login_form
from tests.locators import MainPageLocators as mpl

MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'
LOGIN_PAGE = 'https://stellarburgers.nomoreparties.site/login'
ACCOUNT_PAGE = 'https://stellarburgers.nomoreparties.site/account/profile'

EMAIL = 'hermione@gmail.com'
PASSWORD = 'dramione'


def test_enter_my_account_from_main_page_authorised_user_success(driver):
    driver.get(LOGIN_PAGE)
    submit_login_form(driver, EMAIL, PASSWORD)
    driver.find_element(*mpl.MY_ACCOUNT_BUTTON).click()
    # Wait for the profile page to load
    WebDriverWait(driver, 3).until(ec.element_to_be_clickable((By.XPATH, ".//a[@href='/account/profile']")))
    assert driver.current_url == ACCOUNT_PAGE


def test_enter_constructor_from_my_account_successful(driver):
    driver.get(LOGIN_PAGE)
    submit_login_form(driver, EMAIL, PASSWORD)
    driver.find_element(*mpl.MY_ACCOUNT_BUTTON).click()
    driver.find_element(*mpl.CONSTRUCTOR_BUTTON).click()
    assert driver.current_url == MAIN_PAGE


def test_enter_main_page_from_my_account_clicking_on_logo_successful(driver):
    driver.get(LOGIN_PAGE)
    submit_login_form(driver, EMAIL, PASSWORD)
    driver.find_element(*mpl.MY_ACCOUNT_BUTTON).click()
    driver.find_element(*mpl.LOGO).click()
    assert driver.current_url == MAIN_PAGE
