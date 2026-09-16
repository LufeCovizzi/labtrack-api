from fastapi import FastAPI, Depends, HTTPException
from database import Base, engine, get_db
from models import Experiment, Sample, Reagent
from sqlalchemy.orm import Session
from schemas import (
    ExperimentCreate, ExperimentOut, ExperimentUpdate,
    SampleCreate, SampleOut, SampleUpdate,
    ReagentCreate, ReagentOut, ReagentUpdate,
)


app = FastAPI(
    title="LabTrack API",
    description="API para rastrear experimentos, amostras e reagentes de laboratório.",
    version="0.1.0",
)
Base.metadata.create_all(engine)

@app.get ("/")
def raiz():
    return {"mensagem" : "LabTrack Api no ar"}

@app.post("/experiments", response_model=ExperimentOut, tags=["Experiments"])
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


@app.get("/experiments", response_model=list[ExperimentOut], tags=["Experiments"])
def list_experiments(db: Session = Depends (get_db)):
    experimentos = db.query(Experiment).all()
    return experimentos

@app.get("/experiments/{experiment_id}", response_model=ExperimentOut, tags=["Experiments"])
def get_experiment(experiment_id: int, db: Session = Depends(get_db)):
    experimento = db.query(Experiment).filter(Experiment.id == experiment_id).first()

    if experimento is None:
        raise HTTPException(status_code=404, detail="Experimento não encontrado")

    return experimento


@app.put("/experiments/{experiment_id}", response_model=ExperimentOut, tags=["Experiments"])
def update_experiment(experiment_id: int, dados: ExperimentUpdate, db: Session = Depends(get_db)):
    experimento = db.query(Experiment).filter(Experiment.id == experiment_id).first()

    if experimento is None:
        raise HTTPException(status_code=404, detail="Experimento não encontrado")

    # model_dump(exclude_unset=True) devolve só os campos que vieram no JSON da requisição,
    # ignorando os que ficaram None por não terem sido enviados
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(experimento, campo, valor)

    db.commit()
    db.refresh(experimento)
    return experimento


@app.delete("/experiments/{experiment_id}", status_code=204, tags=["Experiments"])
def delete_experiment(experiment_id: int, db: Session = Depends(get_db)):
    experimento = db.query(Experiment).filter(Experiment.id == experiment_id).first()

    if experimento is None:
        raise HTTPException(status_code=404, detail="Experimento não encontrado")

    db.delete(experimento)
    db.commit()


# ---------- Sample (Amostra) ----------

@app.post("/samples", response_model=SampleOut, tags=["Samples"])
def create_sample(sample: SampleCreate, db: Session = Depends(get_db)):
    # confere que o experimento referenciado existe antes de criar a amostra —
    # o FK garante isso no banco, mas aqui devolvemos um 404 claro em vez de um erro genérico
    experimento = db.query(Experiment).filter(Experiment.id == sample.experiment_id).first()
    if experimento is None:
        raise HTTPException(status_code=404, detail="Experimento não encontrado")

    nova_amostra = Sample(
        experiment_id=sample.experiment_id,
        code=sample.code,
        sample_type=sample.sample_type,
        collected_at=sample.collected_at,
        storage_location=sample.storage_location,
    )
    db.add(nova_amostra)
    db.commit()
    db.refresh(nova_amostra)
    return nova_amostra


@app.get("/samples", response_model=list[SampleOut], tags=["Samples"])
def list_samples(db: Session = Depends(get_db)):
    return db.query(Sample).all()


@app.get("/samples/{sample_id}", response_model=SampleOut, tags=["Samples"])
def get_sample(sample_id: int, db: Session = Depends(get_db)):
    amostra = db.query(Sample).filter(Sample.id == sample_id).first()
    if amostra is None:
        raise HTTPException(status_code=404, detail="Amostra não encontrada")
    return amostra


@app.put("/samples/{sample_id}", response_model=SampleOut, tags=["Samples"])
def update_sample(sample_id: int, dados: SampleUpdate, db: Session = Depends(get_db)):
    amostra = db.query(Sample).filter(Sample.id == sample_id).first()
    if amostra is None:
        raise HTTPException(status_code=404, detail="Amostra não encontrada")

    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(amostra, campo, valor)

    db.commit()
    db.refresh(amostra)
    return amostra


@app.delete("/samples/{sample_id}", status_code=204, tags=["Samples"])
def delete_sample(sample_id: int, db: Session = Depends(get_db)):
    amostra = db.query(Sample).filter(Sample.id == sample_id).first()
    if amostra is None:
        raise HTTPException(status_code=404, detail="Amostra não encontrada")
    db.delete(amostra)
    db.commit()


# ---------- Reagent (Reagente) ----------

@app.post("/reagents", response_model=ReagentOut, tags=["Reagents"])
def create_reagent(reagent: ReagentCreate, db: Session = Depends(get_db)):
    novo_reagente = Reagent(
        name=reagent.name,
        manufacturer=reagent.manufacturer,
        lot_number=reagent.lot_number,
        expiration_date=reagent.expiration_date,
        quantity_available=reagent.quantity_available,
        unit=reagent.unit,
    )
    db.add(novo_reagente)
    db.commit()
    db.refresh(novo_reagente)
    return novo_reagente


@app.get("/reagents", response_model=list[ReagentOut], tags=["Reagents"])
def list_reagents(db: Session = Depends(get_db)):
    return db.query(Reagent).all()


@app.get("/reagents/{reagent_id}", response_model=ReagentOut, tags=["Reagents"])
def get_reagent(reagent_id: int, db: Session = Depends(get_db)):
    reagente = db.query(Reagent).filter(Reagent.id == reagent_id).first()
    if reagente is None:
        raise HTTPException(status_code=404, detail="Reagente não encontrado")
    return reagente


@app.put("/reagents/{reagent_id}", response_model=ReagentOut, tags=["Reagents"])
def update_reagent(reagent_id: int, dados: ReagentUpdate, db: Session = Depends(get_db)):
    reagente = db.query(Reagent).filter(Reagent.id == reagent_id).first()
    if reagente is None:
        raise HTTPException(status_code=404, detail="Reagente não encontrado")

    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(reagente, campo, valor)

    db.commit()
    db.refresh(reagente)
    return reagente


@app.delete("/reagents/{reagent_id}", status_code=204, tags=["Reagents"])
def delete_reagent(reagent_id: int, db: Session = Depends(get_db)):
    reagente = db.query(Reagent).filter(Reagent.id == reagent_id).first()
    if reagente is None:
        raise HTTPException(status_code=404, detail="Reagente não encontrado")
    db.delete(reagente)
    db.commit()