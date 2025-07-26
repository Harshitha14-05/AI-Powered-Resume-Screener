# 🤖 AI-Powered Resume Screener

This project is an intelligent resume screening tool built using **Python**, **Streamlit**, and **NLP** techniques. It allows users to upload resumes and a job description, and automatically ranks resumes based on relevance.

---

## 📌 Features

- Upload multiple resumes in PDF/DOCX format
- Upload or type a Job Description
- NLP-based similarity scoring
- Resume ranking and filtering
- Clean, Streamlit-based UI

---

## 🛠️ Tech Stack

- Python
- Streamlit
- FAISS (Facebook AI Similarity Search)
- Sentence Transformers (BERT model)
- Pandas, NumPy
- PDF and DOCX parsing

---

## 🚀 Project Setup

Follow these steps in your terminal to set up and run the project:

```bash
# Step 1: Clone the repository
git clone https://github.com/Harshitha14-05/AI-Powered-Resume-Screener.git

# Step 2: Navigate into the project directory
cd AI-Powered-Resume-Screener

# Step 3: (Optional but recommended) Create a virtual environment
python -m venv venv
venv\Scripts\activate     # For Windows
# source venv/bin/activate  # For macOS/Linux

# Step 4: Install dependencies
pip install -r requirements.txt

# Step 5: Run the Streamlit app
streamlit run app.py
📁 Folder Structure
bash
Copy code
AI-Powered-Resume-Screener/
│
├── app.py                     # Main Streamlit app
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── sample_resumes/           # Folder to upload sample resumes
│
└── modules/                  # Utility functions
    ├── __init__.py
    └── utils.py              # Functions for parsing, embedding, and scoring
📂 Sample Resume Upload
You can place your resume PDFs or DOCX files into the sample_resumes/ folder, or upload them directly through the Streamlit UI.

Need help with sample resumes? You can generate some free ones from:

https://www.resume.com

https://www.canva.com/resumes

Or ask ChatGPT to generate dummy resume content for you.

🔍 How It Works
Upload resumes.

Upload or paste a job description.

The app converts resumes to text and generates embeddings.

It calculates cosine similarity between each resume and the job description.

Displays ranked resumes with scores.

📦 Deployment
To deploy this project online:

Streamlit Cloud: Easy one-click deploy. Visit https://streamlit.io/cloud

Render or Railway: Create a Python web service and deploy app.py

Let me know if you want a streamlit_app.py and deployment guide.

🙌 Acknowledgments
Streamlit

Sentence Transformers

FAISS

🧠 Author
Harshitha
Built for portfolio and learning purpose 🚀

