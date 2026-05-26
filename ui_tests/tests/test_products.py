from pages.main_page import MainPage
from pages.product_page import ProductPage
import time

BASE_URL = "https://shop.polymer-project.org/"

def test_open_catalog(driver):
    page = MainPage(driver)

    page.open()
    page.wait_for_page()

    page.go_to_men()
    page.wait_for_page()

    assert "men" in driver.current_url.lower()


def test_open_product(driver):
    page = MainPage(driver)

    page.open()
    page.wait_for_page()

    page.go_to_men()
    page.wait_for_page()

    page.open_first_item()
    page.wait_for_page()

    assert "detail" in driver.current_url


def test_add_to_cart(driver):
    page = MainPage(driver)

    page.open()
    page.wait_for_page()

    page.go_to_men()
    page.wait_for_page()

    page.open_first_item()
    page.wait_for_page()

    product = ProductPage(driver)
    product.wait_for_detail()
    product.add_to_cart()

    assert True