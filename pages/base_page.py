from selenium.webdriver.remote.webdriver import WebDriver
from pages.locators import base_locators as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    base_url = 'http://testshop.qa-practice.com/'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page cannot be opened for this page class')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def click_top_cart_button(self):
        top_cart_button = self.find(loc.top_cart_loc)
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.text_to_be_present_in_element(
                loc.cart_count_loc, "1")
        )
        top_cart_button.click()
