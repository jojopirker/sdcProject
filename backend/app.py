from fastapi import FastAPI
from typing import Optional

#
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/{item_id}")
def ask_model(item_id:int):
    return {"test"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
