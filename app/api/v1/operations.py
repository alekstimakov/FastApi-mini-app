# Импортируем класс APIRouter для создания API endpoints
from fastapi import APIRouter

# Импортируем модель данных для операций с деньгами
from app.schemas import OperationRequest
# Импортируем сервис для работы с операциями
from app.service import operations as operations_service

# Создаем роутер для группировки endpoints связанных с операциями
router = APIRouter()

@router.post("/operations/income")
def add_income(operation: OperationRequest):
    # Вызываем сервис для добавления дохода к балансу кошелька
    return operations_service.add_income(operation)


@router.post("/operations/expense")
def add_expense(operation: OperationRequest):
    # Вызываем сервис для добавления расхода (вычитания из баланса кошелька)
    return operations_service.add_expense(operation)
