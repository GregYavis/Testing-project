from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators:
    BUTTON_LOCATOR = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_NAME_ADDED = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PRODUCT_PRICE_IN_CART = (By.CSS_SELECTOR,
                             '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div >p:nth-child(1) > strong')
