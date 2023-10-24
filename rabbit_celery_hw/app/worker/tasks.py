import io
import os

from PIL import Image

from celery import Celery


broker_url = os.environ.get("CELERY_BROKER_URL", "pyamqp://guest@rabbitmq:5672//")
backend_url = os.environ.get("CELERY_BACKEND_URL", "redis://redis:6379")

celery = Celery(__name__, backend="redis://redis:6379", broker=broker_url) 


@celery.task(name="image_to_gray")
def image_to_gray(image_id: int) -> bytes:
    """
    Convert a color image to grayscale and return the grayscale image as bytes.

    Args:
        image_id (int): The ID of the image to be converted to grayscale.

    Returns:
        bytes: Grayscale image as bytes.
    """
    image = Image.open(f"/storage/{image_id}.jpg")
    image_grayscale = image.convert("L")
    buf = io.BytesIO()
    image_grayscale.save(buf, format="JPEG")

    return buf.getvalue()