# Импортируем класс APIRouter для создания API endpoints
from fastapi import APIRouter, Depends
# Импортируем класс Session для работы с базой данных
from sqlalchemy.orm import Session

from app.api.v1.users import get_current_user
# Импортируем функцию для получения сессии базы данных через dependency injection
from app.dependency import get_db
from app.models import User
# Импортируем модель данных для создания кошелька
from app.schemas import CreateWalletRequest
# Импортируем сервис для работы с кошельками
from app.service import wallets as wallets_service

# Создаем роутер для группировки endpoints связанных с кошельками
router = APIRouter()

@router.get("/balance")
def get_balance(wallet_name: str | None = None, db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    # Вызываем сервис для получения баланса кошелька или общего баланса
    # db автоматически получается через dependency injection из get_db
    return wallets_service.get_wallet(db, current_user, wallet_name)

@router.post("/wallets")
def create_wallet(wallet: CreateWalletRequest, db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    # Вызываем сервис для создания нового кошелька
    # db автоматически получается через dependency injection из get_db
    return wallets_service.create_wallet(db, current_user, wallet)
