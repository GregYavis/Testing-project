import pytest

from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at' \
       '-work_207/?promo=offer{}'


@pytest.mark.parametrize("promo_number", [pytest.param(number, marks=
pytest.mark.xfail(number == 7, reason='Bug in #message text')) for number in
                                          range(10)])
@pytest.mark.skip
def test_guest_can_add_product_to_cart(browser, promo_number):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at' \
           f'-work_207/?promo=offer{promo_number}'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.check_product_page()


@pytest.mark.parametrize("promo_number", [pytest.param(number) for number in
                                          range(10)])
@pytest.mark.skip
def test_guest_can_see_success_message_after_add_product_to_cart(browser,
                                                                 promo_number):
    product_page = ProductPage(browser, link.format(promo_number))
    product_page.open()
    product_page.press_add_to_cart_button()
    product_page.check_success_message_not_appear()


@pytest.mark.parametrize("promo_number", [pytest.param(number) for number in
                                          range(10)])
@pytest.mark.skip
def test_guest_cant_see_success_message(browser, promo_number):
    product_page = ProductPage(browser, link.format(promo_number))
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.parametrize("promo_number", [pytest.param(number) for number in
                                          range(10)])
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser,
                                                            promo_number):
    product_page = ProductPage(browser, link.format(promo_number))
    product_page.open()
    product_page.check_success_message_disappear()


@pytest.mark.skip
def test_guest_should_see_login_link_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_cart_page()
    cart_page = BasketPage(browser, browser.current_url)
    cart_page.check_cart()
