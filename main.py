from fastapi import FastAPI
from database import Base, engine
from models import Experiment

app = FastAPI()
Base.metadata.create_all(engine)

@app.get ("/")
def raiz():
    return {"mensagem" : "LabTrack Api no ar"}