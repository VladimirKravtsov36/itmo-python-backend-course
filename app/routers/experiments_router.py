from fastapi import APIRouter, HTTPException, Path
from typing import Annotated

from schemas.experiment import Experiment
from app.fake_db import FAKE_EXPERIMENTS_DB

router = APIRouter()


@router.get("/ping")
def ping():
    return "pong"


@router.get("/experiments")
def show_experiments():
    """
    Return all available experiments
    """
    return FAKE_EXPERIMENTS_DB


@router.get("/experiments/{experiment_id}")
def get_experiment(experiment_id: Annotated[int, Path(ge=0)]):
    """
    Get experiment by id
    """
    try:
        return FAKE_EXPERIMENTS_DB[experiment_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Experiment not found!")


@router.post("/experiments")
def add_experiment(experiment: Experiment):
    """
    Create a new experiment with all the information:

    - **model_name**: which model was trained
    - **task**: e.g. Detection, Segmentation, Classification etc.
    - **dataset**: on what data model was trained
    - **metric_name**: how do we measure model perfomance
    - **metric_value**: how model performed
    """
    FAKE_EXPERIMENTS_DB.append(experiment)

    return "Experiments was succesfully updated!"
