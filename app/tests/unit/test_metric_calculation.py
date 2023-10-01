import pytest

from service.metric_calculator import MetricCalculator
from schemas.experiment import Experiment

# TODO: move to test_db.py
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


@pytest.mark.parametrize(
    "dataset, metric_name, expected_result",
    [
        ("ImageNet", "Accuracy", 0.7625),
        ("MS COCO", "mAP", 0.6),
        ("NonExistentDataset", "NoneExistentMetric", None),
    ],
)
def test_average_metric(dataset, metric_name, expected_result):
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
    metric_calculator = MetricCalculator(experiments=test_experiments)
    std_metric = metric_calculator.compute_std(dataset, metric_name)

    assert std_metric == pytest.approx(expected_result, rel=1e-4)


@pytest.mark.parametrize(
    "task, dataset, metric_name, expected_result",
    [
        ("Image Classification", "ImageNet", "Accuracy", "ViT"),
        ("Object Detection", "MS COCO", "mAP", "YOLOv8"),
        ("NonExistentTask", "NonExistentDataset", "NoneExistentMetric", None),
    ],
)
def test_best_model(dataset, task, metric_name, expected_result):
    metric_calculator = MetricCalculator(experiments=test_experiments)
    best_model = metric_calculator.find_best_model_for_task(task, dataset, metric_name)

    assert best_model == expected_result
