from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestInventory:

    def _login(self, browser):
        LoginPage(browser).open().login("standard_user", "secret_sauce")
        return InventoryPage(browser)

    def test_add_item_to_cart(self, browser):
        """Добавление товара -> счётчик корзины должен показать 1."""
        inventory = self._login(browser)
        inventory.add_backpack_to_cart()

        assert inventory.get_cart_count() == "1"

    def test_sort_price_low_to_high(self, browser):
        """Сортировка по цене (low->high) должна давать возрастающий список цен."""
        inventory = self._login(browser)
        inventory.sort_by("lohi")

        prices = inventory.get_prices()
        assert prices == sorted(prices), "Цены не отсортированы по возрастанию"

    def test_sort_price_high_to_low(self, browser):
        """Сортировка по цене (high->low) должна давать убывающий список цен."""
        inventory = self._login(browser)
        inventory.sort_by("hilo")

        prices = inventory.get_prices()
        assert prices == sorted(prices, reverse=True), "Цены не отсортированы по убыванию"
