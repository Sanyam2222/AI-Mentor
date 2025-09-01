import os
import requests
from .base import AIEngine

class HFEngine(AIEngine):
    def __init__(self):
        self.api_key = os.getenv("HF_API_KEY")
        self.model = "bigscience/bloom"

    def ask(self, question: str) -> str:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {"inputs": question}
        response = requests.post(
            f"https://api-inference.huggingface.co/models/{self.model}",
            headers=headers,
            json=payload,
        )
        return response.json()[0]["generated_text"]
