import os.path as osp
from urllib.parse import urljoin

import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response

app = FastAPI()

DOWNLOAD_URL = "http://downloader:81/images"
DETECTOR_URL = "http://detector:83/detect"


@app.get("/ping")
def ping():
    return "pong"


@app.post("/process_image")
def process_image(image_id: int):
    """
    Process the image corresponding to the given image_id.

    Args:
        image_id (int): The ID of the image to be processed.

    Returns:
        Response: The processed image content in PNG format.

    Raises:
        HTTPException: If the image is not found.

    Example Usage:

        # Make a POST request to the /process_image endpoint with an image_id
        response = requests.post("http://localhost:8000/process_image", json={"image_id": 123})

        # Print the response content
        print(response.content)
    """
    response = requests.post(
        DOWNLOAD_URL,
        params={"image_id": image_id},
        headers={"content-type": "application/json"},
    )
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Image not found")
    
    files = {"file": response.content}
    response = requests.post(DETECTOR_URL, files=files)

    return Response(content=response.content, media_type="image/png")
