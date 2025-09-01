from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.utils.model_loader import load_model
from src.services.ai_service import ask_deepseek

app = FastAPI(title="AI Mentor")

# ===== CORS =====
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for development; replace with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Decision Tree model once
decision_tree_model = load_model("src/model/career_model.pkl")

class UserInput(BaseModel):
    answers: list[int]   # quiz answers (encoded as integers)

@app.post("/predict")
async def predict_career(user_input: UserInput):
    try:
        prediction = decision_tree_model.predict([user_input.answers])
        return {"career_field": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class ExplainRequest(BaseModel):
    career_field: str

@app.post("/explain")
async def explain_career(req: ExplainRequest):
    try:
        prompt = f"Explain why {req.career_field} might be a good career choice for a student."
        explanation = await ask_deepseek(prompt)
        return {"career_field": req.career_field, "explanation": explanation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
