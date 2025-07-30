from fastapi import FastAPI
from app.routes import rag_routes
# api entrypoint
app = FastAPI()

app.include_router(rag_routes.router, prefix="/rag")
