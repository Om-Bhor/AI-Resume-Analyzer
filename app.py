from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import pdfplumber
from google import genai



client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)
if not os.getenv("GOOGLE_API_KEY"):
    st.error("GOOGLE_API_KEY not found. Please check your .env file.")
    st.stop()

def get_gemini_response(prompt, resume_text, job_description):
    try:
        full_prompt = f"""
        {prompt}

        Job Description:
        {job_description}

        Resume:
        {resume_text}
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"


# Extract Text From PDF
def input_pdf_text(uploaded_file):
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            extracted_text = page.extract_text()

            if extracted_text:
                text += extracted_text + "\n"

    return text


# Streamlit UI
st.set_page_config(page_title="ATS Resume Expert")

st.header("AI Resume Analyser")

input_text = st.text_area("Paste Job Description", key="input")

uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:
    st.success("PDF Uploaded Successfully")


# Buttons
submit1 = st.button("Tell Me About The Resume")
submit2 = st.button("How Can I Improve My Skills")
submit3 = st.button("Percentage Match")


# Prompt 1
input_prompt1 = """
You are an experienced Technical HR Manager.

Analyze the candidate’s resume against the provided job description 
and evaluate whether the candidate is suitable for the role.

Provide the response in the following format:

1. Candidate Overview
2. Key Strengths
3. Key Weaknesses
4. Job Role Fit
5. Hiring Decision

Keep the response concise, professional, and recruiter-focused.
"""


# Prompt 2
input_prompt2 = """
You are an AI Career Mentor and Technical Skill Advisor.

Analyze the resume and job description and provide:

1. Target Role Identification
2. Missing Skills
3. Learning Recommendations
4. Project Suggestions
5. Resume Improvement Tips
6. Career Growth Plan

Focus only on improvement guidance and career development.
"""


# Prompt 3
input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner.

Evaluate the resume against the provided job description.

Provide:
1. ATS Match Percentage
2. Missing Keywords
3. Final Thoughts
"""


# Button Logic
if submit1:

    if uploaded_file is not None:

        resume_text = input_pdf_text(uploaded_file)

        response = get_gemini_response(
            input_prompt1,
            resume_text,
            input_text
        )

        st.subheader("Resume Evaluation")
        st.write(response)

    else:
        st.warning("Please upload a resume.")


elif submit2:

    if uploaded_file is not None:

        resume_text = input_pdf_text(uploaded_file)

        response = get_gemini_response(
            input_prompt2,
            resume_text,
            input_text
        )

        st.subheader("Skill Improvement Suggestions")
        st.write(response)

    else:
        st.warning("Please upload a resume.")


elif submit3:

    if uploaded_file is not None:

        resume_text = input_pdf_text(uploaded_file)

        response = get_gemini_response(
            input_prompt3,
            resume_text,
            input_text
        )

        st.subheader("ATS Match Analysis")
        st.write(response)

    else:
        st.warning("Please upload a resume.")