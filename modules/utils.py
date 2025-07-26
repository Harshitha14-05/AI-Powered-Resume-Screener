import os
from modules.extract_text import extract_text
from modules.embedder import get_embedding


def load_resumes(folder_path):
    resumes = {}
    for file_name in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file_name)
        try:
            text = extract_text(full_path)
            resumes[file_name] = text
        except:
            continue
    return resumes


def prepare_embeddings(texts):
    return [get_embedding(text) for text in texts]

