import os
import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def test():
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI mentor."},
            {"role": "user", "content": "Hello, are you working?"},
        ]
    )
    print(response.choices[0].message.content)

asyncio.run(test())
