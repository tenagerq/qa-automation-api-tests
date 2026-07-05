from selenium.webdriver.common.by import By
class InventoryPage:
    """Page Object для страницы каталога товаров (после логина)."""
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self):
        return len(self.driver.find_elements(*self.ITEM_NAME)) > 0
    def add_backpack_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BACKPACK).click()

    def get_cart_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        return badges[0].text if badges else "0"

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()

    def sort_by(self, option_value):
        from selenium.webdriver.support.ui import Select
        Select(self.driver.find_element(*self.SORT_DROPDOWN)).select_by_value(option_value)

    def get_prices(self):
        elements = self.driver.find_elements(*self.ITEM_PRICES)
        return [float(e.text.replace("$", "")) for e in elements]
