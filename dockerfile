FROM python:3.12.2-slim

WORKDIR C:\Users\SATHEESHWARAN\Desktop\DSML_FLASK_1\DOCKER

RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python","-m","flask","--app","predictions.py","run","--host=0.0.0.0"]
