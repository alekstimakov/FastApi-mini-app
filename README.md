# FastApi-mini-app

A small FastAPI service for wallet balance tracking with income and expense operations.

## Features

- Create wallets with an initial balance
- Add income to a wallet
- Add expense from a wallet
- Get one wallet balance
- Get total balance across all wallets
- Data persistence in SQLite (`finance.db`)

## Stack

- Python 3.11+
- FastAPI
- Pydantic v2
- SQLAlchemy 2
- Uvicorn
- SQLite

## Quick Start

```bash
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

Install dependencies:

```bash
pip install -r requirements.txt
```

Run app:

```bash
uvicorn main:app --reload
```

App URL: `http://127.0.0.1:8000`

## API Docs

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Endpoints

Base prefix: `/api/v1`

- `POST /wallets`
- `GET /balance?wallet_name=<name>`
- `GET /balance`
- `POST /operations/income`
- `POST /operations/expense`

## Request Examples

Create wallet:

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/wallets" \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"cash\",\"initial_balance\":1000}"
```

Add income:

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/operations/income" \
  -H "Content-Type: application/json" \
  -d "{\"wallet_name\":\"cash\",\"amount\":250,\"description\":\"salary\"}"
```

Add expense:

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/operations/expense" \
  -H "Content-Type: application/json" \
  -d "{\"wallet_name\":\"cash\",\"amount\":120,\"description\":\"food\"}"
```

Wallet balance:

```bash
curl "http://127.0.0.1:8000/api/v1/balance?wallet_name=cash"
```

Total balance:

```bash
curl "http://127.0.0.1:8000/api/v1/balance"
```

## Validation and Errors

- Wallet name must be non-empty
- `initial_balance` must be `>= 0`
- Operation `amount` must be `> 0`
- Expense fails with `400` if funds are insufficient
- Unknown wallet returns `404`

## Project Structure

```text
fastapi/
  app/
    api/v1/          # Routers
    service/         # Business logic
    repository/      # Data access layer
    models.py        # SQLAlchemy models
    schemas.py       # Pydantic schemas
    database.py      # Engine/session/base
    dependency.py    # DB session dependency
  finance.db         # SQLite database file
  main.py            # FastAPI app entrypoint
  requirements.txt
```
