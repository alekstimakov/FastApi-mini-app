# Импортируем класс Decimal для точных вычислений с деньгами
from decimal import Decimal

# Импортируем классы для работы с базой данных из SQLAlchemy
from sqlalchemy import Column, Integer
from sqlalchemy.orm import Mapped, mapped_column

# Импортируем базовый класс для моделей
from app.database import Base


# Модель кошелька в базе данных
class Wallet(Base):
    # Название таблицы в базе данных
    __tablename__ = "wallet"

    # Уникальный идентификатор кошелька (первичный ключ)
    id: Mapped[int] = mapped_column(primary_key=True)
    # Название кошелька
    name: Mapped[str]
    # Баланс кошелька (используем Decimal для точных вычислений)
    balance: Mapped[Decimal]

