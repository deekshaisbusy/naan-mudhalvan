
# Step 1: Install Required Libraries
!pip install -q PyPDF2 python-docx
# Step 2: Import Libraries
import PyPDF2
import docx
import os
from google.colab import files
# Step 3: Upload Resumes
uploaded = files.upload()
# Step 4: Define Skill Keywords
skills_keywords = ['python', 'java', 'c++', 'machine learning', 'data science',
                   'excel', 'sql', 'communication', 'teamwork', 'project management']
# Step 5: Functions to Extract Text
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()
def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ''
    for para in doc.paragraphs:
        text += para.text
    return text.lower()
# Step 6: Analyze Resumes
for filename in uploaded.keys():
    print(f"\nAnalyzing: {filename}")
    if filename.endswith('.pdf'):
        with open(filename, 'rb') as f:
            text = extract_text_from_pdf(f)
    elif filename.endswith('.docx'):
        text = extract_text_from_docx(filename)
    else:
        print("Unsupported file format.")
        continue
    matched_skills = [skill for skill in skills_keywords if skill in text]
    print("Matched Skills:", matched_skills)
    print("Score:", len(matched_skills), "/", len(skills_keywords))