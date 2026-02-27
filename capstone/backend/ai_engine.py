import os
from groq import Groq
from prompts import get_system_prompt
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_response(mode, user_input):

    system_prompt = get_system_prompt(mode)

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # updated model
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.5
    )

    return completion.choices[0].message.content