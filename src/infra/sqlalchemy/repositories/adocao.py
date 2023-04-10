from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioAdocao():

    def __init__(self, db:Session):
        self.db = db

    def create(self, adocao: schemas.AdocaoBase):
        db_adocao = models.adocao(
            nome=adocao.nome,
            data=adocao.data,
            pet_id=adocao.pet_id,
            tutor_id=adocao.tutor_id
        )
        self.db.add(db_adocao)
        self.db.commit()
        self.db.refresh(db_adocao)
        return db_adocao

    def read(self):
        return self.db.query(models.Adocao).all()
    
    def update(self, id_adocao:int, novos_dados:dict):
        adocao_atualizada = self.db.query(models.Adocao).filter(models.adocao.id == id_adocao).first()
        for chave, valor in novos_dados.items():
            setattr(adocao_atualizada, chave, valor)
        self.db.commit()
        return adocao_atualizada  
