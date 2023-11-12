# Use an official Python runtime as a parent image
FROM python:3.8-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV NAME image_frame_extractor

CMD ["python","app.py"]