# Импортируем класс FastAPI для создания веб-приложения
from fastapi import FastAPI

# Импортируем роутер для работы с кошельками
from app.api.v1.wallets import router as wallet_router
# Импортируем роутер для работы с операциями (доходы и расходы)
from app.api.v1.operations import router as operations_router
from app.api.v1.users import router as users_router
# Импортируем базовый класс для моделей и движок базы данных
from app.database import Base, engine

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Подключаем роутер для кошельков с префиксом /api/v1
app.include_router(wallet_router, prefix="/api/v1", tags=["wallet"])
# Подключаем роутер для операций с префиксом /api/v1
app.include_router(operations_router, prefix="/api/v1", tags=["operations"])
app.include_router(users_router, prefix="/api/v1", tags=["users"])

# Создаем все таблицы в базе данных при старте приложения
Base.metadata.create_all(bind=engine)