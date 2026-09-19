from selenium.webdriver.common.by import By


add_to_cart_loc = (By.ID, 'add_to_cart')
item_title_loc = (By.TAG_NAME, 'h1')
item_breadcrumbs_loc = (By.CSS_SELECTOR, '.breadcrumb')
minus_button_loc = (By.CSS_SELECTOR, '.fa-minus')
plus_button_loc = (By.CSS_SELECTOR, '.fa-plus')
quantity_input_loc = (By.CSS_SELECTOR, '.quantity')
