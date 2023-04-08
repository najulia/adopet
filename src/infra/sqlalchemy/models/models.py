from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base

class Tutor(Base):
    __tablename__ = 'tutores'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100),  nullable=False)
    email = Column(String(200))
    senha = Column(String(100))
    eh_ativo = Column(Boolean, default=True)

    adocoes = relationship("Adocao", back_populates="tutor")

    
class Abrigo(Base):
    __tablename__ = 'abrigos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100),  nullable=False)
    telefone = Column(String(20),  nullable=False)
    cidade = Column(String(100),  nullable=False)

    pets = relationship("Pet", back_populates="abrigo")


class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100),  nullable=False)
    sobre = Column(Text,  nullable=False)
    foto = Column(String(50)) 
    foi_adotado = Column(Boolean, default=False)

    abrigo_id = Column(Integer, ForeignKey("abrigos.id", ondelete='CASCADE', name='abrigosfk'))
    abrigo = relationship("Abrigo", back_populates="pets")

    adocoes = relationship("Adocao", back_populates="pets")

    def adotar(self):
        self.foi_adotado = True; 
        self.abrigo_id = None;


class Adocao(Base):
    __tablename__ = 'adocoes'

    id = Column(Integer, primary_key=True, index=True)
    data = Column(String(100))

    pet_id = Column(Integer, ForeignKey("pets.id", ondelete='CASCADE', name='petsfk'))
    pets = relationship("Pet", back_populates="adocoes")

    tutor_id = Column(Integer, ForeignKey("tutores.id", ondelete='CASCADE', name='tutoresfk'))
    tutor = relationship("Tutor", back_populates="adocoes")