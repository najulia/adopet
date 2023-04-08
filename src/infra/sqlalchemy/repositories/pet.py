from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioPet():

    def __init__(self, db:Session):
        self.db = db

    def create(self, pet: schemas.PetCreate):
        db_pet = models.Pet(
            nome=pet.nome,
            sobre=pet.sobre,
            foto=pet.foto,
            foi_adotado=pet.foi_adotado,
            abrigo_id=pet.abrigo_id
        )
        self.db.add(db_pet)
        self.db.commit()
        self.db.refresh(db_pet)
        return db_pet

    def read(self):
<<<<<<< HEAD
        return self.db.query(models.Pet).all()
    
    def update(self, id_pet:int, novos_dados:dict):
        pet_atualizado = self.db.query(models.Pet).filter(models.Pet.id == id_pet).first()
        for chave, valor in novos_dados.items():
            setattr(pet_atualizado, chave, valor)
        self.db.commit()
        return pet_atualizado
=======
        return self.db.query(models.Pet).all()
>>>>>>> bcab1bd5ddba8e21bcc66da42c222b5804ddfc43
