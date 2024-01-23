# Resume-ATS-system

This system analyzes resumes by extracting text from PDFs. Utilizing the Google Gemini API, it comprehensively evaluates the resume against a provided job description, offering detailed feedback about the candidate's qualifications and alignment with the job requirements.

## Libraries Used

- [Streamlit](https://streamlit.io/)
- [Google GenerativeAI](https://example.com/generativeai)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [PyPDF2](https://pythonhosted.org/PyPDF2/)

## Getting Started

1. Clone this repository.

```bash
git clone https://github.com/SmonFtwi/Resume-ATSS-system
cd your-project
```

2. Install the required libraries.

```bash
pip install requirements.txt
```

3. Set up the necessary environment variables.

- **For `google-generativeai`:**
  - Obtain an API key from [here](https://makersuite.google.com/app/apikey).
  - Set the API key as an environment variable.

4. Run the application.

```bash
streamlit run app.py
```
