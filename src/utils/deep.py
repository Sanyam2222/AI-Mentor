from openai import AsyncOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_API_KEY")

client = AsyncOpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN,
)

async def ask_deepseek(question: str) -> str:
    try:
        response = await client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1:fireworks-ai",
            messages=[{"role": "user", "content": question}],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[DeepSeek API Error] {str(e)}"
