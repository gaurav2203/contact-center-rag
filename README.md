# Contact-Center RAG Chatbot

## 📖 Case Study Introduction

Modern contact centers face a growing challenge: customers expect instant, accurate, and conversational responses across a wide range of inquiries—from booking details and policy clarifications to troubleshooting and general service questions. Traditional knowledge‑base systems often fall short, relying on rigid search mechanisms and manually maintained response flows.

As part of a **project**, this system was developed to address a real-world use case: *building an intelligent, retrieval‑augmented chatbot that can serve as the first line of support for a hotel or service organization’s contact center.*

The goal was to design a fully functional RAG pipeline that:

* ingests and index operational documents (FAQs, policies, SOPs),
* retrieves the most relevant information in real time,
* and generates accurate, grounded responses using an LLM.

The project demonstrates how modern AI techniques can drastically reduce customer wait times, offload routine queries from agents, and ensure consistent, policy‑aligned communication.

## 🚀 Project Overview

This capstone solution showcases a complete RAG application—combining document ingestion, vector search, LLM‑based generation, and a user‑friendly chat interface—to solve real customer‑support challenges.

## 📂 Repository Structure

```
contact-center-rag/
|-- content/             # Document corpus used for indexing
|-- vector_store/        # Generated vector index (FAISS)
|-- notebooks/           # Experiments and prototypes
|-- src/
|   |-- ingestion.py     # Document ingestion + embeddings
|   |-- retrieval.py     # Vector search
|   |-- generation.py    # LLM prompting logic
|   |-- api.py           # FastAPI endpoints
|-- frontend/
|   |-- app.py           # Streamlit chatbot UI
|-- requirements.txt
|-- .gitignore
```

## 🧰 Tech Stack

* **FastAPI** — Backend API
* **Streamlit** — Frontend UI
* **FAISS** — Vector database
* **LLMs** — OLLAMA/ Local models
* **Python 3.10+**

---

## ⚙️ Installation & Setup

### 1. Clone the repo

```
git clone https://github.com/gaurav2203/contact-center-rag.git
cd contact-center-rag
```

### 2. Create virtual environment

```
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Create `.env` file

Example:

```
OLLAMA_API_KEY=your_key_here
```

### 5. Ingest documents

```
python src/ingestion.py --docs ./content --index_path ./vector_store
```

### 6. Run backend

```
uvicorn src.api:app --reload --host 0.0.0.0 --port 8000
```

### 7. Run frontend

```
cd frontend
streamlit run app.py
```

---

## 💬 Usage

Ask natural-language questions through the Streamlit UI.

API example:

```
curl -X POST "http://localhost:8000/query" \
     -H "Content-Type: application/json" \
     -d '{"query": "What are the check-in timings?", "top_k": 5}'
```

---

## 📐 Architecture

1. **Documents** → chunking → **Embeddings** → stored in FAISS
2. User asks question
3. Backend embeds question and retrieves top-K relevant chunks
4. LLM generates grounded response
5. Streamlit displays answer + sources

---

## 🔧 Customization

* Replace FAISS with Pinecone/Milvus in `retrieval.py`
* Swap embedding/LLM provider in `generation.py`
* Add more document types (PDF/CSV/SOP docs) in `ingestion.py`

---

## 📦 Deployment

* Use production LLMs
* Add API authentication
* Add caching + logging
* Run behind NGINX or use Docker

##
