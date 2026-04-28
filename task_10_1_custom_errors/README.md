# Задание 10.1

## Установка и запуск

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Проверка

```bash
curl "http://127.0.0.1:8000/check-age?age=15"
curl http://127.0.0.1:8000/items/999
curl "http://127.0.0.1:8000/check-age?age=20"
curl http://127.0.0.1:8000/items/1
```
