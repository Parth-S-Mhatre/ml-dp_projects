from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import numpy as np

# ✅ Load model and scaler
model = joblib.load("random_forest_model.pkl")
scaler = joblib.load("scaler.pkl")

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input data model
class WaterSample(BaseModel):
    ph: float = Field(..., ge=0, le=14)
    Hardness: float = Field(..., ge=0, le=500)
    Solids: float = Field(..., ge=0, le=50000)
    Chloramines: float = Field(..., ge=0, le=10)
    Sulfate: float = Field(..., ge=0, le=1000)
    Conductivity: float = Field(..., ge=0, le=1000)
    Organic_carbon: float = Field(..., ge=0, le=30)
    Trihalomethanes: float = Field(..., ge=0, le=200)
    Turbidity: float = Field(..., ge=0, le=10)

@app.post("/predict")
def predict(sample: WaterSample):
    # Rule-based override for unsafe pH
    if sample.ph < 6.5 or sample.ph > 8.5:
        return {"potability": 0, "reason": "pH out of potable range"}
    
    data = np.array([[sample.ph, sample.Hardness, sample.Solids, sample.Chloramines,
                      sample.Sulfate, sample.Conductivity, sample.Organic_carbon,
                      sample.Trihalomethanes, sample.Turbidity]])
    
    data_scaled = scaler.transform(data)
    pred = model.predict(data_scaled)

    return {"potability": int(pred[0])}
