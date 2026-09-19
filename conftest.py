from selenium import webdriver
import pytest
from pages.cart_page import Cart
from pages.item_page import Item
from pages.category_page import Category


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()

@pytest.fixture()
def cart_page(driver):
    return Cart(driver)

@pytest.fixture()
def item_page(driver):
    return Item(driver)

@pytest.fixture()
def category_page(driver):
    return Category(driver)
