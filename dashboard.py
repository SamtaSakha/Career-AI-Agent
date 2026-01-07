import streamlit as st

# -----------------------------
# Skill Database
# -----------------------------
KNOWN_SKILLS = [
    "python", "machine learning", "deep learning",
    "data science", "sql", "nlp", "pandas",
    "numpy", "statistics", "power bi"
]

REQUIRED_SKILLS_DS = [
    "python", "machine learning", "sql",
    "deep learning", "statistics", "nlp"
]

# -----------------------------
# Functions
# -----------------------------
def extract_skills(resume_text):
    resume_text = resume_text.lower()
    return [skill for skill in KNOWN_SKILLS if skill in resume_text]

def skill_gap_analysis(user_skills):
    return list(set(REQUIRED_SKILLS_DS) - set(user_skills))

def recommend_career(user_skills):
    if "machine learning" in user_skills:
        return "Data Scientist"
    elif "python" in user_skills:
        return "Data Analyst"
    else:
        return "Entry-Level AI Associate"

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="AI Career Guidance Agent", layout="centered")

st.title("🎯 AI-Powered Career Guidance Agent")
st.subheader("Aligned with SDG 8: Decent Work and Economic Growth")

st.markdown("Enter resume details below 👇")

resume_text = st.text_area(
    "Paste Resume Content",
    height=200,
    placeholder="Paste resume text here..."
)

if st.button("Analyze Career"):
    if resume_text.strip() == "":
        st.warning("Please enter resume content.")
    else:
        skills = extract_skills(resume_text)
        gaps = skill_gap_analysis(skills)
        career = recommend_career(skills)

        st.success("Analysis Completed ✅")

        st.markdown("### 🔹 Extracted Skills")
        st.write(skills if skills else "No matching skills found")

        st.markdown("### 🔹 Recommended Career Role")
        st.info(career)

        st.markdown("### 🔹 Skill Gaps")
        st.write(gaps if gaps else "No major gaps detected 🎉")

        st.markdown("### 🔹 Improvement Suggestions")
        for skill in gaps:
            st.write(f"- Learn **{skill}** to improve job readiness")
