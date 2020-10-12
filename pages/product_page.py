from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def get_price_product(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        return price_product

    def get_product_from_headers_page(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_FROM_PAGE).text
        return name_product

    def should_be_add_to_busket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_BUSKET), "No search BUTTON ADD BUSKET"

    def click_button_add_to_busket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BUSKET)
        button.click()
        assert self.browser.switch_to.alert, "No click BUTTON ADD BUSKET"

    def add_code_in_allert(self):
        self.solve_quiz_and_get_code()

    def should_see_message_added_product(self):
        massage = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDED_PRODUCT_TO_CARD).text
        expected_massage = self.get_product_from_headers_page()
        assert massage == expected_massage, f"Invalid message added product, massages: {massage}, {expected_massage}"

    def should_see_update_price_busket(self):
        price_busket = self.browser.find_element(*ProductPageLocators.PRICE_BUSKET).text
        price_product = self.get_price_product()
        assert price_busket == price_product, f"Invalid price, product price {price_product} " \
                                              f"!= price busket {price_busket}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDED_PRODUCT_TO_CARD), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDED_PRODUCT_TO_CARD), \
            "Success message is presented, but should not be"

    def go_to_see_basket(self):
        button = self.browser.find_element(*ProductPageLocators.LINK_SEE_BASKET)
        button.click()

