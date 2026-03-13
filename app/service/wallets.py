# Импортируем класс HTTPException для обработки ошибок HTTP запросов
from fastapi import HTTPException

# Импортируем модель данных для создания кошелька
from app.schemas import CreateWalletRequest
# Импортируем репозиторий для работы с кошельками
from app.repository import wallets as wallets_repository

def get_wallet(wallet_name: str | None = None):
    # Если имя кошелька не указано - считаем общий баланс
    if wallet_name is None:
        # Получаем все кошельки из репозитория
        wallets = wallets_repository.get_all_wallets()
        return {"total_balance": sum([w.amount for w in wallets])} # Суммируем все значения из словаря BALANCE

    # Проверяем существует ли запрашиваемый кошелек
    if not wallets_repository.is_wallet_exist(wallet_name):
        raise HTTPException(status_code=404, detail=f"Wallet '{wallet_name}' not found")  # Если кошелька нет - возвращаем ошибку 404

    # Получаем баланс кошелька из репозитория
    wallet = wallets_repository.get_wallet_balance_by_name(wallet_name)
    return {"wallet": wallet.name, "balance": wallet.balance}  # Возвращаем баланс конкретного кошелька

def create_wallet(wallet: CreateWalletRequest):
    # Проверяем не существует ли уже такой кошелек
    if wallets_repository.is_wallet_exist(wallet.name):
        raise HTTPException(status_code=400, detail=f"Wallet '{wallet.name}' already exists")  # Если кошелек уже есть - возвращаем ошибку 400

    # Валидация name и initial_balance теперь в модели CreateWalletRequest!
    # Создаем новый кошелек с начальным балансом через репозиторий
    wallet = wallets_repository.create_wallet(wallet.name, wallet.initial_balance)
    # Возвращаем информацию о созданном кошельке
    return {
        "message": f"Wallet '{wallet.name}' created",
        "wallet": wallet.name,
        "balance": wallet.balance
    }
