from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import create_db
from src.routers import rotas_tutores, rotas_pets, rotas_abrigos, rotas_adocoes

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

#ROTA DE TUTORES

app.include_router(rotas_tutores.router)

#ROTA DE PETS

app.include_router(rotas_pets.router)


#ROTA DOS ABRIGO

app.include_router(rotas_abrigos.router)


#ROTAS DE ADOCAO

app.include_router(rotas_adocoes.router)