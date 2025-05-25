import streamlit as st
from resume_parser import extract_text_from_pdf, extract_sections
from utils import match_score

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

st.markdown("""
    <style>
    .big-font {
        font-size:28px !important;
        font-weight: 700;
    }
    .score-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #0072C6;
        margin-top: 10px;
    }
    .matched-skills {
        background-color: #e8f5e9;
        padding: 15px;
        border-radius: 8px;
        color: #2e7d32;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)


st.title("📄 AI-Powered Resume Analyzer")
st.markdown("Use this tool to analyze how well your resume matches a job description. Get an instant score and feedback. 🚀")

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader("📤 Upload Your Resume (PDF)", type=["pdf"])
with col2:
    job_desc = st.text_area("📝 Paste Job Description")

if resume_file and job_desc:
    with st.spinner("⚙️ Analyzing your resume..."):
        text = extract_text_from_pdf(resume_file)
        sections = extract_sections(text)
        score, matched_skills = match_score(text, job_desc)

    
    st.markdown("<div class='score-box'>📊 Relevance Score: {:.2f} / 100</div>".format(score), unsafe_allow_html=True)


    st.markdown("### 🧩 Matched Skills")
    if matched_skills:
        st.markdown("<div class='matched-skills'>" + ", ".join(matched_skills) + "</div>", unsafe_allow_html=True)
    else:
        st.warning("No matching skills found. Try improving your resume.")

   
    st.markdown("### 📄 Resume Breakdown")
    for section, content in sections.items():
        with st.expander(f"📌 {section}"):
            st.write(content[:1000] + "..." if len(content) > 1000 else content)

    st.markdown("### 💡 Tips to Improve")
    st.info("""
    - Make sure your resume includes keywords from the job description.
    - Emphasize technical skills, certifications, and measurable achievements.
    - Use active language and structured formatting.
    """)

else:
    st.info("📎 Upload a resume and paste a job description to get started.")
