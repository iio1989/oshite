FROM python:3.10.8
#FROM python:3.10.8-slim-buster

RUN pip install --upgrade pip

RUN pip install flask==2.2.2

ENV PORT 8000

WORKDIR /app

COPY ./app /app

CMD ["python", "app.py"]
