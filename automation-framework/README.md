# Automation Framework — Selenium + Pytest + Page Object Model

Фреймворк для автоматизированного UI-тестирования интернет-магазина
[saucedemo.com](https://www.saucedemo.com/) — стандартного полигона
для практики QA-автоматизации.

## Стек

- **Python 3.11+**
- **Selenium 4** — управление браузером
- **Pytest** — раннер и структура тестов
- **Page Object Model (POM)** — паттерн для поддерживаемых тестов
- **pytest-html** — отчёты о прогоне
- **webdriver-manager** — автоматическая установка chromedriver

## Структура проекта

```
automation-framework/
├── pages/                 # Page Object классы (локаторы + действия)
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/                 # тесты
│   ├── test_login.py      # позитивные/негативные сценарии логина
│   ├── test_inventory.py  # каталог товаров, сортировка
│   └── test_cart.py       # добавление/удаление товаров, checkout
├── conftest.py             # фикстура браузера
├── pytest.ini               # конфигурация pytest
└── requirements.txt
```

## Что покрыто тестами

- **Login:** валидный вход, неверный пароль, заблокированный пользователь,
  пустые поля (data-driven через `@pytest.mark.parametrize`)
- **Inventory:** добавление товара в корзину, сортировка по цене (возр./убыв.)
- **Cart:** товар отображается в корзине, удаление товара, переход к оформлению

Всего 10 тестов, покрывающих как happy path, так и негативные сценарии.

## Установка и запуск

```bash
git clone <ссылка на репозиторий>
cd automation-framework
pip install -r requirements.txt
pytest
```

После прогона HTML-отчёт появится в `reports/report.html`.

Запустить конкретный файл:
```bash
pytest tests/test_login.py
```

Запустить с подробным выводом:
```bash
pytest -v
```

## Архитектурное решение: почему Page Object Model

Локаторы и действия на странице вынесены в отдельные классы (`pages/`),
а тесты (`tests/`) содержат только бизнес-логику проверки. Это значит:

- если верстка сайта поменяется — правки нужны только в одном месте
- тесты читаются как сценарии, а не как набор селекторов
- код переиспользуется между тестами (например, логин используется
  и в `test_inventory.py`, и в `test_cart.py`)

## Автор

Oleksandr Derhunov — Junior QA Engineer
[GitHub](https://github.com/tenagerq) · [LinkedIn](https://linkedin.com/in/oleksandr-derhunov)
