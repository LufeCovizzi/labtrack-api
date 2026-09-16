from sqlalchemy import Column, Integer, String, Text, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime, timezone


class Experiment(Base):
    __tablename__ = "experiments"

    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    description = Column(Text)
    responsible_researcher = Column(String(150))
    status = Column(String(30), default="em andamento")
    created_at = Column(DateTime, default=datetime.utcnow)

    # "samples" não é uma coluna no banco: é um atalho do SQLAlchemy pra
    # buscar todas as Sample cujo experiment_id aponta pra este Experiment
    samples = relationship("Sample", back_populates="experiment")


class Sample(Base):
    __tablename__ = "samples"

    id = Column(Integer, primary_key=True)
    # ForeignKey diz ao banco: esse valor tem que existir como id em experiments.
    # É isso que garante, no nível do banco, que não existe amostra "órfã"
    experiment_id = Column(Integer, ForeignKey("experiments.id"))
    code = Column(String(100))
    sample_type = Column(String(100))
    collected_at = Column(DateTime)
    storage_location = Column(String(150))
    created_at = Column(DateTime, default=datetime.utcnow)

    # lado inverso do relationship: sample.experiment devolve o objeto Experiment inteiro
    experiment = relationship("Experiment", back_populates="samples")


class Reagent(Base):
    __tablename__ = "reagents"

    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    manufacturer = Column(String(150))
    lot_number = Column(String(100))
    expiration_date = Column(DateTime)
    quantity_available = Column(Float)
    unit = Column(String(30))
    created_at = Column(DateTime, default=datetime.utcnow)