# Импортируем класс APIRouter для создания API endpoints
from fastapi import APIRouter, Depends
# Импортируем класс Session для работы с базой данных
from sqlalchemy.orm import Session

# Импортируем функции для получения сессии базы данных и текущего пользователя
from app.dependency import get_db, get_current_user
from app.models import User
# Импортируем модели данных для пользователей
from app.schemas import UserRequest, UserResponse
# Импортируем сервис для работы с пользователями
from app.service import users as users_service

# Создаем роутер для группировки endpoints связанных с пользователями
router = APIRouter()

@router.post("/users", response_model=UserResponse)
def create_user(payload: UserRequest, db: Session = Depends(get_db)):
    # Вызываем сервис для создания нового пользователя
    # db автоматически получается через dependency injection из get_db
    return users_service.create_user(db, payload.login)

@router.get("/users/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    # Преобразуем модель SQLAlchemy в модель Pydantic для ответа
    return UserResponse.model_validate(current_user)
