import requests
from .base import AIEngine

class OllamaEngine(AIEngine):
    def __init__(self, url="http://localhost:11434"):
        self.url = url

    def ask(self, question: str) -> str:
        payload = {"model": "llama2", "prompt": question}
        res = requests.post(f"{self.url}/api/generate", json=payload, stream=False)
        return res.json().get("response", "No reply")
