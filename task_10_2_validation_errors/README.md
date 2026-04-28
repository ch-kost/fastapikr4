# Задание 10.2

## Установка и запуск

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Проверка

```bash
curl -X POST http://127.0.0.1:8000/users -H "Content-Type: application/json" -d "{\"username\":\"alex\",\"age\":20,\"email\":\"alex@example.com\",\"password\":\"password123\"}"
curl -X POST http://127.0.0.1:8000/users -H "Content-Type: application/json" -d "{\"username\":\"alex\",\"age\":15,\"email\":\"bad\",\"password\":\"123\"}"
```
