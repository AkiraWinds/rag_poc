from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(title="RAG PoC")

app.include_router(router)
