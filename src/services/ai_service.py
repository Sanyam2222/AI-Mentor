import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()  # Load env vars from .env file

HF_TOKEN = os.getenv("HF_API_KEY")
if not HF_TOKEN:
    raise ValueError("HF_TOKEN environment variable is not set")

# Create async OpenAI client pointing to Hugging Face router API
client = AsyncOpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN,
)

async def ask_deepseek(question: str) -> str:
    """
    Ask the TinyLlama chat model hosted on Hugging Face and return the response.
    """
    try:
        response = await client.chat.completions.create(
            model="TinyLlama/TinyLlama-1.1B-Chat-v1.0:featherless-ai",
            messages=[{"role": "user", "content": question}],
            max_tokens=300,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[API Error] {str(e)}"
