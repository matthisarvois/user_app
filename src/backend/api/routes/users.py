# APIRouter = permet de définir un groupe de routes
# Depends = système d'injection de dépendances de FastAPI
# HTTPException = permet de renvoyer des erreurs HTTP propres
from fastapi import APIRouter, Depends, HTTPException

# AsyncSession = type de session SQLAlchemy async
from sqlalchemy.ext.asyncio import AsyncSession

# select = permet d'écrire des requêtes SELECT SQL
from sqlalchemy import select

# get_session = fonction qui fournit une session DB aux routes
from src.backend.db.session import get_session

# User = modèle SQLAlchemy (table users)
from src.backend.models.user import User

# UserCreate / UserOut = schémas Pydantic (input / output API)
from src.backend.schemas.user import UserCreate, UserOut


# 🧠 router = l'objet que FastAPI va importer dans main.py
# prefix="/users" :
#   toutes les routes ici commenceront par /users
# tags=["users"] :
#   juste pour organiser Swagger (/docs)
router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserOut)
async def create_user(
    payload: UserCreate,
    session: AsyncSession = Depends(get_session),
):
    """
    Crée un utilisateur dans la base.
    - payload : données envoyées par le frontend
    - session : session DB injectée automatiquement par FastAPI
    """

    # Vérifie si un user avec le même email existe déjà
    res = await session.execute(
        select(User).where(User.email == str(payload.email))
    )

    if res.scalar_one_or_none():
        raise HTTPException(
            status_code=409,
            detail="Email already exists",
        )

    # Création de l'objet SQLAlchemy (PAS encore écrit en DB)
    user = User(
        nom=payload.nom,
        email=str(payload.email),
        age=payload.age,
        genre = payload.genre,
        DateDaernierControlTech = payload.DateDaernierControlTech,
        
        
    )

    # Ajout à la session
    session.add(user)

    # Commit = écriture réelle dans la DB
    await session.commit()

    # Refresh = recharge depuis la DB (récupère l'id auto)
    await session.refresh(user)

    return user


@router.get("/", response_model=list[UserOut])
async def list_users(
    session: AsyncSession = Depends(get_session),
):
    """
    Retourne la liste de tous les utilisateurs
    """

    res = await session.execute(select(User))
    return res.scalars().all()