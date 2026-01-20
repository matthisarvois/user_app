# create_async_engine = fabrique un "moteur" de connexion asynchrone.
# async_sessionmaker = fabrique des sessions asynchrones.
# AsyncSession = type de session (objet qui exécute les requêtes SQL)
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

# On importe tes réglages (config DB)
from src.backend.core.config import settings


# engine = le "moteur" SQLAlchemy.
# echo=False :
# - si True, SQLAlchemy affiche toutes les requêtes SQL dans la console (je le met pour voir au début ce que cela donne)
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
)


# AsyncSessionLocal = un "fabricant" (factory) de sessions.
# class_=AsyncSession :
# - précise que les sessions créées sont bien des AsyncSession
AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


# get_session = une "dépendance" FastAPI (Dependency Injection)
#
# FastAPI peut faire Depends(get_session) dans une route,
# ce qui lui donnera une session DB automatiquement.

# async with AsyncSessionLocal() as session:
# - ouvre une session DB
# - garantit que la session est "fermée proprement" à la fin
#   même si une erreur arrive
#
# yield session :
# - yield = renvoie la session au code appelant (ex: ta route)
# - quand la route finit, FastAPI revient ici et ferme la session
async def get_session() :
    async with AsyncSessionLocal() as session:
        yield session