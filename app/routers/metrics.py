from fastapi import APIRouter, HTTPException

from db.crud import MetricManager
from service.metric_calculator import MetricCalculator
from schemas.experiment import Experiment, MetricComputingParams

router = APIRouter()


@router.post("/metric_average")
def metric_average(metric_params: MetricComputingParams):
    """
    Calculate the average value of a metric for a given dataset.

    Args:
        dataset (str): The name of the dataset.
        metric_name (str): The name of the metric.

    Returns:
        float: The average value of the metric.
    """
    metric_manager = MetricManager()
    db_results = metric_manager.get_metric_for_dataset(
        metric_params.dataset, metric_params.metric_name
    )

    if not db_results:
        raise HTTPException(status_code=404, detail="Experiments not found")

    experiments = [Experiment(**result) for result in db_results]
    metric_calculator = MetricCalculator(experiments)
    average = metric_calculator.compute_average(
        metric_params.dataset, metric_params.metric_name
    )

    return {"average": average}


@router.post("/metric_std")
def metric_std(metric_params: MetricComputingParams):
    """
    Calculate the standard deviation of a metric for a given dataset.

    Args:
        dataset (str): The name of the dataset.
        metric_name (str): The name of the metric.

    Returns:
        float: The standard deviation of the metric.
    """
    metric_manager = MetricManager()
    db_results = metric_manager.get_metric_for_dataset(
        metric_params.dataset, metric_params.metric_name
    )

    if not db_results:
        raise HTTPException(status_code=404, detail="Experiments not found")

    experiments = [Experiment(**result) for result in db_results]
    metric_calculator = MetricCalculator(experiments)
    std = metric_calculator.compute_std(
        metric_params.dataset, metric_params.metric_name
    )

    return {"std": std}


@router.post("/best_model")
def best_model(metric_params: MetricComputingParams):
    """
    Get the best model based on a task, dataset, and metric.

    Args:
        task (str): The task.
        dataset (str): The name of the dataset.
        metric_name (str): The name of the metric.

    Returns:
        dict: The best model name and metric value.
    """
    metric_manager = MetricManager()
    db_results = metric_manager.get_models_for_task(
        metric_params.task, metric_params.dataset, metric_params.metric_name
    )

    if not db_results:
        raise HTTPException(status_code=404, detail="Experiments not found")

    experiments = [Experiment(**result) for result in db_results]
    metric_calculator = MetricCalculator(experiments)
    best_results = metric_calculator.find_best_model_for_task(
        metric_params.task, metric_params.dataset, metric_params.metric_name
    )

    return best_results
