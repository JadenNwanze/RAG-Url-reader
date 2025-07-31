#  RAG-URL-reader

**RAG-URL-reader** is a Retrieval-Augmented Generation (RAG) system that transforms any public webpage into an intelligent, queryable knowledge base. By combining state-of-the-art machine learning and MLOps practices, this system enables users to extract meaningful insights from online content with just a URL input.

---

##  Project Summary

RAG-URL-reader automates the entire workflow of:

1. **Scraping and parsing** content from any user-provided URL  
2. **Generating dense vector embeddings** using HuggingFace Transformer models  
3. **Storing vectors efficiently** using Facebook AI Similarity Search (FAISS)  
4. **Answering user questions** about the content using LangChain's RAG framework and a language model  
5. **Providing real-time interaction** through a user-friendly Streamlit interface and FastAPI backend  

This project showcases not only advanced NLP concepts, but also **production-grade MLOps practices** including modular pipeline design, containerization (Docker), and multi-interface support (REST + UI).

---

## Key Features

-  **End-to-End RAG Pipeline** – From raw web content to intelligent answers in one system
-  **Natural Language QA** – Uses LangChain and LLMs to generate accurate, human-like answers
-  **HuggingFace Embedding Integration** – Leverages pretrained models for semantic vectorization
-  **FAISS Vector Search** – Fast and scalable similarity search engine
-  **MLOps-Ready** – Built with modularity, versioning, and deployment in mind
-  **RESTful API via FastAPI** – Backend designed for scalability and integration
-  **Streamlit UI** – Easy-to-use interface for non-technical users

---

##  MLOps Methodologies Applied

This project goes beyond prototyping, by integrating MLOps principles throughout its lifecycle:

###  Modular Pipeline Design
Each core functionality—scraping, embedding, vector storage, and question-answering—is encapsulated into standalone, reusable modules. This improves scalability, maintainability, and ease of testing.

### Reproducibility
- Clear dependency management through requirements.txt
- Deterministic embedding and storage pipeline ensures consistency across runs

### Containerization-Ready
A Dockerfile is included to enable deployment across environments without setup inconsistencies. This enhances CI/CD readiness and accelerates deployment to platforms like AWS, Azure, GCP, or DockerHub.

###  API + UI Dual Support
- The **FastAPI backend** allows programmatic access for enterprise applications
- The **Streamlit frontend** provides an interactive interface for demos or internal tooling

---

##  Example Use Case

> **Problem:** A user wants to quickly understand the main points of a technical article without reading the entire page.

> **Solution:**  
1. Paste the article's URL into the system  
2. Ask questions like:  
   - "What is the article about?"  
   - "Who are the key researchers mentioned?"  
   - "What are the main findings or arguments?"  
3. Get concise, context-aware answers derived directly from the scraped content

---

##  Technologies Used

| Category              | Tools / Frameworks              |
|-----------------------|----------------------------------|
| LLM & QA              | LangChain, OpenAI (or similar)   |
| Embedding Models      | HuggingFace Transformers (`sentence-transformers`) |
| Vector Store          | FAISS                            |
| API Backend           | FastAPI                          |
| UI Interface          | Streamlit                        |
| Web Scraping          | WebBasedLoader, Requests          |
| DevOps / MLOps        | Docker          |
| Language              | Python 3.13                     |

---

##  Deployment Note

Due to platform cost constraints, the project has **not been deployed live** yet. However, it has been developed and tested locally, and is fully compatible with deployment platforms like:

- Render
- Vercel (Streamlit frontend)
- AWS EC2 / Lambda
- Heroku
- Docker Swarm / Kubernetes

---

## How to use
- uvicorn app.backend:app --reload, to run Fastapi backend
- streamlit run app/frontend.py, to run Streamlit UI

## To view the Proof of Concept(POC):
- Use this link:
- https://rag-url-reader.streamlit.app/
