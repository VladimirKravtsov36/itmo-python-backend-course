from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_metric_average():
    """
    Test the metric_average endpoint with a valid dataset and metric_name.
    Asserts that the response status code is 200 and the JSON content is {"average": 0.7625}.
    """
    response = client.post(
        "/metric_average/",
        json={"dataset": "ImageNet", "metric_name": "Accuracy"},
    )

    assert response.status_code == 200
    assert response.json() == {"average": 0.7625}


def test_metric_average_error():
    """
    Test the metric_average endpoint with an invalid dataset and metric_name.
    Asserts that the response status code is 404.
    """
    response = client.post(
        "/metric_average/",
        json={"dataset": "NonExistentData", "metric_name": "NonExistentMetric"},
    )

    assert response.status_code == 404


def test_best_model():
    """
    Test the best_model endpoint with valid task, dataset, and metric_name.
    Asserts that the response status code is 200 and the JSON content is {"metric": 0.88, "model": "ViT"}.
    """
    response = client.post(
        "/best_model/",
        json={"task": "Image Classification", "dataset": "ImageNet", "metric_name": "Accuracy"},
    )

    assert response.status_code == 200
    assert response.json() == {"metric": 0.88, "model": "ViT"}


def test_best_model_error():
    """
    Test the best_model endpoint with invalid task, dataset, and metric_name.
    Asserts that the response status code is 404.
    """
    response = client.post(
        "/best_model/",
        json={"task": "NonExistentTask", "dataset": "NonExistentData", "metric_name": "NonExistentMetric"},
    )

    assert response.status_code == 404