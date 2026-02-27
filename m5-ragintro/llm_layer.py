import os
from dotenv import load_dotenv
from litellm import completion

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "groq/llama-3.1-8b-instant")

SYSTEM_PROMPT = """
You are a domain-aware AI assistant.
Answer ONLY using the provided context.
If the answer is not in context, say:
'I do not have enough information in the provided documents.'
"""

def generate_answer(context, question):
    prompt = f"""
Context:
{context}

Question:
{question}

Answer using ONLY the context above.
"""

    response = completion(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=600
    )

    return response["choices"][0]["message"]["content"]
