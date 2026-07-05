from selenium.webdriver.common.by import By
class CartPage:
    """Page Object для страницы корзины."""
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button[id^='remove']")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    def __init__(self, driver):
        self.driver = driver
    def get_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEM))
    def get_item_names(self):
        return [e.text for e in self.driver.find_elements(*self.ITEM_NAME)]
    def remove_item(self):
        self.driver.find_element(*self.REMOVE_BUTTON).click()
    def go_to_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
