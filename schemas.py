from pydantic import BaseModel
from datetime import datetime

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