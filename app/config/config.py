import os
HF_TOKEN = os.environ.get("HF_TOKEN")

HUGGINGFACE_REPO_ID="mistralai/Mistral-7B-Instruct-v0.3"
DB_FAISS_PATH=r"C:\Python_Project\LLMops\Medical_RAG_Chatbot\vectorstore\dp_faiss"
DATA_PATH="C:\Python_Project\LLMops\Medical_RAG_Chatbot\data"
CHUNK_SIZE=500
CHUNK_OVERLAP=50
