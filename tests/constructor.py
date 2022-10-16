from tests.locators import ConstructorLocators as cl

MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'


def test_go_to_sauces_in_constructor(driver):
    driver.get(MAIN_PAGE)
    driver.find_element(*cl.SAUCES_BUTTON).click()
    assert driver.find_element(*cl.SAUCES_CURRENT) is not None


def test_go_to_fillings_in_constructor(driver):
    driver.get(MAIN_PAGE)
    driver.find_element(*cl.FILLINGS_BUTTON).click()
    assert driver.find_element(*cl.FILLINGS_CURRENT) is not None


def test_go_to_buns_in_constructor(driver):
    driver.get(MAIN_PAGE)
    driver.find_element(*cl.SAUCES_BUTTON).click()
    driver.find_element(*cl.BUNS_BUTTON).click()
    assert driver.find_element(*cl.BUNS_CURRENT) is not None
