from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import joblib
import pandas as pd

# ===============================
# LOAD ML MODEL (FIXED)
# ===============================
# Use joblib instead of pickle (MANDATORY for sklearn pipelines)
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.joblib")

model = joblib.load(MODEL_PATH)


app = FastAPI(title="Insurance Premium Prediction API")

# ===============================
# CITY TIERS
# ===============================
tier_1_cities = [
    "Mumbai", "Delhi", "Bangalore", "Chennai",
    "Kolkata", "Hyderabad", "Pune"
]

tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi",
    "Visakhapatnam", "Coimbatore", "Bhopal", "Nagpur", "Vadodara",
    "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati",
    "Thiruvananthapuram", "Ludhiana", "Nashik", "Allahabad",
    "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem",
    "Vijayawada", "Tiruchirappalli", "Bhavnagar", "Gwalior",
    "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode",
    "Warangal", "Kolhapur", "Bilaspur", "Jalandhar", "Noida",
    "Guntur", "Asansol", "Siliguri"
]

# ===============================
# INPUT SCHEMA
# ===============================
class UserInput(BaseModel):

    age: Annotated[int, Field(gt=0, lt=120)]
    weight: Annotated[float, Field(gt=0)]
    height: Annotated[float, Field(gt=0, lt=2.5)]
    income_lpa: Annotated[float, Field(gt=0)]
    smoker: bool
    city: str
    occupation: Literal[
        "retired",
        "freelancer",
        "student",
        "government_job",
        "business_owner",
        "unemployed",
        "private_job"
    ]

    # -------------------------------
    # COMPUTED FEATURES
    # -------------------------------
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        return "low"

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        return 3


# ===============================
# PREDICTION ENDPOINT
# ===============================
@app.post("/predict")
def predict_premium(data: UserInput):

    input_df = pd.DataFrame([{
        "bmi": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation
    }])

    prediction = model.predict(input_df)[0]

    return JSONResponse(
        status_code=200,
        content={"predicted_category": prediction}
    )
