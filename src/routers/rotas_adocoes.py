from fastapi import APIRouter
from fastapi import Depends
from src.infra.sqlalchemy.config.database import get_db
from src.schemas import schemas
from src.infra.sqlalchemy.repositories.adocao import RepositorioAdocao
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/adocoes/', status_code=201)
def cria_adocoes(adocao:schemas.AdocaoBase, db:Session = Depends(get_db)):
    return RepositorioAdocao(db).create(adocao)

@router.get('/adocoes/', response_model=list[schemas.AdocaoBase])
def lista_adocao(db:Session = Depends(get_db)):
    return RepositorioAdocao(db).read()