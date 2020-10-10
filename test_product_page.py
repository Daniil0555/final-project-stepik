from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.base_page import BasePage
import time


def test_guest_should_see_button_add_busket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_busket()


def test_guest_click_button_added_product(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.click_button_add_to_busket()


def test_guest_passed_aller_added_product(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.click_button_add_to_busket()
    page.add_code_in_allert()


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.click_button_add_to_busket()
    page.add_code_in_allert()
    page.should_see_message_added_product()


def test_the_cart_value_after_adding_a_product(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.click_button_add_to_busket()
    page.add_code_in_allert()
    page.should_see_message_added_product()
    page.should_see_update_price_busket()


