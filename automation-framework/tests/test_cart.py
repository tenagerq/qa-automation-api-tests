from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

class TestCart:

    def _login_and_add_item(self, browser):
        LoginPage(browser).open().login("standard_user", "secret_sauce")
        inventory = InventoryPage(browser)
        inventory.add_backpack_to_cart()
        inventory.go_to_cart()
        return CartPage(browser)

    def test_item_appears_in_cart(self, browser):
        """Добавленный товар должен появиться в корзине с правильным именем."""
        cart = self._login_and_add_item(browser)

        assert cart.get_item_count() == 1
        assert "Backpack" in cart.get_item_names()[0]

    def test_remove_item_from_cart(self, browser):
        """Удаление товара -> корзина должна стать пустой."""
        cart = self._login_and_add_item(browser)
        cart.remove_item()

        assert cart.get_item_count() == 0

    def test_checkout_button_navigates(self, browser):
        """Клик по Checkout должен вести на страницу оформления заказа."""
        cart = self._login_and_add_item(browser)
        cart.go_to_checkout()

        assert "checkout-step-one" in browser.current_url
