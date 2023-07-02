FROM python:3.11

WORKDIR /app

RUN pip install fastapi uvicorn[standard]
RUN pip install -U fugashi[unidic-lite] sentence-transformers

COPY ./app/ .
RUN python3 download_model.py

EXPOSE 8080
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
