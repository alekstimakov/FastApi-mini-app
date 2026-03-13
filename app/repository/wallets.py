from app.database import SessionLocal

from app.models import Wallet


# Словарь для хранения балансов кошельков (ключ - название кошелька, значение - баланс)
def is_wallet_exist(wallet_name: str) -> bool:
    # Проверяем существует ли кошелек в словаре BALANCE
    db = SessionLocal()
    try:
        return db.query(Wallet).filter(Wallet.name == wallet_name).first() is not None
    finally:
        db.close()


def add_income(wallet_name: str, amount: float) -> Wallet:
    # Добавляем доход к балансу кошелька
    db = SessionLocal()
    try:
        wallet = db.query(Wallet).filter(Wallet.name == wallet_name).first()
        wallet.amount += amount
        db.commit()
        return wallet
    finally:
        db.close()


def get_wallet_balance_by_name(wallet_name: str) -> Wallet:
    db = SessionLocal()
    try:
        return db.query(Wallet).filter(Wallet.name == wallet_name).first()
    finally:
        db.close()

def add_expense(wallet_name: str, amount: float) -> Wallet:
    # Добавляем доход к балансу кошелька
    db = SessionLocal()
    try:
        wallet = db.query(Wallet).filter(Wallet.name == wallet_name).first()
        wallet.amount -= amount
        db.commit()
        return wallet
    finally:
        db.close()


def get_all_wallets() -> list[Wallet]:
    # Возвращаем копию словаря со всеми кошельками (чтобы не изменять оригинал)
    db = SessionLocal()
    try:
        return db.query(Wallet).all()
    finally:
        db.close()

def create_wallet(wallet_name: str, amount: float) -> Wallet:
    # Создаем новый кошелек с указанным начальным балансом
    db = SessionLocal()
    try:
        wallet = Wallet(name=wallet_name, amount=amount)
        db.add(wallet)
        db.commit()
        db.refresh(wallet)
        return wallet
    finally:
        db.close()

