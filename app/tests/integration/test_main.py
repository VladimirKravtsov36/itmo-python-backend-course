from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_metric_average():
    response = client.post(
        "/metric_average/",
        json={"dataset": "ImageNet", "metric_name": "Accuracy"},
    )

    assert response.status_code == 200
    assert response.json() == {"average": 0.7625}


def test_metric_average_error():
    response = client.post(
        "/metric_average/",
        json={"dataset": "NonExistentData", "metric_name": "NonExistentMetric"},
    )

    assert response.status_code == 404


def test_best_model():
    response = client.post(
        "/best_model/",
        json={
            "task": "Image Classification",
            "dataset": "ImageNet",
            "metric_name": "Accuracy",
        },
    )

    assert response.status_code == 200
    assert response.json() == {"metric": 0.88, "model": "ViT"}


def test_best_model_error():
    response = client.post(
        "/best_model/",
        json={
            "task": "NonExistentTask",
            "dataset": "NonExistentData",
            "metric_name": "NonExistentMetric",
        },
    )

    assert response.status_code == 404
