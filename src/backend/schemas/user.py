from pydantic import BaseModel, EmailStr
from datetime import date

#Ce que l'user envoie pour créer un user
class UserCreate(BaseModel):
    nom: str
    email:EmailStr
    genre: str | None = None
    age:int
    DateDaernierControlTech: date

class UserOut(BaseModel):
    id: int
    nom: str
    email:EmailStr
    genre: str | None = None
    age:int
    DateDaernierControlTech: date | None = None
    
    #Cela va permettre la conversion de sqlalchempy en json
    class Config:
        from_attributes = True
    