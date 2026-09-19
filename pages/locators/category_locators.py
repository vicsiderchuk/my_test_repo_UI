from selenium.webdriver.common.by import By


item_price_loc = (By.CSS_SELECTOR, '.oe_currency_value')
sort_by_dropdown_loc = (By.CSS_SELECTOR, '.o_sortby_dropdown .dropdown-toggle')
sort_by_price_asc_loc = (By.CSS_SELECTOR, '.dropdown-menu a[href="/shop?order=list_price+asc&category=1"]')
list_view_button_loc = (By.CSS_SELECTOR, '.o_wsale_apply_list')
active_list_view_button_loc = (By.CSS_SELECTOR, '.o_wsale_apply_list.active')
customizable_desk_card =(By.CSS_SELECTOR, '[content="Customizable Desk"]')
