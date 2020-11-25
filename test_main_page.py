from pages.main_page import MainPage
from pages.login_page import LoginPage


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


"""
def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#registration_link")
    login_link.click()"""
