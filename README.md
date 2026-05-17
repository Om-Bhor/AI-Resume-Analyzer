# AI Resume Analyzer

An AI-powered Resume Analyzer built using Python, Streamlit, and Google Gemini API.
This project analyzes resumes against job descriptions and provides:

* ATS Match Percentage
* Resume Evaluation
* Skill Improvement Suggestions
* Career Guidance
* Missing Skills Analysis

The application is designed for roles such as:

* Data Science
* Full Stack Development
* AI Engineering
* Generative AI Engineering

---

# Features

## Resume Analysis

* Upload resume in PDF format
* Extract resume text
* Analyze candidate profile
* Identify strengths and weaknesses

## ATS Scanner

* ATS match percentage
* Missing keyword detection
* Resume optimization suggestions

## Skill Improvement Suggestions

* Missing technical skills
* Learning recommendations
* Project recommendations
* Career growth roadmap

## AI-Powered Insights

* Uses Google Gemini API for intelligent analysis
* Context-aware evaluation
* Structured professional feedback

---

# Tech Stack

| Technology        | Purpose                         |
| ----------------- | ------------------------------- |
| Python            | Backend Logic                   |
| Streamlit         | Web Application UI              |
| Google Gemini API | AI Analysis                     |
| python-dotenv     | Environment Variable Management |
| pdf2image         | PDF Processing                  |
| Pillow            | Image Handling                  |
| Poppler           | PDF Rendering Dependency        |

---

# Project Structure

```bash
Resume_Analyser/
│
├── app.py
├── requirements.txt
├── packages.txt
├── README.md
├── .env
├── .gitignore
└── venv/
```

---

# Installation Guide

## 1. Clone Repository

```bash
git clone <your_repo_link>
cd Resume_Analyser
```

---

## 2. Create Virtual Environment

```bash
python3 -m venv venv
```

---

## 3. Activate Virtual Environment

### macOS/Linux

```bash
source venv/bin/activate
```

---

## 4. Install Required Python Libraries

```bash
pip install -r requirements.txt
```

---

# Requirements File

Create a `requirements.txt` file:

```txt
streamlit
google-generativeai
python-dotenv
pdf2image
Pillow
```

---

# Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

# Install Poppler (Important)

`pdf2image` requires Poppler for PDF processing.

## macOS

Install using Homebrew:

```bash
brew install poppler
```

Verify installation:

```bash
pdfinfo -v
```

---

# Run the Project

```bash
streamlit run app.py
```

After running, Streamlit will provide a local URL such as:

```bash
http://localhost:8501
```

Open it in your browser.

---

# GitHub Setup

## Initialize Git

```bash
git init
```

## Add Files

```bash
git add .
```

## Commit Changes

```bash
git commit -m "Initial Commit"
```

## Connect GitHub Repository

```bash
git remote add origin <your_repo_link>
git branch -M main
git push -u origin main
```

---

# Hugging Face Deployment

## Create `packages.txt`

Because `pdf2image` requires Poppler:

```txt
poppler-utils
```

---

## Upload Files to Hugging Face Space

Required files:

```bash
app.py
requirements.txt
packages.txt
README.md
```

---

# Common Errors Faced During Development

## 1. Virtual Environment Creation Error

### Error

```bash
Error: Refusing to create a venv because it contains the PATH separator :
```

### Cause

Folder name contained a colon (`:`).

### Solution

Rename folder to remove special characters.

Example:

❌ Wrong:

```bash
Learning:Project
```

✅ Correct:

```bash
Learning_Project
```

---

## 2. ModuleNotFoundError: pdf2image

### Error

```bash
ModuleNotFoundError: No module named 'pdf2image'
```

### Solution

```bash
pip install pdf2image
```

---

## 3. Poppler Not Installed

### Error

```bash
PDFInfoNotInstalledError
```

### Solution

```bash
brew install poppler
```

---

## 4. Homebrew Permission Denied Error

### Error

```bash
Permission denied
/Users/username/Library/Caches/Homebrew/
```

### Solution

```bash
sudo chown -R $(whoami) ~/Library/Caches/Homebrew
chmod -R u+w ~/Library/Caches/Homebrew
rm -rf ~/Library/Caches/Homebrew/api
```

Then reinstall:

```bash
brew install poppler
```

---

## 5. Streamlit Stop Command

To stop Streamlit server:

```bash
Ctrl + C
```

---

# Future Improvements

* Multi-Resume Ranking System
* AI Interview Question Generator
* Resume Chatbot using RAG
* Recruiter Dashboard
* Real-Time Resume Scoring
* Resume Recommendation Engine
* Vector Database Integration
* LangChain Integration
* FastAPI Backend

---

# Learning Outcomes

This project demonstrates:

* NLP Concepts
* Prompt Engineering
* ATS Analysis
* Resume Parsing
* Generative AI Integration
* Streamlit Deployment
* API Integration
* Environment Variable Management
* Real-World AI Application Development

---

# Author

OM RAJESH BHOR

---

# License

This project is for educational and portfolio purposes.
