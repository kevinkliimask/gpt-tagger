from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from openai_service import handle_tagging
from config import Settings

settings = Settings()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url],
    allow_methods=["POST"],
    allow_headers=["*"],
)

class Data(BaseModel):
    data: List[List[str]]

@app.post("/")
async def get_tags(data: Data, count: int = 5, model: str = "gpt-3.5-turbo"):
    if len(data.data) > 10:
        raise HTTPException(status_code=400, detail="Data length must be a maximum of 10 lines")
    if not 3 <= count <= 10:
        raise HTTPException(status_code=400, detail="Count must be between 3 and 10")
    if not model in ["gpt-3.5-turbo", "gpt-4"]:
        raise HTTPException(status_code=400, detail="Model must be gpt-3.5-turbo or gpt-4")

    return await handle_tagging(data.data, count, model)
