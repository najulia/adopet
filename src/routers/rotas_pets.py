from fastapi import APIRouter
from fastapi import Depends
from src.infra.sqlalchemy.config.database import get_db
from src.schemas import schemas
from src.infra.sqlalchemy.repositories.pet import RepositorioPet
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/pets/', status_code=201)
def cria_pets(pet:schemas.PetCreate, db:Session = Depends(get_db)):
    return RepositorioPet(db).create(pet)

@router.get('/pets/', response_model=list[schemas.PetBase])
def lista_pets(db:Session = Depends(get_db)):
    return RepositorioPet(db).read()

@router.put('/pets/{id_pet}/', response_model=schemas.PetBase)
def atualiza_pets(id_pet:int, novos_dados:dict, db:Session = Depends(get_db)):
    return RepositorioPet(db).update(id_pet=id_pet, novos_dados=novos_dados)