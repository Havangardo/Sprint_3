# Автотесты для сервиса Stellar Burgers

### [Stellar Burgers](https://stellarburgers.nomoreparties.site/) - сайт для заказа бургеров.

Все тесты выполняются Chrome driver. 

На данный момент реализованы следующие проверки:
- test_successful_registration - успешная регистрация;
- test_registration_wrong_password - ошибка регистрации из-за слишком короткого пароля;
- test_login_from_main_page_success - успешная авторизация по кнопке «Войти в аккаунт» на главной;
- test_login_from_my_account_success - успешная авторизация через кнопку «Личный кабинет»;
- test_login_from_registration_form_success - успешная авторизация через кнопку в форме регистрации;
- test_login_from_password_retrieval_page_success - успешная авторизация через кнопку в форме восстановления пароля;
- test_successful_registration - успешный выход из аккаунта;
- test_enter_my_account_from_main_page_authorised_user_success - успешный переход с главной страницы в ЛК по клику на «Личный кабинет»;
- test_enter_constructor_from_my_account_successful - успешный переход по клику на «Конструктор» из ЛК;
- test_enter_main_page_from_my_account_clicking_on_logo_successful - успешный переход на главную страницу из ЛК по клику на логотип;
- test_go_to_sauces_in_constructor - переход в раздел Соусы в Конструкторе;
- test_go_to_fillings_in_constructor - переход в раздел Начинки в Конструкторе;
- test_go_to_buns_in_constructor - переход в раздел Булки в конструкторе.