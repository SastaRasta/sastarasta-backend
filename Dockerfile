FROM python:3.11-bookworm

RUN mkdir /app
WORKDIR /app

RUN mkdir /app/src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src/ ./src/
CMD ["python", "src/main.py"]

EXPOSE 5000