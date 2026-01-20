from fastapi import FastAPI
from src.backend.api.routes.health import router as health_router

# On importe engine juste pour vérifier que le fichier session.py
# est correct et que SQLAlchemy arrive à créer le moteur.
from src.backend.db.session import engine

app = FastAPI(title="User API")
app.include_router(health_router)

# On déclare une fonction "startup" : FastAPI l'exécute
# automatiquement au démarrage de l'application.
#
# Conséquence : si ta DB URL est mauvaise ou si aiosqlite manque,
# tu le verras dès le démarrage (erreur immédiate).
@app.on_event("startup")
async def startup():
    _ = engine  # on touche la variable pour confirmer que l'import marche