# server.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

model = joblib.load("regression.joblib")

app = FastAPI()

class HouseFeatures(BaseModel):
    size: int
    nb_rooms: int
    garden: bool

@app.get("/predict")
def predict_default():
    return {"y_pred": 2}

@app.post("/predict")
def predict(features: HouseFeatures):
    garden = 1 if features.garden else 0
    X_new = [[features.size, features.nb_rooms, garden]]
    y_pred = model.predict(X_new)[0]
    return {"y_pred": y_pred}
