from pydantic import BaseModel
from typing import Optional

class TutorBase(BaseModel):
    id: Optional[int] = None
    nome: str 
    email: str 
    eh_ativo:  bool = True

    class Config:
        orm_mode = True   

class TutorCreate(TutorBase):
    senha: str 

class AbrigoBase(BaseModel):

    id: Optional[int]
    nome: str
    telefone: str
    cidade: str
    #pets: List[PetBase] = []

    class Config:
        orm_mode = True


class PetBase(BaseModel):
    id: Optional[int]
    nome: str 
    sobre: str
    foto: str | None = None
    foi_adotado: bool = False
    abrigo: Optional[AbrigoBase]

    class Config:
        orm_mode = True

class PetCreate(PetBase):
    abrigo_id: int

    class Config:
        orm_mode = True

class AdocaoBase(BaseModel):
    id: Optional[int]
    data: str 

    pet_id: int
    tutor_id: int

    class Config:
        orm_mode = True


