def extract_keywords(text):
    words = text.lower().split()
    return set(words)

def compare_skills(resume_text, jd_text):
    resume_words = extract_keywords(resume_text)
    jd_words = extract_keywords(jd_text)

    matched = resume_words.intersection(jd_words)
    missing = jd_words - resume_words

    return list(matched), list(missing)
