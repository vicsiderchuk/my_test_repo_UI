from selenium.webdriver.common.by import By


empty_cart_text_loc = (By.CLASS_NAME, 'alert-info')
item_name_loc = (By.TAG_NAME, 'h6')
plus_one_item_loc = (By.CSS_SELECTOR, '.fa-plus')
item_price_loc = (By.CSS_SELECTOR, '[data-oe-expression="product_price"] .oe_currency_value')
