# Импортируем класс Decimal для точных вычислений с деньгами
from decimal import Decimal

# Импортируем класс Session для работы с базой данных
from sqlalchemy.orm import Session

# Импортируем фабрику для создания сессий (не используется напрямую, но может понадобиться)
from app.database import SessionLocal
# Импортируем модель кошелька
from app.models import Wallet


def is_wallet_exist(db: Session, wallet_name: str) -> bool:
    # Выполняем запрос к таблице кошельков
    # Фильтруем по названию кошелька
    # Проверяем существует ли кошелек (если first() вернул None - кошелька нет)
    return db.query(Wallet).filter(Wallet.name == wallet_name).first() is not None


def add_income(db: Session, wallet_name: str, amount: Decimal) -> Wallet:
    # Находим кошелек по названию в базе данных
    wallet = db.query(Wallet).filter(Wallet.name == wallet_name).first()
    # Добавляем доход к балансу кошелька
    wallet.balance += amount
    # Возвращаем обновленный объект кошелька
    return wallet

def get_wallet_balance_by_name(db: Session, wallet_name: str) -> Wallet:
    # Выполняем запрос к таблице кошельков
    # Фильтруем по названию кошелька
    # Возвращаем первый найденный кошелек
    return db.query(Wallet).filter(Wallet.name == wallet_name).first()

def add_expense(db: Session, wallet_name: str, amount: Decimal) -> Wallet:
    # Находим кошелек по названию в базе данных
    wallet = db.query(Wallet).filter(Wallet.name == wallet_name).first()
    # Вычитаем расход из баланса кошелька
    wallet.balance -= amount
    # Возвращаем обновленный объект кошелька
    return wallet

def get_all_wallets(db: Session, ) -> list[Wallet]:
    # Выполняем запрос к таблице кошельков
    # Возвращаем список всех кошельков из базы данных
    return db.query(Wallet).all()

def create_wallet(db: Session, wallet_name: str, amount: Decimal) -> Wallet:
    # Создаем новый объект кошелька с указанным названием и балансом
    wallet = Wallet(name=wallet_name, balance=amount)
    # Добавляем кошелек в сессию базы данных
    db.add(wallet)
    # Применяем изменения к базе данных (но не сохраняем транзакцию)
    db.flush()
    # Возвращаем созданный объект кошелька
    return wallet


