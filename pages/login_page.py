from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        # self.should_be_login_form()
        # self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert url.find("login") != -1, f"url {url} login page - invalid"

    # def should_be_login_form(self):
    #     # реализуйте проверку, что есть форма логина
    #     assert True
    #
    # def should_be_register_form(self):
    #     # реализуйте проверку, что есть форма регистрации на странице
    #     assert True