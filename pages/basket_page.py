from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage


class BasketPage(BasePage):
    def check_cart(self):
        self.check_cart_empty_message()
        self.check_cart_is_empty()

    def check_cart_empty_message(self):
        assert self.is_element_present(*MainPageLocators.CART_EMPTY_MESSAGE), \
            "Cart should be empty but page hasn't message about it"

    def check_cart_is_empty(self):
        assert self.is_not_element_present(*MainPageLocators.PRODUCT_IN_CART), \
            "Cart should be empty but it's not"
