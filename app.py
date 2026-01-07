import nltk
from sklearn.feature_extraction.text import CountVectorizer

# Download required NLP resources
nltk.download('punkt')

# -----------------------------
# Step 1: Load Resume
# -----------------------------
def load_resume(file_path):
    with open(file_path, "r") as file:
        return file.read()

# -----------------------------
# Step 2: Extract Skills (Basic NLP)
# -----------------------------
def extract_skills(resume_text):
    known_skills = [
        "python", "machine learning", "deep learning",
        "data science", "sql", "nlp", "pandas",
        "numpy", "statistics", "power bi"
    ]

    resume_text = resume_text.lower()
    extracted = [skill for skill in known_skills if skill in resume_text]
    return extracted

# -----------------------------
# Step 3: Skill Gap Analysis
# -----------------------------
def skill_gap_analysis(user_skills):
    required_skills = [
        "python", "machine learning", "sql",
        "deep learning", "statistics", "nlp"
    ]

    missing_skills = list(set(required_skills) - set(user_skills))
    return missing_skills

# -----------------------------
# Step 4: Career Recommendation
# -----------------------------
def recommend_career(user_skills):
    if "machine learning" in user_skills:
        return "Recommended Role: Data Scientist"
    elif "python" in user_skills:
        return "Recommended Role: Data Analyst"
    else:
        return "Recommended Role: Entry-Level AI Associate"

# -----------------------------
# Step 5: Resume Improvement Suggestions
# -----------------------------
def resume_suggestions(missing_skills):
    suggestions = []
    for skill in missing_skills:
        suggestions.append(f"Consider learning {skill} to improve job readiness.")
    return suggestions

# -----------------------------
# Main AI Agent Flow
# -----------------------------
def career_ai_agent(resume_path):
    resume_text = load_resume(resume_path)
    skills = extract_skills(resume_text)
    missing_skills = skill_gap_analysis(skills)
    career = recommend_career(skills)
    suggestions = resume_suggestions(missing_skills)

    print("----- AI Career Agent Output -----\n")
    print("Extracted Skills:", skills)
    print("\nSkill Gaps:", missing_skills)
    print("\nCareer Recommendation:", career)
    print("\nResume Improvement Suggestions:")
    for s in suggestions:
        print("-", s)

# Run Agent
career_ai_agent("resume_sample.txt")
