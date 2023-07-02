from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

model_path = 'model/'
MODEL = SentenceTransformer(model_path)
app = FastAPI()

class EmbeddingTarget(BaseModel):
    sentence: str

@app.get("/")
def read_root():
    return {"health": "ok"}


@app.post("/embed")
def embed(target: EmbeddingTarget):
    embeddings = MODEL.encode([target.sentence])
    return {"embeddings": embeddings[0].tolist()}

