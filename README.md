## Структура

- `task_9_1_alembic` — FastAPI + SQLAlchemy + Alembic миграции для Product.
- `task_10_1_custom_errors` — пользовательские исключения и обработчики ошибок.
- `task_10_2_validation_errors` — валидация Pydantic и кастомный обработчик ошибок валидации.
- `task_11_1_unit_tests` — FastAPI-приложение и синхронные unit-тесты через TestClient.
- `task_11_2_async_tests` — FastAPI-приложение и асинхронные тесты через pytest-asyncio, httpx ASGITransport и Faker.

## Быстрый запуск

Перейдите в нужную папку задания, установите зависимости и запустите команды из README этой папки.

```bash
cd task_10_1_custom_errors
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Для Linux/macOS активация окружения:

```bash
source .venv/bin/activate
```
