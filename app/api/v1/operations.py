# Импортируем класс APIRouter для создания API endpoints
from fastapi import APIRouter, Depends
# Импортируем класс Session для работы с базой данных
from sqlalchemy.orm import Session

# Импортируем функцию для получения сессии базы данных через dependency injection
from app.dependency import get_db, get_current_user
from app.models import User
# Импортируем модель данных для операций с деньгами
from app.schemas import OperationRequest
# Импортируем сервис для работы с операциями
from app.service import operations as operations_service

# Создаем роутер для группировки endpoints связанных с операциями
router = APIRouter()

@router.post("/operations/income")
def add_income(operation: OperationRequest, db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    # Вызываем сервис для добавления дохода к балансу кошелька
    # db автоматически получается через dependency injection из get_db
    return operations_service.add_income(db, current_user, operation)


@router.post("/operations/expense")
def add_expense(operation: OperationRequest, db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    # Вызываем сервис для добавления расхода (вычитания из баланса кошелька)
    # db автоматически получается через dependency injection из get_db
    return operations_service.add_expense(db, current_user, operation)
