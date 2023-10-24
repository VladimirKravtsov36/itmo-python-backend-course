FROM python:3.9-slim

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

ENV PYTHONPATH "${PYTHONPATH}:/code/:/code/app"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "83"]