import streamlit as st
from utils.pdf_extractor import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.ats_score import calculate_ats_score
from utils.recommender import recommend_role

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("AI Resume Analyzer")
st.write("Upload your resume PDF to analyze skills.")
st.sidebar.title("AI Resume Analyzer")
st.sidebar.write("Built using NLP and Streamlit")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file is not None:

    #extract text
    resume_text = extract_text_from_pdf(uploaded_file)

    #extract skills
    skills = extract_skills(resume_text)

    st.subheader("Extracted Skills")

    if skills:
        for skill in skills:
            st.success(skill)
    else:
        st.warning("No skills found.")


    #missing skills detection
    all_skills = [
        "Python",
        "Java",
        "Machine Learning",
        "Deep Learning",
        "SQL",
        "HTML",
        "CSS",
        "JavaScript",
        "TensorFlow",
        "PyTorch",
        "React",
        "Node.js",
        "Data Analysis",
        "AWS",
        "Git"
    ]
    missing_skills = []

    for skill in all_skills:
         if skill not in skills:
             missing_skills.append(skill)
    
    st.subheader("Missing Skills")
    
    for skill in missing_skills:
        st.warning(skill)


    #ats score
    score = calculate_ats_score(skills)
    st.subheader("ATS Score")
    st.metric(label="Resume Score", value=f"{score}%")     



    #role recommendation
    recommended_role = recommend_role(skills)

    st.subheader("Recommended Role")
    st.success(recommended_role)
    
  