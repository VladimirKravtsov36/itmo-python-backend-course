import cv2
import numpy as np
from fastapi import FastAPI, UploadFile
from fastapi.responses import Response
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

app = FastAPI()


@app.get("/ping")
def ping():
    return "pong"


@app.post("/detect")
async def detect(file: UploadFile):
    """
    Perform object detection on an uploaded image file.

    Args:
        file (UploadFile): The uploaded image file.

    Returns:
        Response: A response containing the encoded image as a byte string.
    """
    image_bytes = await file.read()
    image_np = np.frombuffer(image_bytes, np.uint8)
    image_cv2 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

    detection_result = model.predict(image_cv2)
    detection_result_np = detection_result[0].plot()

    success, encoded_image = cv2.imencode(".jpg", detection_result_np)

    return Response(content=encoded_image.tobytes(), media_type="image/png")
