
---

# 📘 toolkit.md

```markdown
# Prompt-Powered Kickstart: Building a Beginner Data API with FastAPI

---

## 1. Title & Objective

### Technology Chosen:
FastAPI (Python framework)

### Why I Chose It:
I recently graduated with a certificate in Data Science and wanted to learn how to expose data insights through a web API. FastAPI is a modern, fast, and beginner-friendly framework for building APIs.

### End Goal:
To build a simple API that loads a dataset and returns basic statistics such as mean, minimum, maximum, and record count.

---

## 2. Quick Summary of the Technology

FastAPI is a modern Python web framework used to build APIs quickly and efficiently. It is widely used for:
- Machine learning model deployment
- Data services
- Microservices

### Real-world Example:
FastAPI is commonly used to deploy machine learning models as REST APIs.

---

## 3. System Requirements

- Operating System: Windows / Mac / Linux  
- Python 3.9+  
- Code Editor (VS Code recommended)  
- Terminal or Command Prompt  

---

## 4 .Installation & Setup Instructions (Quick Guide)

To run this project locally, follow these steps:

1. Navigate to the project folder and run the following commands:

```bash
cd data-api
2. Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)
source venv/bin/activate      # Mac/Linux

3. install required dependencies

pip install fastapi uvicorn pandas

4. Start the FastAPI server:

python -m uvicorn main:app --reload