import pytest
from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    # for case where we call LoginPage in MainPage.go_to_login_page return
    # login_oage = page.go_to_login_page
    # login_page.should_be_login_page


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_cart_page()
    cart_page = BasketPage(browser, browser.current_url)
    cart_page.check_cart()

@pytest.mark.login_guest
class TestLoginFromMainPage:
    # to prepare special data for test we can use fixtures in test clases
    # example approximate to pseudocode
    # @pytest.fixture(scope = "function", autouse=True)
    # def setup(self):
    #   prepare data or objects to test
    #   yield
    #   clear generated data
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        # for case where we call LoginPage in MainPage.go_to_login_page return
        # login_oage = page.go_to_login_page
        # login_page.should_be_login_page

    def guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


"""
def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#registration_link")
    login_link.click()"""
