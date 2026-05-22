
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.scheduler import start_scheduler

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_scheduler()   # runs only once, not on reloader process
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def home():
    return {"message": "AI Job Agent Running ✅"}
