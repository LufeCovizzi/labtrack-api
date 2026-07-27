from fastapi import FastAPI, Depends
from database import Base, engine, get_db
from models import Experiment
from sqlalchemy.orm import Session
from schemas import ExperimentCreate, ExperimentOut


app = FastAPI()
Base.metadata.create_all(engine)

@app.get ("/")
def raiz():
    return {"mensagem" : "LabTrack Api no ar"}

@app.post("/experiments", response_model = ExperimentOut)
def create_experiment(experiment: ExperimentCreate, db: Session = Depends(get_db)):
    novo_experimento = Experiment(
       title = experiment.title,
       description = experiment.description,
       responsible_researcher = experiment.responsible_researcher,
       status = experiment.status 
    )

    db.add(novo_experimento)
    db.commit()
    db.refresh(novo_experimento)
    return novo_experimento


@app.get("/experiments", response_model=list[ExperimentOut])
def list_experiments(db: Session = Depends (get_db)):
    experimentos = db.query(Experiment).all()
    return experimentos