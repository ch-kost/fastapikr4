# Задание 9.1

## Установка

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Миграции

```bash
alembic upgrade head
python seed.py
```

## Запуск API

```bash
uvicorn main:app --reload
```

## Проверка

```bash
curl http://127.0.0.1:8000/products
curl -X POST http://127.0.0.1:8000/products -H "Content-Type: application/json" -d "{\"title\":\"Mouse\",\"price\":1200.5,\"count\":4,\"description\":\"Wireless mouse\"}"
```
