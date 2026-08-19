from fastapi import FastAPI
from app.api import chat, documents, health

app = FastAPI(title="RAG Chatbot API", version="0.1.0")

app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])
app.include_router(documents.router, prefix="/documents", tags=["documents"])
