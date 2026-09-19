from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import item_locators as loc


class Item(BasePage):
    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    def click_add_to_cart_button(self):
        add_to_cart_button = self.find(loc.add_to_cart_loc)
        add_to_cart_button.click()

    def item_card_opened(self):
        desk_title = self.find(loc.item_title_loc).text
        assert desk_title == 'Customizable Desk'

    def check_breadcrumbs_text(self):
        breadcrumbs = self.find(loc.item_breadcrumbs_loc)
        assert 'All Products' in breadcrumbs.text
        assert 'Multimedia' in breadcrumbs.text
        assert 'Office Design Software' in breadcrumbs.text

    def click_minus_button(self):
        self.find(loc.minus_button_loc).click()

    def click_plus_button(self):
        self.find(loc.plus_button_loc).click()

    def check_quantity(self, expected_quantity):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.text_to_be_present_in_element_value(loc.quantity_input_loc, expected_quantity)
        )
        quantity_input = self.find(loc.quantity_input_loc)
        quantity_value = quantity_input.get_attribute('value')
        assert quantity_value == expected_quantity
