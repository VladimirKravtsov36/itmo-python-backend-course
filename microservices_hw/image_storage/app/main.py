import os.path as osp

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

app = FastAPI()

IMG_PATH = "/code/images/"


@app.get("/ping")
def ping():
    return "pong"


@app.post("/images")
def get_image(image_id: str):
    """
    Retrieves an image file based on the provided image ID.

    Args:
        image_id (str): The ID of the image to retrieve.

    Returns:
        FileResponse: The image file as a response.

    Raises:
        HTTPException: If the image file is not found (status code 404).
    """
    path = osp.join(IMG_PATH, f"{image_id}.jpg")
    if osp.isfile(path):
        return FileResponse(path)

    raise HTTPException(status_code=404, detail="Image not found")
