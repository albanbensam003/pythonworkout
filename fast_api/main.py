from typing import Union
import logging
from fastapi import FastAPI
from collections import Counter

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
