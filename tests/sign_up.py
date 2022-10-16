from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import random
from tests.locators import RegistrationLocators as rl
from selenium.webdriver.common.by import By


REGISTRATION_PAGE = 'https://stellarburgers.nomoreparties.site/register'
LOGIN_PAGE = 'https://stellarburgers.nomoreparties.site/login'
NAME = 'Hermione Granger'
EMAIL = 'Hermione_Granger_03_' + str(random.randint(100, 999)) + '@gmail.com'
CORRECT_PASSWORD = 'HarryLikesDraco'
WRONG_PASSWORD = 'Harry'


def test_successful_registration(driver):
    submit_registration_form(driver, REGISTRATION_PAGE, NAME, EMAIL, CORRECT_PASSWORD)
    # Wait for the login page to load
    WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, ".// h2[text() = 'Вход']")))
    assert driver.current_url == LOGIN_PAGE


def test_registration_wrong_password(driver):
    submit_registration_form(driver, REGISTRATION_PAGE, NAME, EMAIL, WRONG_PASSWORD)
    error_message = driver.find_element(By.XPATH, ".//p[@class='input__error text_type_main-default']").text
    assert 'Некорректный пароль' == error_message


def submit_registration_form(driver, url, name, email, password):
    driver.get(url)
    driver.find_element(*rl.NAME_FIELD).send_keys(name)
    driver.find_element(*rl.EMAIL_FIELD).send_keys(email)
    driver.find_element(*rl.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*rl.SUBMIT_BUTTON).click()
