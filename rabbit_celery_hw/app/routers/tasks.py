from celery.result import AsyncResult
from fastapi import APIRouter, UploadFile
from fastapi.responses import Response
from worker import tasks

router = APIRouter()


@router.post("/convert_to_gray")
async def to_gray(image_id: int):
    """
    Convert an image to grayscale.

    Args:
        image_id (int): The ID of the image to be converted to grayscale.

    Returns:
        dict: A dictionary containing the task ID.

    Example:
        >>> response = client.post("/convert_to_gray", json={"image_id": 123})
    """
    task = tasks.image_to_gray.delay(image_id)

    return {"task_id": task.id}


@router.get("/tasks/{task_id}")
def get_status(task_id):
    """
    Get the status of a task.

    Args:
        task_id: The ID of the task.

    Returns:
        dict or Response: If the task is successful, returns a dictionary containing the task status. If the task is not successful, returns a Response object with the task status.

    Example:
        >>> response = client.get("/tasks/456")
    """
    task_result = AsyncResult(task_id, backend=tasks.celery.backend)
    if task_result.status == "SUCCESS":
        return Response(content=task_result.result, media_type="image/png")
    return {"status": task_result.status}
