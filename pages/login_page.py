import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert '/login/' in login_url, f"Login url is not valid, " \
                                       f"get {login_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form not presented on page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            'Register form is not presented on page'

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_EMAIL)
        email_input.send_keys(email)
        pwd = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD)
        pwd.send_keys(password)
        pwd_confirm = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
        pwd_confirm.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        submit_button.click()
