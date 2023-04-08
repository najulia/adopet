from sqlalchemy.orm import Session, session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import update

class RepositorioTutor():

    def __init__(self, db:Session):
        self.db = db

    def create(self, tutor:schemas.TutorCreate):
        db_tutor = models.Tutor(
            nome=tutor.nome,
            email=tutor.email, 
            eh_ativo=tutor.eh_ativo, 
            senha=tutor.senha
        )
        self.db.add(db_tutor)
        self.db.commit()
        self.db.refresh(db_tutor)
        return db_tutor

    def read(self):
        return self.db.query(models.Tutor).all()

    def read_by_id(self):
        pass

    def update(self, id_tutor:int, novos_dados:dict):
        tutor_atualizado = self.db.query(models.Tutor).filter(models.Tutor.id == id_tutor).first()
        for chave, valor in novos_dados.items():
            setattr(tutor_atualizado, chave, valor)
        self.db.commit()
        return tutor_atualizado


    def deactivate(self):
        pass

    def activate(self):
        pass