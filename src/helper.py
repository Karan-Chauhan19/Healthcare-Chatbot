'''
Author : Karan Chauhan
Github : Karan-Chauhan19
Organization : L.J University
'''

import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import torch

class Helper:
    def __init__(self, db_path="vector_store/chroma_db"):
        self.db_path = db_path
        self.embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cuda" if torch.cuda.is_available() else "cpu"}
        )

    def load_pdf(self):
        loader = PyPDFLoader('/home/karan-chauhan/WorkStation/Project/Healthcare-Chatbot/Data/Symptoms.pdf')
        return loader.load()

    def text_splitter(self):
        docs = self.load_pdf()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        return text_splitter.split_documents(docs)

    def get_or_create_embeddings(self):
        """Loads saved embeddings or creates new ones if missing"""
        if os.path.exists(self.db_path):
            print("✅ Loading existing embeddings...")
            return Chroma(persist_directory=self.db_path, embedding_function=self.embedding_model)

        print("⚡ Creating new embeddings (First Run Only)...")
        documents = self.text_splitter()
        db = Chroma.from_documents(documents, self.embedding_model, persist_directory=self.db_path)
        db.persist()
        return db
