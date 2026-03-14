# Импортируем тип Generator для создания генератора сессий базы данных
from typing import Generator

# Импортируем класс Session для работы с базой данных
from sqlalchemy.orm import Session

# Импортируем фабрику для создания сессий базы данных
from app.database import SessionLocal


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

