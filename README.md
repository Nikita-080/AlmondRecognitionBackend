# AlmondRecognitionBackend

## ручной запуск

### подготовка

```
git clone https://github.com/Nikita-080/AlmondRecognitionBackend.git
cd AlmondRecognitionBackend
python -m venv venv
```

необходимо прописать путь к модели в конфиге

модель можно взять по адресу https://github.com/VladMexon/Almond в каталоге /runs/detect/train3/weights/best.pt

### включение

```
venv\\Scripts\\activate
fastapi dev --host 0.0.0.0 app/main.py
```

### выключение

```
ctrl + c
deactivate
```

### примечания

* сервер стартует на http://127.0.0.1:8000

* страница с апи http://127.0.0.1:8000/docs

### возможные проблемы

* ошибка с DLL библиотекой PyTorch, решается установкой другой версии

```
pip install torch==2.8.0 torchvision==0.23.0 torchaudio==2.8.0
```

## запуск через Docker

### подготовка

скачать и запустить докер

```
git clone https://github.com/Nikita-080/AlmondRecognitionBackend.git
cd AlmondRecognitionBackend
docker build -t arb1 .
```

### включение

```
docker run -p 4000:8000 arb1
```

### выключение

```
ctrl + c
docker stop arb1
```

### примечания

* сервер стартует на http://127.0.0.1:4000

* страница с апи http://127.0.0.1:4000/docs