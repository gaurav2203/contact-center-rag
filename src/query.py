import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from vector_store import FaissVectorStore
from data_loader import DataLoader

load_dotenv("../.env")
OLLAMA_API_KEY= os.getenv("OLLAMA_API_KEY")


class RAGSearch:
    def __init__(self, persist_dir: str = "../vector_store", embedding_model: str = "all-MiniLM-L6-v2", llm_model: str = "llama2"):
        self.vectorstore = FaissVectorStore(persist_dir, embedding_model)
        # Load or build vectorstore
        faiss_path = os.path.join(persist_dir, "faiss.index")
        meta_path = os.path.join(persist_dir, "metadata.pkl")
        if not (os.path.exists(faiss_path) and os.path.exists(meta_path)):
            # from data_loader import load_all_documents
            docs = DataLoader.document_loader("data")
            self.vectorstore.build_from_documents(docs)
        else:
            self.vectorstore.load()
        self.llm = ChatOllama(OLLAMA_API_KEY=OLLAMA_API_KEY, model=llm_model)
        print(f"[INFO] OLLAMA LLM initialized: {llm_model}")

    def search_and_summarize(self, query: str, top_k: int = 5) -> str:
        results = self.vectorstore.query(query, top_k=top_k)
        texts = [r["metadata"].get("text", "") for r in results if r["metadata"]]
        context = "\n\n".join(texts)
        if not context:
            return "No relevant documents found."
        prompt= f"""
                You are a helpful customer support agent. 
                Your goal is to answer the user's question using the provided context and nothing else:
                '{query}'\n\nContext:\n{context}\n\nAnswer:
            """
        response = self.llm.invoke([prompt])
        return response.content
