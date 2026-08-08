from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq()

messages_example=[
    {
"role" : "system",
"content" : """

"""
    },
    {
"role" : "user",
"content" : ""
    },
    {
"role" : "assistant",
"content" : ""
    }
]