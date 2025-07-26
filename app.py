import streamlit as st
from modules.utils import load_resumes, prepare_embeddings
from modules.embedder import get_embedding
from modules.ranker import rank_resumes

st.set_page_config(page_title="Resume Screener", layout="wide")
st.title("📄 AI-Powered Resume Screener")

job_description = st.text_area("Paste the Job Description Here:")
resumes_folder = "data/resumes"

if st.button("Rank Resumes"):
    if job_description:
        with st.spinner("Processing resumes..."):
            resumes = load_resumes(resumes_folder)
            resume_names = list(resumes.keys())
            resume_texts = list(resumes.values())

            job_embed = get_embedding(job_description)
            resume_embeds = prepare_embeddings(resume_texts)

            scores = rank_resumes(job_embed, resume_embeds)
            sorted_results = sorted(zip(resume_names, scores), key=lambda x: x[1], reverse=True)

            st.success("Resumes Ranked by Relevance")
            for name, score in sorted_results:
                st.write(f"📄 {name} — Similarity Score: {score:.2f}")
    else:
        st.warning("Please enter a job description first.")
