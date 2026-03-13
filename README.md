# FastApi-mini-app

Мини-приложение на FastAPI для учета баланса кошельков, доходов и расходов.

## Возможности

- Создание кошелька с начальным балансом
- Пополнение кошелька
- Списание средств
- Получение баланса конкретного кошелька
- Получение суммарного баланса всех кошельков

## Стек

- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic

## Быстрый старт

```bash
cd fastapi
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Установка зависимостей:

```bash
pip install -r requirements.txt
```

Запуск:

```bash
uvicorn main:app --reload
```

Сервер будет доступен на `http://127.0.0.1:8000`.

## Документация API

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Эндпоинты

Базовый префикс: `/api/v1`

- `POST /wallets` - создать кошелек
- `GET /balance?wallet_name=<name>` - баланс конкретного кошелька
- `GET /balance` - суммарный баланс всех кошельков
- `POST /operations/income` - добавить доход
- `POST /operations/expense` - добавить расход

## Примеры запросов

Создать кошелек:

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/wallets" \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"cash\",\"initial_balance\":1000}"
```

Добавить доход:

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/operations/income" \
  -H "Content-Type: application/json" \
  -d "{\"wallet_name\":\"cash\",\"amount\":250,\"description\":\"salary\"}"
```

Добавить расход:

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/operations/expense" \
  -H "Content-Type: application/json" \
  -d "{\"wallet_name\":\"cash\",\"amount\":120,\"description\":\"food\"}"
```

Баланс кошелька:

```bash
curl "http://127.0.0.1:8000/api/v1/balance?wallet_name=cash"
```

Суммарный баланс:

```bash
curl "http://127.0.0.1:8000/api/v1/balance"
```

## Структура проекта

```text
fastapi/
  app/
    api/v1/          # HTTP-роуты
    service/         # Бизнес-логика
    repository/      # Доступ к данным (in-memory словарь)
    schemas.py       # Pydantic-схемы
  main.py            # Точка входа приложения
  requirements.txt
```

## Ограничения текущей версии

- Данные хранятся в памяти процесса (`in-memory`)
- После перезапуска сервера все кошельки и операции теряются
