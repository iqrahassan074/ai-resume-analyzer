import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_skill_list():
    with open("assets/skills.json", "r") as f:
        return json.load(f)

def match_score(resume_text, job_desc):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_desc])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    skills = load_skill_list()
    matched = [skill for skill in skills if skill.lower() in resume_text.lower()]

    return similarity * 100, matched
