from selenium.webdriver.common.by import By


class MainPageLocators:
    # Личный кабинет в хэдере
    MY_ACCOUNT_BUTTON = (By.XPATH, ".//a[@href='/account']/p[@class='AppHeader_header__linkText__3q_va ml-2']")
    # Конструктор в хэдере
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//a[@href='/']/p[@class='AppHeader_header__linkText__3q_va ml-2']")
    # Логотип в хэдере
    LOGO = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")
    # Оформить заказ, если юзер авторизован, Войти в аккаунт - если нет (кнопка справа внизу)
    LOGIN_OR_ORDER_BUTTON = (By.XPATH,
                          ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")


class RegistrationLocators:
    # Поля в форме регистрации
    NAME_FIELD = (By.XPATH, ".//fieldset[1]//input")
    EMAIL_FIELD = (By.XPATH, ".//fieldset[2]//input")
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password']")
    SUBMIT_BUTTON = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")


class LoginLocators:
    # Поля в форме авторизации
    LOGIN_FIELD = (By.XPATH, ".//input[@name='name']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password']")
    SUBMIT_BUTTON = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")

    # Кнопка логина на странице регистрации и восстановления пароля
    LOGIN_LINK = (By.XPATH, ".//a[@class='Auth_link__1fOlj']")

    # Выход из аккаунта
    LOGOUT_BUTTON = (By.XPATH, ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")


class ConstructorLocators:
    # Кнопки перехода
    BUNS_BUTTON = (By.XPATH, ".//span[(@class='text text_type_main-default' and text()='Булки')]")
    SAUCES_BUTTON = (By.XPATH, ".//span[(@class='text text_type_main-default' and text()='Соусы')]")
    FILLINGS_BUTTON = (By.XPATH, ".//span[(@class='text text_type_main-default' and text()='Начинки')]")

    # Условие, что раздел выбран
    BUNS_CURRENT = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Булки']")
    SAUCES_CURRENT = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Соусы']")
    FILLINGS_CURRENT = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Начинки']")
