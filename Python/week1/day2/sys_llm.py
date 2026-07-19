import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
prompt="Suggest a name for my cloth company brand"

# message me role and content
message_system={
    "role": "system",
    "content": "You are a brand manager who suggests name for my food brand, name should be in one word, suggest one name only"
}
message={
    "role": role,
    "content": prompt
}

messages=[message_system, message]

response=client.chat.completions.create(model=model, messages=messages, temperature=0)
print(response)

print("#######################################")

answer=response.choices[0].message.content
print(answer)