from selenium.common.exceptions import NoSuchElementException, TimeoutException
import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        login_link = self.browser.find_element(
            *BasePageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_cart_page(self):
        cart_button = self.browser.find_element(*BasePageLocators.CART_BUTTON)
        cart_button.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            "Login link is not present"

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, search_method, selector):
        try:
            self.browser.find_element(search_method, selector)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, search_method, selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                expected_conditions.presence_of_element_located((
                    search_method, selector
                )))
        except TimeoutException:
            return True

        return False

    def element_disappeared(self, search_method, selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until_not(
                expected_conditions.presence_of_element_located((
                    search_method, selector
                ))
            )
        except TimeoutException:
            return False

        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
