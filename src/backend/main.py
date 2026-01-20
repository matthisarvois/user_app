from fastapi import FastAPI

from src.backend.api.routes.health import router as health_router
from src.backend.api.routes.users import router as users_router

from src.backend.db.session import engine
from src.backend.db.base import Base

# IMPORTANT : importer le modèle pour que SQLAlchemy "connaisse" la table
from src.backend.models.user import User  # noqa: F401


app = FastAPI(title="User API")

app.include_router(health_router)
app.include_router(users_router)

