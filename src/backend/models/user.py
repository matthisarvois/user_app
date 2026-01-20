from sqlalchemy import Integer, String, Date
from datetime import date
#des trucs pour sql
from sqlalchemy.orm import Mapped, mapped_column #Nouvelle facon de déclarer des colonnes
from src.backend.db.base import Base

#On créer la base sql en python
class User(Base):
    #Nom de la table
    __tablename__ = "utilisateur"
    #Identifiant clé primaire autoincrémentée
    id: Mapped[int] = mapped_column(Integer, primary_key=True,index=True)
    #Nom, texte et nullable = Fase ca veut dire que c'est obligatoire
    nom: Mapped[str] = mapped_column(String(120),nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    
    genre: Mapped[str|None] = mapped_column(String(300), nullable=True)
    
    DateDaernierControlTech: Mapped[date|None] = mapped_column(Date, nullable=True)
    
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    

