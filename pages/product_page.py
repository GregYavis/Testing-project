import time

from .base_page import BasePage

from .locators import ProductPageLocators


class ProductPage(BasePage):
    def check_product_page(self):
        self.check_url_is_promo()
        self.should_be_add_button()
        self.press_add_to_cart_button()
        self.check_that_product_added_to_cart()
        self.check_price_of_user_cart()

    def check_url_is_promo(self):
        url = self.browser.current_url
        assert '/?promo=newYear' in url, f'Link is not correct {url}'

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_LOCATOR), \
            "Button is not presented on product page"

    def press_add_to_cart_button(self):
        add_to_cart_button = self.browser.find_element(
            *ProductPageLocators.BUTTON_LOCATOR)
        add_to_cart_button.click()
        self.solve_quiz_and_get_code()
        #time.sleep(500)

    def check_that_product_added_to_cart(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME)
        product_name_added = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_ADDED
        )
        print(product_name.text, product_name_added.text)
        assert product_name.text in product_name_added.text, \
            "Product name must be same as product name that was added to cart"

    def check_price_of_user_cart(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        )
        product_price_in_cart = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_CART
        )
        print(product_price.text, product_price_in_cart.text)
        assert product_price.text == product_price_in_cart.text, \
            "Product price must be same as price of product in cart"
