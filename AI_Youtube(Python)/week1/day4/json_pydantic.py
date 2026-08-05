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

# Structure
from pydantic import BaseModel

class Ticket(BaseModel):
    name : str
    email : str
    issue : str

schema = Ticket.model_json_schema()

response_format = {
    "type" : "json_object"
}

system_prompt=f"""
Extract the personal information from the ticket strictly based on this schema and give me output in json object format
{schema}
"""

message_system={
 "role" : "system",
 "content" : system_prompt
}

message_user={
    "role" : "user"
}
text="Hello my name is Kartik. I have purchased i-phone from you which is not working. I live in Nagpur. My email is abc@gmail.com. My contact number is 8208463693. I work as a senior software engineer"
prompt=f"""
This is a customer ticket. Please extract the personal information from this.
{text}
"""
# message me role and content
message={
    "role": role,
    "content": prompt
}

messages=[message_system, message]

response=client.chat.completions.create(model=model, messages=messages, response_format=response_format)
print(response)

print("#######################################")

answer=response.choices[0].message.content
print(answer)

# How to read this

import json
raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)
