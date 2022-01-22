from datetime import datetime
from fastapi import FastAPI
from typing import Optional
import joblib
import pandas as pd
from pydantic import BaseModel

#
app = FastAPI()
knn_model = None
ohenc = None

input_format_df = None

class Item(BaseModel):
    first_road_class: str
    weather_conditions: str
    road_surface_conditions: str
    urban_or_rural_area: str
    vehicle_type: str
    longitude: float
    latitude: float
    picked_date: datetime
    
@app.on_event("startup")
async def startup_event():
    knn_model = joblib.load('./model/finalized_model.pkl')
    ohenc = joblib.load('./model/encoder.pkl')

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items")
def ask_model(item: Item):
    #result = knn_model.predict() 
    return {"accident_severty":"result"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
