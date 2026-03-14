# Импортируем класс Decimal для точных вычислений с деньгами
from decimal import Decimal

# Импортируем классы для работы с базой данных из SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

# Импортируем базовый класс для моделей
from app.database import Base


# Модель пользователя в базе данных
class User(Base):
    # Название таблицы в базе данных
    __tablename__ = "user"
    # Уникальный идентификатор пользователя (первичный ключ)
    id: Mapped[int] = mapped_column(primary_key=True)
    # Логин пользователя (уникальный, обязательный для заполнения)
    login: Mapped[str] = mapped_column(unique=True)


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
    # Идентификатор пользователя-владельца кошелька (внешний ключ на таблицу user)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
