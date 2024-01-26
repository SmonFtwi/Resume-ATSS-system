import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

load_dotenv()  # load all the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini pro response


def get_gemini_response(input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([input])
    return response.text


# convert PDF to text
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text


# Stramlit APP
st.set_page_config(page_title="ATS Resume Analyzer")
st.header("ATS Tracking system")
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume(PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded successfully")


submit3 = st.button("Percentage match")


# prompt sample


ats_scanner_prompt = """
Simulate an ATS (Applicant Tracking System) scanner scenario:

You are an advanced ATS scanner equipped with data science knowledge. Your task is to evaluate the resume against the provided job description. Begin by acting like an ATS and scan the resume for relevant keywords and qualifications. Next, check the job description data provided below against the resume data. Provide a percentage match, list any keywords missing, and conclude with your final thoughts on the candidate's suitability.

---

**Job Description Data:**
[Insert Job Description Here]

---
"""

if submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_text(uploaded_file)
        response = get_gemini_response(f"{ats_scanner_prompt}\n{pdf_content}")
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")
