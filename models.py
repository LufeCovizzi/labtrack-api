from sqlalchemy import Column, Integer, String, Text, DateTime
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