# Импортируем класс HTTPException для обработки ошибок HTTP запросов
from fastapi import HTTPException
# Импортируем класс Session для работы с базой данных
from sqlalchemy.orm import Session

# Импортируем модель данных для создания кошелька
from app.schemas import CreateWalletRequest
# Импортируем репозиторий для работы с кошельками
from app.repository import wallets as wallets_repository

def get_wallet(db: Session, wallet_name: str | None = None):
    # Если имя кошелька не указано - считаем общий баланс
    if wallet_name is None:
        # Получаем все кошельки из репозитория
        wallets = wallets_repository.get_all_wallets(db)
        return {"total_balance": sum([w.balance for w in wallets])}  # Суммируем балансы всех кошельков

    # Проверяем существует ли запрашиваемый кошелек
    if not wallets_repository.is_wallet_exist(db, wallet_name):
        raise HTTPException(status_code=404, detail=f"Wallet '{wallet_name}' not found")  # Если кошелька нет - возвращаем ошибку 404

    # Получаем кошелек из репозитория по названию
    wallet = wallets_repository.get_wallet_balance_by_name(db, wallet_name)
    return {"wallet": wallet.name, "balance": wallet.balance}  # Возвращаем баланс конкретного кошелька

def create_wallet(db: Session, wallet: CreateWalletRequest):
    # Проверяем не существует ли уже такой кошелек
    if wallets_repository.is_wallet_exist(db, wallet.name):
        raise HTTPException(status_code=400, detail=f"Wallet '{wallet.name}' already exists")  # Если кошелек уже есть - возвращаем ошибку 400

    # Валидация name и initial_balance теперь в модели CreateWalletRequest!
    # Создаем новый кошелек с начальным балансом через репозиторий
    wallet = wallets_repository.create_wallet(db, wallet.name, wallet.initial_balance)
    # Сохраняем изменения в базе данных
    db.commit()
    # Возвращаем информацию о созданном кошельке
    return {
        "message": f"Wallet '{wallet.name}' created",
        "wallet": wallet.name,
        "balance": wallet.balance
    }
