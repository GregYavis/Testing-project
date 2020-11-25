import pytest

from pages.main_page import MainPage
from pages.product_page import ProductPage


@pytest.mark.parametrize("promo_number", [pytest.param(number, marks=
pytest.mark.xfail(number==7, reason='Bug in #message text')) for number in
range(10)])


def test_guest_can_add_product_to_cart(browser, promo_number):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at' \
           f'-work_207/?promo=offer{promo_number}'
    print(link)
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.check_product_page()
