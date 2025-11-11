from pathlib import Path
from typing import List, Any
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader


class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def document_loader(self) -> List[Any]:
        """
        Reads all the PDF and DOCX files from file_path and returns a list of documents.
        """
        file_path = Path(self.file_path).resolve()
        print(f"[INFO] Loading documents from: {file_path}")
        documents = []

        # --- Load PDF Files ---
        pdf_files = list(file_path.glob("**/*.pdf"))
        print(f"[INFO] Found {len(pdf_files)} PDF files.")

        for pdf_file in pdf_files:
            try:
                loader = PyPDFLoader(str(pdf_file))
                loaded = loader.load()
                print(f"[INFO] Loaded {len(loaded)} pages from {pdf_file.name}")
                documents.extend(loaded)
            except Exception as e:
                print(f"[ERROR] Failed to load {pdf_file.name}: {e}")
                raise

        # --- Load DOCX Files ---
        docx_files = list(file_path.glob("**/*.docx"))
        print(f"[INFO] Found {len(docx_files)} DOCX files.")

        for docx_file in docx_files:
            try:
                loader = Docx2txtLoader(str(docx_file))
                loaded = loader.load()
                print(f"[INFO] Loaded {len(loaded)} pages from {docx_file.name}")
                documents.extend(loaded)
            except Exception as e:
                print(f"[ERROR] Failed to load {docx_file.name}: {e}")
                raise

        return documents
