from fastapi import APIRouter
from fastapi import Depends
from src.infra.sqlalchemy.config.database import get_db
from src.schemas import schemas
from src.infra.sqlalchemy.repositories.abrigo import RepositorioAbrigo
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/abrigos/', status_code=201)
def cria_abrigos(abrigo:schemas.AbrigoBase, db:Session = Depends(get_db)):
    return RepositorioAbrigo(db).create(abrigo)

@router.get('/abrigos/', response_model=list[schemas.AbrigoBase])
def lista_abrigos(db:Session = Depends(get_db)):
    return RepositorioAbrigo(db).read()

@router.put('/abrigos/{id_abrigo}/', response_model=schemas.AbrigoBase)
def atualiza_abrigos(id_abrigo:int, novos_dados:dict, db:Session = Depends(get_db)):
    return RepositorioAbrigo(db).update(id_abrigo=id_abrigo, novos_dados=novos_dados)