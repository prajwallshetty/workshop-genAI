import os
from dotenv import load_dotenv
from litellm import completion

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "groq/llama-3.1-8b-instant")

SYSTEM_PROMPT = """
You are an AI product strategist.
Generate clear, structured startup-style product designs.
Be practical and industry-aware.
"""

def generate_pitch(prompt):

    response = completion(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6,
        max_tokens=900
    )

    return response["choices"][0]["message"]["content"]
