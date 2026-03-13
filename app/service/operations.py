# Импортируем класс HTTPException для обработки ошибок HTTP запросов
from fastapi import HTTPException

# Импортируем модель данных для операций с деньгами
from app.schemas import OperationRequest
# Импортируем репозиторий для работы с кошельками
from app.repository import wallets as wallets_repository

def add_income(operation: OperationRequest):
    # Проверяем существует ли кошелек
    if not wallets_repository.is_wallet_exist(operation.wallet_name):
        raise HTTPException(
            status_code=404,
            detail=f"Wallet '{operation.wallet_name}' not found"
        )  # Если кошелька нет - возвращаем ошибку 404

    # Валидация amount > 0 теперь в модели OperationRequest!
    # Добавляем доход к балансу кошелька через репозиторий
    new_balance = wallets_repository.add_income(operation.wallet_name, operation.amount)

    # Возвращаем информацию об операции
    return {
        "message": "Income added",
        "wallet": operation.wallet_name,
        "amount": operation.amount,
        "description": operation.description,
        "new_balance": new_balance
    }

def add_expense(operation: OperationRequest):
    # Проверяем существует ли кошелек
    if not wallets_repository.is_wallet_exist(operation.wallet_name):
        raise HTTPException(
            status_code=404,
            detail=f"Wallet '{operation.wallet_name}' not found"
        )  # Если кошелька нет - возвращаем ошибку 404

    # Валидация amount > 0 теперь в модели OperationRequest!

    # Проверяем достаточно ли средств в кошельке (это бизнес-логика, не валидация!)
    # Получаем текущий баланс кошелька из репозитория
    balance = wallets_repository.get_wallet_balance_by_name(operation.wallet_name)
    if balance < operation.amount:  # Если баланс меньше суммы расхода
        raise HTTPException(
            status_code=400,
            detail=f"Insufficient funds. Available: {balance}"
        )  # Если денег недостаточно - возвращаем ошибку 400

    # Вычитаем расход из баланса кошелька через репозиторий
    new_balance = wallets_repository.add_expense(operation.wallet_name, operation.amount)

    # Возвращаем информацию об операции
    return {
        "message": "Expense added",
        "wallet": operation.wallet_name,
        "amount": operation.amount,
        "description": operation.description,
        "new_balance": new_balance
    }
