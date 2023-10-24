import os.path as osp
from urllib.parse import urljoin

import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response

app = FastAPI()

STORAGE_URL = "http://storage:80/images"


@app.get("/ping")
def ping():
    return "pong"


@app.post("/images")
def download_image(image_id: str):
    """
    Downloads an image from a storage server.

    Args:
        image_id (str): The ID of the image to be downloaded.

    Returns:
        Response: The downloaded image content with the media type set to "image/png".

    Raises:
        HTTPException: If the image is not found (status code 404).
    """
    response = requests.post(
        STORAGE_URL,
        params={"image_id": image_id},
        headers={"content-type": "application/json"},
    )
    if response.status_code == 200:
        return Response(content=response.content, media_type="image/png")
    raise HTTPException(status_code=404, detail="Image not found")
