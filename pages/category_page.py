from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import category_locators as loc


class Category(BasePage):
    page_url = '/shop/category/desks-1'

    def click_sort_by_dropdown(self):
        sort_by_dropdown = self.find(loc.sort_by_dropdown_loc)
        sort_by_dropdown.click()

    def click_sort_by_price_asc(self):
        sort_by_price_asc = self.find(loc.sort_by_price_asc_loc)
        sort_by_price_asc.click()

    def check_prices_sorted_asc(self):
        all_prices = self.find_all(loc.item_price_loc)
        prices_list = []
        for price in all_prices:
            prices_list.append(float(price.text.replace(',', '')))
        assert prices_list == sorted(prices_list)

    def click_list_view_button(self):
        list_view_button = self.find(loc.list_view_button_loc)
        list_view_button.click()

    def check_list_view_is_active(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.visibility_of_element_located(loc.active_list_view_button_loc)
        )

    def click_item_card(self):
        customizable_desk_card = self.find(loc.customizable_desk_card)
        customizable_desk_card.click()
