from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_success_processing():
    """
    Test case to check the success processing of an image.

    Sends a POST request to the "/process_image/" endpoint with a valid image ID of 2.
    Expects a response with a status code of 200, indicating successful processing.
    """
    response = client.post(
        "/process_image/",
        params={"image_id": 2},
    )

    assert response.status_code == 200


def test_unexisting_image():
    """
    Test case to check the handling of an unexisting image.

    Sends a POST request to the "/process_image/" endpoint with an unexisting image ID of -999.
    Expects a response with a status code of 404, indicating that the requested image does not exist.
    """
    response = client.post(
        "/process_image/",
        params={"image_id": -999},
    )

    assert response.status_code == 404