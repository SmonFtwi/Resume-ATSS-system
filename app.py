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
    response = model.generate_content(input)
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


submit1 = st.button("Tell Me About the Resume")

submit3 = st.button("Percentage match")


# prompt sample
input_prompt1 = """
 You are an experienced Human Resources Manager tasked with reviewing a candidate's CV for an open position
 within your organization. Your objective is to assess the alignment between the candidate's qualifications 
 and the requirements outlined in the job description. Provide a comprehensive evaluation highlighting the 
 strengths and weaknesses of the applicant in relation to the specified job requirements. 
 Additionally, offer recommendations on whether the candidate's profile aligns with the role and
 any additional insights that would aid in the decision-making process.

Instructions:

Carefully examine the candidate's CV.
Compare the candidate's skills, experience, and qualifications with the job description.
Provide detailed feedback on how well the candidate meets the specific requirements of the HR Manager position.
Highlight any notable strengths or weaknesses in the candidate's profile.
Conclude your evaluation with a clear recommendation on whether the candidate is a suitable fit for the role.
Feel free to include any additional insights that could be valuable for the hiring decision.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""
if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt1)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt3)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")
