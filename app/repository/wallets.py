# Словарь для хранения балансов кошельков (ключ - название кошелька, значение - баланс)
BALANCE: dict[str, float] = {}

def is_wallet_exist(wallet_name: str) -> bool:
    # Проверяем существует ли кошелек в словаре BALANCE
    return wallet_name in BALANCE

def add_income(wallet_name: str, amount: float) -> float:
    # Добавляем доход к балансу кошелька
    BALANCE[wallet_name] += amount
    # Возвращаем обновленный баланс кошелька
    return BALANCE[wallet_name]

def get_wallet_balance_by_name(wallet_name: str) -> float:
    # Возвращаем баланс кошелька по его названию
    return BALANCE[wallet_name]

def add_expense(wallet_name: str, amount: float) -> float:
    # Вычитаем расход из баланса кошелька
    BALANCE[wallet_name] -= amount
    # Возвращаем обновленный баланс кошелька
    return BALANCE[wallet_name]

def get_all_wallets() -> dict[str, float]:
    # Возвращаем копию словаря со всеми кошельками (чтобы не изменять оригинал)
    return BALANCE.copy()

def create_wallet(wallet_name: str, amount: float) -> float:
    # Создаем новый кошелек с указанным начальным балансом
    BALANCE[wallet_name] = amount
    # Возвращаем баланс созданного кошелька
    return BALANCE[wallet_name]


