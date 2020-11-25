from pages.main_page import MainPage
from pages.product_page import ProductPage


def test_guest_can_add_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.check_product_page()
