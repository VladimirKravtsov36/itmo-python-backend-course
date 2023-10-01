from typing import List

from schemas.experiment import Experiment


class MetricCalculator:
    def __init__(self, experiments: List[Experiment]):
        self.experiments = experiments

    def compute_average(self, dataset: str, metric_name: str) -> float:
        metric_values = [
            exp.metric_value
            for exp in self.experiments
            if exp.dataset == dataset and exp.metric_name == metric_name
        ]

        if metric_values:
            return sum(metric_values) / len(metric_values)

    def compute_std(self, dataset: str, metric_name: str) -> float:
        metric_values = [
            exp.metric_value
            for exp in self.experiments
            if exp.dataset == dataset and exp.metric_name == metric_name
        ]

        if metric_values:
            mean = sum(metric_values) / len(metric_values)
            variance = sum([((x - mean) ** 2) for x in metric_values]) / len(
                metric_values
            )
            std = variance**0.5

            return std

    def find_best_model_for_task(
        self, task: str, dataset: str, metric_name: str
    ) -> str:
        models_metrics = [
            (exp.model_name, exp.metric_value)
            for exp in self.experiments
            if exp.task == task
            and exp.dataset == dataset
            and exp.metric_name == metric_name
        ]

        if models_metrics:
            return max(models_metrics, key=lambda x: x[1])[0]
