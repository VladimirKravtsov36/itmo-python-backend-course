import pytest

from service.metric_calculator import MetricCalculator
from schemas.experiment import Experiment


test_experiments = [
    Experiment(
        model_name="ResNet",
        task="Image Classification",
        dataset="ImageNet",
        metric_name="Accuracy",
        metric_value=0.75,
    ),
    Experiment(
        model_name="YOLOv8",
        task="Object Detection",
        dataset="MS COCO",
        metric_name="mAP",
        metric_value=0.65,
    ),
    Experiment(
        model_name="ViT",
        task="Image Classification",
        dataset="ImageNet",
        metric_name="Accuracy",
        metric_value=0.88,
    ),
    Experiment(
        model_name="YOLOv7",
        task="Object Detection",
        dataset="MS COCO",
        metric_name="mAP",
        metric_value=0.55,
    ),
    Experiment(
        model_name="VGG16",
        task="Image Classification",
        dataset="ImageNet",
        metric_name="Accuracy",
        metric_value=0.6,
    ),
    Experiment(
        model_name="SWIN",
        task="Image Classification",
        dataset="ImageNet",
        metric_name="Accuracy",
        metric_value=0.82,
    ),
]


"""
This code snippet contains test functions that use the `pytest.mark.parametrize` decorator to run multiple test cases with different input values. The functions test the functionality of the `MetricCalculator` class by calling its methods and asserting the expected results.

Example Usage:
    test_average_metric("ImageNet", "Accuracy", 0.7625)
    test_std_metric("MS COCO", "mAP", 0.05)
    test_best_model("Image Classification", "ImageNet", "Accuracy", {"metric": 0.88, "model": "ViT"})

Inputs:
    dataset (str): The name of the dataset.
    metric_name (str): The name of the metric.
    expected_result (float or dict or None): The expected result of the metric calculation.

Outputs:
    None. The test functions do not return any value. The output is the result of the assertions, which will be displayed as test pass or failure.
"""

@pytest.mark.parametrize(
    "dataset, metric_name, expected_result",
    [
        ("ImageNet", "Accuracy", 0.7625),
        ("MS COCO", "mAP", 0.6),
        ("NonExistentDataset", "NoneExistentMetric", None),
    ],
)
def test_average_metric(dataset, metric_name, expected_result):
    """
    Test the `compute_average` method of the `MetricCalculator` class.

    Args:
        dataset (str): The name of the dataset.
        metric_name (str): The name of the metric.
        expected_result (float or None): The expected result of the metric calculation.

    Returns:
        None. The output is the result of the assertion.
    """
    metric_calculator = MetricCalculator(experiments=test_experiments)
    average_metric = metric_calculator.compute_average(dataset, metric_name)

    assert average_metric == pytest.approx(expected_result, rel=1e-6)


@pytest.mark.parametrize(
    "dataset, metric_name, expected_result",
    [
        ("ImageNet", "Accuracy", 0.1045),
        ("MS COCO", "mAP", 0.05),
        ("NonExistentDataset", "NoneExistentMetric", None),
    ],
)
def test_std_metric(dataset, metric_name, expected_result):
    """
    Test the `compute_std` method of the `MetricCalculator` class.

    Args:
        dataset (str): The name of the dataset.
        metric_name (str): The name of the metric.
        expected_result (float or None): The expected result of the metric calculation.

    Returns:
        None. The output is the result of the assertion.
    """
    metric_calculator = MetricCalculator(experiments=test_experiments)
    std_metric = metric_calculator.compute_std(dataset, metric_name)

    assert std_metric == pytest.approx(expected_result, rel=1e-4)


@pytest.mark.parametrize(
    "task, dataset, metric_name, expected_result",
    [
        (
            "Image Classification",
            "ImageNet",
            "Accuracy",
            {"metric": 0.88, "model": "ViT"},
        ),
        ("Object Detection", "MS COCO", "mAP", {"metric": 0.65, "model": "YOLOv8"}),
        ("NonExistentTask", "NonExistentDataset", "NoneExistentMetric", None),
    ],
)
def test_best_model(dataset, task, metric_name, expected_result):
    """
    Test the `find_best_model_for_task` method of the `MetricCalculator` class.

    Args:
        dataset (str): The name of the dataset.
        task (str): The name of the task.
        metric_name (str): The name of the metric.
        expected_result (dict or None): The expected result of the best model search.

    Returns:
        None. The output is the result of the assertion.
    """
    metric_calculator = MetricCalculator(experiments=test_experiments)
    best_result = metric_calculator.find_best_model_for_task(task, dataset, metric_name)

    assert best_result == expected_result
