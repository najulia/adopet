from fastapi import APIRouter,  HTTPException
from fastapi import Depends
from src.infra.sqlalchemy.config.database import get_db
from src.schemas import schemas
from src.infra.sqlalchemy.repositories.tutor import RepositorioTutor
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models


router = APIRouter()

@router.post('/tutores/', status_code=201)
def cria_tutores(tutor:schemas.TutorCreate, db:Session = Depends(get_db)):
    tutor_criado = RepositorioTutor(db).create(tutor)
    return tutor_criado

@router.get('/tutores/', response_model=list[schemas.TutorBase])
def lista_tutores(db:Session = Depends(get_db)):
    return RepositorioTutor(db).read()

@router.get('/tutores/{id_tutor}', response_model=schemas.TutorBase)
def busca_por_id(id_tutor:int, db:Session = Depends(get_db)):
    tutor_localizado = RepositorioTutor(db).read_by_id(id_tutor=id_tutor)
    if not tutor_localizado:
        raise HTTPException(status_code=404, detail=f"Tutor com o id {id_tutor} não existe")
    return tutor_localizado

@router.put('/tutores/{id_tutor}', response_model=schemas.TutorBase)
def atualiza_tutores(id_tutor:int, novos_dados:dict, db:Session = Depends(get_db)):
    return RepositorioTutor(db).update(id_tutor=id_tutor, novos_dados=novos_dados)
