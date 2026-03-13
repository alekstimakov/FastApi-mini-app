# Импортируем классы из библиотеки Pydantic для создания моделей данных и валидации
from pydantic import BaseModel, Field, field_validator


# Модель для описания операции с деньгами
# BaseModel из Pydantic автоматически валидирует данные
class OperationRequest(BaseModel):
    # Название кошелька (обязательное поле, максимум 127 символов)
    wallet_name: str = Field(..., max_length=127)
    # Сумма операции (обязательное поле, должна быть положительной)
    amount: float
    # Описание операции (необязательное поле, максимум 255 символов)
    description: str | None = Field(None, max_length=255)

    # Валидатор для проверки что сумма положительная
    @field_validator('amount')
    def amount_must_be_positive(cls, v: float) -> float:
        # Проверяем что значение больше нуля
        if v <= 0:
            # Если нет - выбрасываем ошибку валидации
            raise ValueError('Amount must be positive')
        # Возвращаем значение если все ок
        return v

    # Валидатор для проверки что имя кошелька не пустое
    @field_validator('wallet_name')
    def wallet_name_not_empty(cls, v: str) -> str:
        # Убираем пробелы по краям
        v = v.strip()
        # Проверяем что строка не пустая
        if not v:
            # Если пустая - выбрасываем ошибку валидации
            raise ValueError('Wallet name cannot be empty')
        # Возвращаем очищенное значение
        return v


# Модель для создания кошелька
class CreateWalletRequest(BaseModel):
    # Название кошелька (обязательное поле, максимум 127 символов)
    name: str = Field(..., max_length=127)
    # Начальный баланс (необязательное поле, по умолчанию 0)
    initial_balance: float = 0

    # Валидатор для проверки что имя кошелька не пустое
    @field_validator('name')
    def name_not_empty(cls, v: str) -> str:
        # Убираем пробелы по краям
        v = v.strip()
        # Проверяем что строка не пустая
        if not v:
            # Если пустая - выбрасываем ошибку валидации
            raise ValueError('Wallet name cannot be empty')
        # Возвращаем очищенное значение
        return v

    # Валидатор для проверки что начальный баланс не отрицательный
    @field_validator('initial_balance')
    def balance_not_negative(cls, v: float) -> float:
        # Проверяем что значение не отрицательное
        if v < 0:
            # Если отрицательное - выбрасываем ошибку валидации
            raise ValueError('Initial balance cannot be negative')
        # Возвращаем значение если все ок
        return v

