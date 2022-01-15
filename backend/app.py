from fastapi import FastAPI
from typing import Optional
import joblib
import pandas as pd
from pydantic import BaseModel

#
app = FastAPI()
knn_model = None

input_format_df = None

class Item(BaseModel):
    day_of_week: str
    first_road_class: str
    weather_conditions: str
    road_surface_conditions: str
    special_conditions_at_site: str
    urban_or_rural_area: str
    longitude: float
    latitude: float
    daytime: str
    season: str
    vehicle_type: str

@app.on_event("startup")
async def startup_event():
    filename = './model/finalized_model.pkl'
    #knn_model = joblib.load(filename)

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
