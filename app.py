from fastapi import FastAPI
from pydantic import BaseModel, Field, ConfigDict
import joblib
import numpy as np
import os

# Load trained model
# Try multiple possible paths
possible_paths = [
    os.path.join(os.path.dirname(__file__), "model", "model.pkl"),  # Docker path
    os.path.join("model", "model.pkl"),  # Docker path
    os.path.join(os.path.dirname(__file__), "lab2", "outputs", "model.pkl"),  # Local dev path
    os.path.join("lab2", "outputs", "model.pkl"),  # Local dev path
    "lab2/outputs/model.pkl",  # Local dev path
]

model_path = None
for path in possible_paths:
    if os.path.exists(path):
        model_path = path
        break

if model_path is None:
    raise FileNotFoundError(f"Model file not found. Tried: {possible_paths}")

with open(model_path, "rb") as f:
    model = joblib.load(f)

app = FastAPI(title="Wine Quality Prediction API")

# Input schema
class WineInput(BaseModel):
    fixed_acidity: float = Field(example=7.4, description="Fixed acidity in g(tartaric acid)/dm³")
    volatile_acidity: float = Field(example=0.7, description="Volatile acidity in g(acetic acid)/dm³")
    citric_acid: float = Field(example=0.0, description="Citric acid in g/dm³")
    residual_sugar: float = Field(example=1.9, description="Residual sugar in g/dm³")
    chlorides: float = Field(example=0.076, description="Chlorides in g(sodium chloride)/dm³")
    free_sulfur_dioxide: float = Field(example=11.0, description="Free sulfur dioxide in mg/dm³")
    total_sulfur_dioxide: float = Field(example=34.0, description="Total sulfur dioxide in mg/dm³")
    density: float = Field(example=0.9978, description="Density in g/cm³")
    pH: float = Field(example=3.51, description="pH value")
    sulphates: float = Field(example=0.56, description="Sulphates in g(potassium sulphate)/dm³")
    alcohol: float = Field(example=9.4, description="Alcohol content in % vol")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "fixed_acidity": 7.4,
                "volatile_acidity": 0.7,
                "citric_acid": 0.0,
                "residual_sugar": 1.9,
                "chlorides": 0.076,
                "free_sulfur_dioxide": 11,
                "total_sulfur_dioxide": 34,
                "density": 0.9978,
                "pH": 3.51,
                "sulphates": 0.56,
                "alcohol": 9.4
            }
        }
    )

@app.post("/predict", summary="Predict Quality", description="Predict wine quality based on chemical properties")
def predict_quality(data: WineInput):
    features = np.array([[
        data.fixed_acidity,
        data.volatile_acidity,
        data.citric_acid,
        data.residual_sugar,
        data.chlorides,
        data.free_sulfur_dioxide,
        data.total_sulfur_dioxide,
        data.density,
        data.pH,
        data.sulphates,
        data.alcohol
    ]])
    prediction = model.predict(features)[0]
    return {
        "predicted_quality": round(float(prediction), 2)
    }
