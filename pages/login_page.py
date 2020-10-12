from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert url.find("login") != -1, f"url {url} login page - invalid"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No search login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "No " \
                                                                              "search registration form"

    def register_new_user(self, email, password):
        input_registration = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        input_registration.send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPLAY).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION).click()
        # assert self.browser.find_element(*LoginPageLocators.ALERT_REGISTRATION_SUCCESS), "Registration fail"

    def shold_be_allert_success_registration(self):
        self.browser.find_element(*LoginPageLocators.ALERT_REGISTRATION_SUCCESS), "Registration fail"
