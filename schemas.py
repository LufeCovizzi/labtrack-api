from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# O que a API recebe. O que é obrigatório ou não na validação da entrada
# status: str = "em andamento" mostra que status tem um valor obrigatório igual em models.py, caso o usuário tente criar um experimento sem mandar o campo status o Pydantic já preenche com "em andamento" 
class ExperimentCreate(BaseModel):
    title: str
    description: str
    responsible_researcher: str
    status: str = "em andamento" 
    
    
# O que a API retorna: ExperimentOut. O que a API retorna quando alguém busca ou cria um experimento
class ExperimentOut(BaseModel):
    id: int
    title: str
    description: str
    responsible_researcher: str
    status: str
    created_at: datetime   # <- mudou de created_time pra created_at


# Update parcial: todo campo é opcional (default None), pra permitir mandar só o que quer mudar
class ExperimentUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    responsible_researcher: Optional[str] = None
    status: Optional[str] = None


# ---------- Sample (Amostra) ----------

class SampleCreate(BaseModel):
    experiment_id: int
    code: str
    sample_type: str
    collected_at: datetime
    storage_location: str


class SampleOut(BaseModel):
    id: int
    experiment_id: int
    code: str
    sample_type: str
    collected_at: datetime
    storage_location: str
    created_at: datetime


class SampleUpdate(BaseModel):
    code: Optional[str] = None
    sample_type: Optional[str] = None
    collected_at: Optional[datetime] = None
    storage_location: Optional[str] = None


# ---------- Reagent (Reagente) ----------

class ReagentCreate(BaseModel):
    name: str
    manufacturer: str
    lot_number: str
    expiration_date: datetime
    quantity_available: float
    unit: str


class ReagentOut(BaseModel):
    id: int
    name: str
    manufacturer: str
    lot_number: str
    expiration_date: datetime
    quantity_available: float
    unit: str
    created_at: datetime


class ReagentUpdate(BaseModel):
    name: Optional[str] = None
    manufacturer: Optional[str] = None
    lot_number: Optional[str] = None
    expiration_date: Optional[datetime] = None
    quantity_available: Optional[float] = None
    unit: Optional[str] = None