# src/api/routes.py

from fastapi import APIRouter
from pydantic import BaseModel
from model.career_predictor import predict_career

router = APIRouter()

# Define the request schema
class CareerRequest(BaseModel):
    answers: list[int]  # user answers as list of integers

# Define the response schema
class CareerResponse(BaseModel):
    career: str

@router.post("/predict", response_model=CareerResponse)
async def predict(request: CareerRequest):
    career = predict_career(request.answers)
    return {"career": career}
