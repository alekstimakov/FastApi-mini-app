# Импортируем класс APIRouter для создания API endpoints
from fastapi import APIRouter

# Импортируем модель данных для создания кошелька
from app.schemas import CreateWalletRequest
# Импортируем сервис для работы с кошельками
from app.service import wallets as wallets_service

# Создаем роутер для группировки endpoints связанных с кошельками
router = APIRouter()

@router.get("/balance")
def get_balance(wallet_name: str | None = None):
    # Вызываем сервис для получения баланса кошелька или общего баланса
    return wallets_service.get_wallet(wallet_name)

@router.post("/wallets")
def create_wallet(wallet: CreateWalletRequest):
    # Вызываем сервис для создания нового кошелька
    return wallets_service.create_wallet(wallet)

