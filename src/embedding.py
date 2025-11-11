from typing import List, Any
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingManager:
    def __init__(self, embedding_model: str = "all-MiniLM-L6-v2", chunk_size: int= 1000, chunk_overlap: int= 200):
        self.embedding_model = SentenceTransformer(embedding_model)
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        print(f"[INFO] Using embedding model: {embedding_model}")

    def chunk_text(self, document: str) -> List[str]:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size, 
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""])
        texts = text_splitter.split_documents(document)
        print(f"[INFO] Split document into {len(texts)} chunks.")
        return texts
    
    def embed_chunks(self, chunks: List[Any]) -> np.ndarray:
        texts = [chunk.page_content for chunk in chunks]
        print(f"[INFO] Generating embeddings for {len(texts)} chunks...")
        embeddings = self.embedding_model.encode(texts, show_progress_bar=True)
        print(f"[INFO] Embeddings shape: {embeddings.shape}")
        return embeddings
