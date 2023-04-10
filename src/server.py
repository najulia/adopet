from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import get_db, create_db
from src.schemas import schemas
from src.infra.sqlalchemy.repositories.tutor import RepositorioTutor
from src.infra.sqlalchemy.repositories.abrigo import RepositorioAbrigo
from src.infra.sqlalchemy.repositories.pet import RepositorioPet
from src.infra.sqlalchemy.repositories.adocao import RepositorioAdocao
from sqlalchemy.orm import Session

create_db()

app = FastAPI()

#CORS

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#TUTOR 

@app.post('/tutores/', status_code=201)
def cria_tutores(tutor:schemas.TutorCreate, db:Session = Depends(get_db)):
    tutor_criado = RepositorioTutor(db).create(tutor)
    return tutor_criado

@app.get('/tutores/', response_model=list[schemas.TutorBase])
def lista_tutores(db:Session = Depends(get_db)):
    return RepositorioTutor(db).read()

@app.put('/tutores/{id_tutor}', response_model=schemas.TutorBase)
def atualiza_tutores(id_tutor:int, novos_dados:dict, db:Session = Depends(get_db)):
    return RepositorioTutor(db).update(id_tutor=id_tutor, novos_dados=novos_dados)

#PET

@app.post('/pets/', status_code=201)
def cria_pets(pet:schemas.PetCreate, db:Session = Depends(get_db)):
    return RepositorioPet(db).create(pet)

@app.get('/pets/', response_model=list[schemas.PetBase])
def lista_pets(db:Session = Depends(get_db)):
    return RepositorioPet(db).read()

@app.put('/pets/{id_pet}/', response_model=schemas.PetBase)
def atualiza_pets(id_pet:int, novos_dados:dict, db:Session = Depends(get_db)):
    return RepositorioPet(db).update(id_pet=id_pet, novos_dados=novos_dados)

#ABRIGO

@app.post('/abrigos/', status_code=201)
def cria_abrigos(abrigo:schemas.AbrigoBase, db:Session = Depends(get_db)):
    return RepositorioAbrigo(db).create(abrigo)

@app.get('/abrigos/', response_model=list[schemas.AbrigoBase])
def lista_abrigos(db:Session = Depends(get_db)):
    return RepositorioAbrigo(db).read()

@app.put('/abrigos/{id_abrigo}/', response_model=schemas.AbrigoBase)
def atualiza_abrigos(id_abrigo:int, novos_dados:dict, db:Session = Depends(get_db)):
    return RepositorioAbrigo(db).update(id_abrigo=id_abrigo, novos_dados=novos_dados)

#ADOCAO

@app.post('/adocoes/', status_code=201)
def cria_adocoes(adocao:schemas.AdocaoBase, db:Session = Depends(get_db)):
    return RepositorioAdocao(db).create(adocao)

@app.get('/adocoes/', response_model=list[schemas.AdocaoBase])
def lista_adocao(db:Session = Depends(get_db)):
    return RepositorioAdocao(db).read()