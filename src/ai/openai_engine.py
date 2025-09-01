import os
from openai import OpenAI
from .base import AIEngine

class OpenAIEngine(AIEngine):
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def ask(self, question: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": question}]
        )
        return response.choices[0].message.content
