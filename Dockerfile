FROM python:3.11-slim

WORKDIR ~/AlmondRecognitionBackend
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["fastapi", "dev", "--host", "0.0.0.0", "app/main.py"]