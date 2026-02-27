from tools import compare_skills
from llm_layer import generate_agent_response

def resume_agent(resume_text, job_description):

    matched, missing = compare_skills(resume_text, job_description)

    prompt = f"""
Step 1: Analyze resume.

Step 2: Compare with job description.

Matched Skills:
{matched}

Missing Skills:
{missing}

Step 3: Provide:

- Summary of resume strength
- Improvement suggestions
- Final Score out of 10
"""

    return generate_agent_response(prompt)
