from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# FastAPI app instance
app = FastAPI()

# Allow frontend (Streamlit) to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a request model
class Message(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "FastAPI backend is running!"}

@app.post("/process")
def process_message(msg: str):
    response = f"Hello! You said: {msg.upper()}"
    return {"response": response}


@app.post("/chat")
def chat_endpoint(query: Message):
    from query import RAGSearch
    rag_search = RAGSearch("../vector_store/")
    answer = rag_search.search_and_summarize(query.text, top_k=5)
    return {"response": answer}


@app.post("/uppercase")
def convert_to_uppercase(msg: Message):
    upper_text = msg.text.upper()
    return {"result": upper_text}



# run app
# uvicorn main:app --reload --port 8000