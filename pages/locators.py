from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_NOT_VALID = (By.CSS_SELECTOR, '#login_link_inc')
    CART_BUTTON = (
        By.CSS_SELECTOR, 'div.basket-mini.pull-right.hidden-xs > span > a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

    CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
    PRODUCT_IN_CART = (By.CSS_SELECTOR, 'div.col-sm-4 > h3 > a')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD_CONFIRM = (
    By.CSS_SELECTOR, '#id_registration-password2')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#register_form > button')

class ProductPageLocators:
    BUTTON_LOCATOR = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PRODUCT_PRICE_IN_CART = (By.CSS_SELECTOR,
                             '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div >p:nth-child(1) > strong')
