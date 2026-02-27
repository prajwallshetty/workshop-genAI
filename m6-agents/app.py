import streamlit as st
from agent_brain import resume_agent

st.set_page_config(page_title="Resume Evaluation Agent", layout="wide")

st.title("🤖 AI Resume Evaluation Agent")
st.write("Compare a Resume with a Job Description")

# Input areas
resume_text = st.text_area("📄 Paste Resume Text", height=250)
job_description = st.text_area("📌 Paste Job Description", height=250)

if st.button("Evaluate Resume"):

    if resume_text and job_description:

        with st.spinner("Analyzing resume..."):
            result = resume_agent(resume_text, job_description)

        st.success("Analysis Complete ✅")

        st.markdown("### 📊 Agent Report")
        st.write(result)

    else:
        st.warning("Please enter both Resume and Job Description.")