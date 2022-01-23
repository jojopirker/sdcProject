from datetime import datetime
from fastapi import FastAPI
from typing import Optional
import joblib
import pandas as pd
import numpy as np
from pydantic import BaseModel
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import OneHotEncoder

description = """
UK Accidents ML Model API helps predict serverity of accidents in the UK. 
🚗🚗🚗🚗🚗🚗
"""


app = FastAPI(title="UK Accidents ML Model",
description=description,
version="1.0")
global knn_model 
global ohenc 

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

def getDayTime(hour):
    if hour >= 5 and hour < 11:
        return "morning (5-11)"
    elif hour >= 11 and hour < 14:
        return "midday (11-14)"
    elif hour >= 14 and hour < 18:
        return "afternoon (16-18)"
    elif hour >= 17 and hour < 23:
        return "evening (18-23)"
    else:
        return "night (23-5)"

def getSeasonText(number):
    if number==1:
        return "Spring"
    elif number==2:
        return "Summer"
    elif number==3:
        return "Autumn"
    elif number==4:
        return "Winter"
    
@app.on_event("startup")
async def startup_event():
    global knn_model 
    knn_model = joblib.load('./model/finalized_model.pkl')
    global ohenc 
    ohenc = joblib.load('./model/encoder.pkl')


@app.post("/predict")
def ask_model(item: Item):
    hour = item.picked_date.hour
    daytime = getDayTime(hour)
    season = getSeasonText(item.picked_date.month%12 // 3+1)
    day_of_week = item.picked_date.strftime("%A")

    cat_list = [[day_of_week, item.first_road_class, item.weather_conditions, item.road_surface_conditions, item.urban_or_rural_area,daytime, season, item.vehicle_type]]
    lat_long = [[item.longitude, item.latitude]]

    df_cat = pd.DataFrame(cat_list)
    df_met = pd.DataFrame(lat_long)

    prep_cat = ohenc.transform(df_cat).toarray()

    input_Final = np.concatenate([df_met, prep_cat], axis=1)

    result = knn_model.predict(input_Final) 
    return {"accident_severty":result[0]}

