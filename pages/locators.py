from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LINK_SEE_BASKET = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    INPUT_LOGIN = (By.NAME, "login-username")
    INPUT_PASSWORD = (By.NAME, "login-password")
    BUTTON_LOGIN = (By.NAME, "login_submit")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD_REPLAY = (By.NAME, "registration-password2")
    BUTTON_REGISTRATION = (By.NAME, "registration_submit")


class ProductPageLocators():
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_BUSKET = (By.CSS_SELECTOR, ".alertinner p strong")
    NAME_PRODUCT_FROM_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    BUTTON_ADD_BUSKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_ADDED_PRODUCT_TO_CARD = (By.CSS_SELECTOR, ".alertinner strong")
    LINK_SEE_BASKET = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators():
    MESSAGE_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    SUMMARY_BASKET = (By.CSS_SELECTOR, ".basket_summary")
