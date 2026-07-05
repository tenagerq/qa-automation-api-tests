import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class TestLogin:

    def test_successful_login(self, browser):
        """Позитивный сценарий: валидный пользователь попадает в каталог."""
        login_page = LoginPage(browser).open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(browser)
        assert inventory_page.is_loaded(), "После логина каталог товаров не открылся"

    def test_login_wrong_password(self, browser):
        """Негативный сценарий: неверный пароль -> должна показаться ошибка."""
        login_page = LoginPage(browser).open()
        login_page.login("standard_user", "wrong_password")

        error = login_page.get_error_message()
        assert "do not match" in error.lower()

    def test_login_locked_out_user(self, browser):
        """Негативный сценарий: заблокированный пользователь не должен попасть в систему."""
        login_page = LoginPage(browser).open()
        login_page.login("locked_out_user", "secret_sauce")

        error = login_page.get_error_message()
        assert "locked out" in error.lower()

    @pytest.mark.parametrize("username,password", [
        ("", ""),
        ("standard_user", ""),
        ("", "secret_sauce"),
    ])
    def test_login_empty_fields(self, browser, username, password):
        """Data-driven тест: разные варианты пустых полей."""
        login_page = LoginPage(browser).open()
        login_page.login(username, password)

        error = login_page.get_error_message()
        assert error != ""
