from fastapi import APIRouter, HTTPException
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

@router.get('/pets/{id_pet}', response_model=schemas.PetBase)
def busca_por_id(id_pet:int, db:Session = Depends(get_db)):
    pet_localizado = RepositorioPet(db).read_by_id(id_pet=id_pet)
    if not pet_localizado:
        raise HTTPException(status_code=404, detail=f"Pet com o id {id_pet} não existe")
    return pet_localizado


@router.put('/pets/{id_pet}/', response_model=schemas.PetBase)
def atualiza_pets(id_pet:int, novos_dados:dict, db:Session = Depends(get_db)):
    return RepositorioPet(db).update(id_pet=id_pet, novos_dados=novos_dados)