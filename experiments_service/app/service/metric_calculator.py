from typing import List

from schemas.experiment import Experiment


class MetricCalculator:
    def __init__(self, experiments: List[Experiment]):
        self.experiments = experiments

    def compute_average(self, dataset: str, metric_name: str) -> float:
        """
        Calculate the average value of a specific metric for a given dataset.

        Args:
            dataset (str): The name of the dataset for which the average is calculated.
            metric_name (str): The name of the metric for which the average is calculated.

        Returns:
            float: The average value of the specified metric for the given dataset.
        """

        metric_values = [
            exp.metric_value
            for exp in self.experiments
            if exp.dataset == dataset and exp.metric_name == metric_name
        ]

        if metric_values:
            return sum(metric_values) / len(metric_values)

    def compute_std(self, dataset: str, metric_name: str) -> float:
        """
        Calculate the standard deviation of a given metric for a specific dataset.

        Args:
            dataset (str): The name of the dataset for which the standard deviation is calculated.
            metric_name (str): The name of the metric for which the standard deviation is calculated.

        Returns:
            float: The standard deviation of the metric for the given dataset.
        """

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
        """
        Find the best model for a given task, dataset, and metric name based on the metric values of the experiments.

        Args:
            task (str): The task for which the best model needs to be found.
            dataset (str): The dataset for which the best model needs to be found.
            metric_name (str): The name of the metric based on which the best model needs to be found.

        Returns:
            str: The name of the best model for the given task, dataset, and metric name.
        """

        models_metrics = [
            (exp.model_name, exp.metric_value)
            for exp in self.experiments
            if exp.task == task
            and exp.dataset == dataset
            and exp.metric_name == metric_name
        ]

        if models_metrics:
            best_result = max(models_metrics, key=lambda x: x[1])
            return {"model": best_result[0], "metric": best_result[1]}
