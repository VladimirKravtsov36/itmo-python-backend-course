from pydantic import BaseModel


class Experiment(BaseModel):
    model_name: str
    task: str
    dataset: str
    metric_name: str
    metric_value: float
