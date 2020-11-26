import time

from .base_page import BasePage

from .locators import ProductPageLocators


class ProductPage(BasePage):
    def check_product_page(self):
        self.should_be_add_button()
        self.press_add_to_cart_button()
        product_name = self.get_product_name()
        self.check_that_product_added_to_cart(product_name)
        product_price = self.get_product_price()
        self.check_price_of_user_cart(product_price)

    def check_success_message_not_appear(self):
        self.press_add_to_cart_button()
        self.should_not_be_success_message()

    def check_success_message_disappear(self):
        self.press_add_to_cart_button()
        self.message_should_disappear()

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_LOCATOR), \
            "Button is not presented on product page"

    # get product_name
    # get product_price
    def press_add_to_cart_button(self):
        add_to_cart_button = self.browser.find_element(
            *ProductPageLocators.BUTTON_LOCATOR)
        add_to_cart_button.click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text

    def check_that_product_added_to_cart(self, product_name):
        product_name_added = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE
        ).text

        assert product_name == product_name_added, \
            "Product name must be same as product name that was added to cart"

    def check_price_of_user_cart(self, price):
        product_price_in_cart = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_CART
        )
        assert price == product_price_in_cart.text, \
            "Product price must be same as price of product in cart"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def message_should_disappear(self):
        assert self.element_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Message should disappear, but it's not"
