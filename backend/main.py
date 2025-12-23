from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.api.chat import router as chat_router
from app.db.session import engine
from app.db.models import Base

app = FastAPI(title="Spur AI Live Chat")

Base.metadata.create_all(bind=engine)

app.include_router(chat_router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse("app/static/index.html")
