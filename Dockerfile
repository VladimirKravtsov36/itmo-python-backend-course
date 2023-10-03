FROM python:3.9-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

RUN apt update && apt install make

COPY ./Makefile /code/Makefile

ENV PYTHONPATH "${PYTHONPATH}:/code/app"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]