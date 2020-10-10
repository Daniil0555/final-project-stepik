from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_must_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.SUMMARY_BASKET), "Basket no empty"

    def message_basket_must_be_empty(self):
        message = self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET_EMPTY).text
        assert message == "Your basket is empty. Continue shopping", f"Basket no empty {message}"
