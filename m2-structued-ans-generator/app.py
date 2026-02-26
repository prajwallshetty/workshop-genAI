import os
import json
from flask import Flask, request, render_template
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_structured_answer(user_input):

    system_prompt = """
You are a structured response generator.

STRICT RULES:
1. Output ONLY valid JSON.
2. No markdown.
3. No explanation outside JSON.
4. Follow exact schema:

{
  "title": string,
  "summary": string,
  "key_points": [string],
  "action_steps": [string]
}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # instant LLM
        temperature=0,  # Deterministic
        top_p=1,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    content = response.choices[0].message.content

    return json.loads(content)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        user_input = request.form["query"]
        result = generate_structured_answer(user_input)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)