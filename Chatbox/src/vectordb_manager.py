# vectordb_manager.py

import os
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_or_create_vectorstore(docs=None, save_path="vectorstore_index"):
    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # ✅ Load only mode
    if docs is None:
        if os.path.exists(f"{save_path}/index.faiss"):
            return FAISS.load_local(save_path, embedding_function, allow_dangerous_deserialization=True)
        else:
            raise ValueError("No existing vectorstore found. Please run the embedding step first.")

    # ✅ Create and save vectorstore if docs are provided
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=100,
        separators=["\n\n", "\n", " ", "."]
    )
    chunks = splitter.split_documents(docs)
    vectorstore = FAISS.from_documents(chunks, embedding=embedding_function)
    vectorstore.save_local(save_path)

    return vectorstore
