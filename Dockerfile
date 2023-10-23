FROM python:3.10.8
#FROM python:3.10.8-slim-buster

# タイムゾーン
#RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
RUN apt update
RUN apt install -y libopencv-dev

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install flask==2.3.2
RUN pip install opencv-python

ENV PORT 8000

WORKDIR /app

COPY ./app /app

CMD ["python", "app.py"]
