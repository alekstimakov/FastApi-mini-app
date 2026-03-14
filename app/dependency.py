# Импортируем тип Generator для создания генератора сессий базы данных
from typing import Generator

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# Импортируем класс Session для работы с базой данных
from sqlalchemy.orm import Session

# Импортируем фабрику для создания сессий базы данных
from app.database import SessionLocal
from app.models import User
from app.repository import users as users_repository


# Схема безопасности для HTTP Bearer токенов (токен передается в заголовке Authorization)
security = HTTPBearer()


# Функция для получения сессии базы данных через dependency injection в FastAPI
def get_db() -> Generator[Session, None, None]:
    # Создаем новую сессию для работы с базой данных
    db = SessionLocal()
    try:
        # Возвращаем сессию через yield (это позволяет FastAPI автоматически закрыть сессию после использования)
        yield db
    finally:
        # Закрываем сессию базы данных в любом случае (даже если произошла ошибка)
        db.close()


# Функция для получения текущего пользователя из токена авторизации
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security),
                     db: Session = Depends(get_db)) -> User:
    # Извлекаем логин из токена авторизации (токен передается в заголовке Authorization)
    login = credentials.credentials
    # Ищем пользователя в базе данных по логину
    user = users_repository.get_user(db, login)
    # Если пользователь не найден - возвращаем ошибку 401 (неавторизован)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    # Возвращаем найденного пользователя
    return user