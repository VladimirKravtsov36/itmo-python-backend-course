from pydantic import BaseModel
from typing import Optional


class Experiment(BaseModel):
    model_name: str
    task: str
    dataset: str
    metric_name: str
    metric_value: float


class MetricComputingParams(BaseModel):
    dataset: str
    metric_name: str
    task: Optional[str] = None
