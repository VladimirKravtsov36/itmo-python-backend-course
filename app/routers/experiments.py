from fastapi import APIRouter, HTTPException, Path
from typing import Annotated

from schemas.experiment import Experiment
from app.fake_db import FAKE_EXPERIMENTS_DB
from db.crud import ExperimentsManager

router = APIRouter()


@router.get("/ping")
def ping():
    return "pong"


@router.get("/experiments")
def show_experiments():
    """
    Return all available experiments
    """
    exp_manager = ExperimentsManager()
    db_results = exp_manager.read_experiments()

    experiments = [Experiment(**result) for result in db_results]

    return experiments


@router.get("/experiments/{experiment_id}")
def get_experiment(experiment_id: Annotated[int, Path(ge=0)]):
    """
    Get experiment by id
    """
    exp_manager = ExperimentsManager()
    db_result = exp_manager.get_experiment_by_id(experiment_id)

    if db_result is None:
        raise HTTPException(status_code=404, detail="Experiment not found")

    experiment = Experiment(**db_result)

    return experiment


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
    exp_manager = ExperimentsManager()
    exp_id = exp_manager.create_experiment(experiment)
    return exp_id
