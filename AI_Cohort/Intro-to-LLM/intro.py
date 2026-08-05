from pathlib import Path
from dotenv import load_dotenv
import os

from groq import Groq

load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is meaning of name Kartik",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)