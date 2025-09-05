from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from pathlib import Path
from services.ai_service import ask_deepseek

app = FastAPI(title="AI Mentor")

# ===== CORS =====
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace with your frontend in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the career tree once
TREE_PATH = Path("career_tree.json")
with open(TREE_PATH, "r", encoding="utf-8") as f:
    career_tree = json.load(f)

# ===== Models =====
class PathRequest(BaseModel):
    path: list[str]  # path of selected options

class ExplainRequest(BaseModel):
    career_field: str

# ===== Endpoints =====
@app.get("/first-question")
def first_question():
    node = career_tree
    return {
        "question": node["question"],
        "options": [{"text": o["text"], "tooltip": o.get("tooltip", "")} for o in node["options"]]
    }

@app.post("/next-question")
def next_question(req: PathRequest):
    node = career_tree
    for choice in req.path:
        option = next((o for o in node["options"] if o["text"] == choice), None)
        if option is None:
            raise HTTPException(status_code=400, detail=f"Invalid choice: {choice}")
        node = option.get("next") or {"career": option.get("career"), "motivation": option.get("motivation")}

    if "question" in node:
        return {
            "question": node["question"],
            "options": [{"text": o["text"], "tooltip": o.get("tooltip", "")} for o in node["options"]]
        }
    else:
        return node  # leaf node: career + motivation

@app.post("/explain")
async def explain(req: ExplainRequest):
    try:
        prompt = f"Explain why {req.career_field} might be a good career choice for a student."
        explanation = await ask_deepseek(prompt)
        return {"career_field": req.career_field, "explanation": explanation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
