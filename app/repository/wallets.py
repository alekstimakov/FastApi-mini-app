# Импортируем класс Decimal для точных вычислений с деньгами
from decimal import Decimal

# Импортируем класс Session для работы с базой данных
from sqlalchemy.orm import Session

# Импортируем фабрику для создания сессий (не используется напрямую, но может понадобиться)
# Импортируем модель кошелька
from app.models import Wallet


# Проверяет существует ли кошелек с указанным названием у пользователя
def is_wallet_exist(db: Session, user_id: int, wallet_name: str) -> bool:
    # Выполняем запрос к таблице кошельков
    # Фильтруем по названию кошелька и идентификатору пользователя
    # Проверяем существует ли кошелек (если first() вернул None - кошелька нет)
    return db.query(Wallet).filter(Wallet.name == wallet_name, Wallet.user_id == user_id).first() is not None


# Добавляет доход к балансу кошелька
def add_income(db: Session, user_id: int, wallet_name: str, amount: Decimal) -> Wallet:
    # Находим кошелек по названию в базе данных
    wallet = db.query(Wallet).filter(Wallet.name == wallet_name, Wallet.user_id == user_id).first()
    # Добавляем доход к балансу кошелька
    wallet.balance += amount
    # Возвращаем обновленный объект кошелька
    return wallet

# Находит кошелек в базе данных по названию
def get_wallet_balance_by_name(db: Session, user_id: int, wallet_name: str) -> Wallet:
    # Выполняем запрос к таблице кошельков
    # Фильтруем по названию кошелька и идентификатору пользователя
    # Возвращаем первый найденный кошелек
    return db.query(Wallet).filter(Wallet.name == wallet_name, Wallet.user_id == user_id).first()

# Вычитает расход из баланса кошелька
def add_expense(db: Session, user_id: int, wallet_name: str, amount: Decimal) -> Wallet:
    # Находим кошелек по названию в базе данных
    wallet = db.query(Wallet).filter(Wallet.name == wallet_name, Wallet.user_id == user_id).first()
    # Вычитаем расход из баланса кошелька
    wallet.balance -= amount
    # Возвращаем обновленный объект кошелька
    return wallet

# Получает все кошельки пользователя из базы данных
def get_all_wallets(db: Session, user_id: int, ) -> list[Wallet]:
    # Выполняем запрос к таблице кошельков
    # Фильтруем по идентификатору пользователя
    # Возвращаем список всех кошельков пользователя
    return db.query(Wallet).filter(Wallet.user_id == user_id).all()

# Создает новый кошелек в базе данных
def create_wallet(db: Session, user_id: int, wallet_name: str, amount: Decimal) -> Wallet:
    # Создаем новый объект кошелька с указанным названием и балансом
    wallet = Wallet(name=wallet_name, balance=amount, user_id=user_id)
    # Добавляем кошелек в сессию базы данных
    db.add(wallet)
    # Применяем изменения к базе данных (но не сохраняем транзакцию)
    db.flush()
    # Возвращаем созданный объект кошелька
    return wallet


