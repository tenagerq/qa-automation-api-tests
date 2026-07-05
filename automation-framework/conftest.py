import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    """+
    Открывает Chrome перед каждым тестом и закрывает после.
    webdriver-manager сам скачивает нужную версию chromedriver —
    руками ничего ставить не нужно.
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(5)  # ждать элементы до 5 сек, если их сразу нет в DOM
    yield driver  # тест получает driver и работает с ним
    driver.quit()  # выполнится после теста, даже если тест упал
