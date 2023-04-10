from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioAbrigo():

    def __init__(self, db:Session):
        self.db = db

    def create(self, abrigo: schemas.AbrigoBase):
        db_abrigo = models.Abrigo(
            nome=abrigo.nome,
            telefone=abrigo.telefone,
            cidade=abrigo.cidade
        )
        self.db.add(db_abrigo)
        self.db.commit()
        self.db.refresh(db_abrigo)
        return db_abrigo

    def read(self):
        return self.db.query(models.Abrigo).all()
    
    def update(self, id_abrigo:int, novos_dados:dict):
        abrigo_atualizado = self.db.query(models.Abrigo).filter(models.Abrigo.id == id_abrigo).first()
        for chave, valor in novos_dados.items():
            setattr(abrigo_atualizado, chave, valor)
        self.db.commit()
        return abrigo_atualizado    
