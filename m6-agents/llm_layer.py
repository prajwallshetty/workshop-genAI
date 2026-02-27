import os
from dotenv import load_dotenv
from litellm import completion

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "groq/llama-3.1-8b-instant")

SYSTEM_PROMPT = """
You are a professional Resume Evaluation Agent.
Follow step-by-step reasoning.
Provide structured output.
"""

def generate_agent_response(prompt):
    response = completion(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=800
    )

    return response["choices"][0]["message"]["content"]
