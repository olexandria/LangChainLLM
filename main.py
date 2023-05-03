import os

from fastapi import FastAPI

from LLM import load_documents, get_answer
from message import add_message
from schemas import Message, RequestModel

os.environ["OPENAI_API_KEY"] = "your_api_key_here"

app = FastAPI()
documents = load_documents()


@app.post("/add_message")
async def create_message(message: Message):
    return add_message(message, documents)


@app.post("/ask")
async def ask_question(request: RequestModel):
    result = get_answer(request.question, documents)
    return {"Q:": request.question, "A:": result}
