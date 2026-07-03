# QA Automation — API Tests

Проект автоматизированного тестирования REST API с использованием Python, Pytest и requests.

## Что тестируется

Публичное тестовое API [JSONPlaceholder](https://jsonplaceholder.typicode.com) (эндпоинт `/posts`):

- Получение данных (GET) — проверка статус-кода и структуры ответа
- Параметризованные тесты — проверка нескольких ID в одном тесте (валидные и невалидные)
- Создание данных (POST) — проверка позитивного сценария
- Граничные случаи — проверка поведения при пустых данных

## Стек технологий

- **Python 3.11**
- **Pytest** — фреймворк для тестирования
- **requests** — отправка HTTP-запросов
- **pytest-html** — генерация HTML-отчётов
- Фикстуры (`conftest.py`), параметризация, маркеры (`smoke` / `regression`)

## Структура проекта

```
├── conftest.py       # общие фикстуры (base_url, сессия, тестовые данные)
├── test_users.py      # 7 тестов: позитивные, негативные, параметризованные
├── pytest.ini          # настройки pytest, регистрация маркеров
└── requirements.txt   # зависимости проекта
```

## Как запустить

```bash
pip install -r requirements.txt
pytest -v
```

После запуска автоматически создаётся HTML-отчёт `report.html` с результатами всех тестов.

Запуск только быстрых тестов:
```bash
pytest -m smoke
```

Запуск полного набора регрессионных тестов:
```bash
pytest -m regression
```

## Пример покрытия тестами

| Тест | Что проверяет |
|---|---|
| `test_get_single_post_status_code` | Корректный статус-код 200 |
| `test_get_single_post_response_structure` | Наличие и тип полей в ответе |
| `test_get_post_various_ids` | Валидные и невалидные ID (параметризация) |
| `test_create_post` | Создание записи, статус 201 |
| `test_create_post_empty_payload` | Поведение при пустых данных |

## Автор

Oleksandr — Junior QA Engineer, изучаю QA automation на практике.
