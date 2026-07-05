from selenium.webdriver.common.by import By


class LoginPage:
    """
    Page Object для страницы логина saucedemo.com

    Идея POM: вся работа с локаторами и действиями на странице
    живёт здесь. Тесты не знают, как устроен HTML — они просто
    вызывают методы вроде login(). Если верстка сайта поменяется,
    править нужно только этот файл, а не десятки тестов.
    """

    URL = "https://www.saucedemo.com/"

    # Локаторы — где на странице искать элементы
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
