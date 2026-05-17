from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import io
import base64
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the pdf to bytes
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]
        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# STREAMLIT
st.set_page_config(page_title = "ATS Resume Expert")
st.header("AI Resume Analyser")
input_text =st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Uploade Your resume(PDF)", type=["pdf"])

if file_uploaded is not None:
    st.write("PDF Upoaded Succesfully")

submit1 = st.button("Tell Me About The Resume")
submit2 = st.button("How Can I Improvise My Skills")
submit3 = st.button("Percentage Match")

input_prompt1 = """
You are an experienced Technical HR Manager.

Analyze the candidate’s resume against the provided job description 
and evaluate whether the candidate is suitable for the role.

Provide the response in the following format:

1. Candidate Overview
- Brief summary of the profile.

2. Key Strengths
- Mention the strongest matching skills, projects, and experiences.

3. Key Weaknesses
- Mention missing skills or experience gaps.

4. Job Role Fit
- Explain how well the profile aligns with the job description.

5. Hiring Decision
- Classify the candidate as:
  - Strong Fit
  - Moderate Fit
  - Weak Fit

Keep the response concise, professional, and recruiter-focused.

Do not provide learning roadmaps or career guidance.
"""

input_prompt2 = """
You are an AI Career Mentor and Technical Skill Advisor.

Your task is to help the candidate improve their profile for the most suitable role 
based on the provided job description. The role may belong to one of the following domains:
- Data Science
- Full Stack Development
- AI Engineering
- Generative AI Engineering
- Ml Engineering

Analyze the resume and job description, then provide:

1. Target Role Identification
- Identify which role best matches the candidate’s profile and the job description.

2. Missing Skills
- Mention important technical skills, tools, or concepts missing from the profile.

3. Learning Recommendations
- Suggest technologies, frameworks, and concepts the candidate should learn.

4. Project Suggestions
- Recommend practical projects to strengthen the candidate’s portfolio.

5. Resume Improvement Tips
- Suggest ATS optimization, resume formatting, and presentation improvements.

6. Career Growth Plan
- Suggest a roadmap for improving the profile over the next few months.

Focus only on improvement guidance and career development.
Do not provide hiring decisions or ATS scores.

If information is missing, do not assume details that are not present in the resume.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of Data Science, Full Stack Development, AI Engineering, or Generative AI roles and deep ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""
if submit1:
    if file_uploaded is not None:
        pdf_content = input_pdf_setup(uploded_file)
        resplonse = get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please Upload Resume")
elif submit2:
    if file_uploaded is not None:
        pdf_content = input_pdf_setup(uploded_file)
        resplonse = get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please Upload Resume")
elif submit3:
    if file_uploaded is not None:
        pdf_content = input_pdf_setup(uploded_file)
        resplonse = get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please Upload Resume")
