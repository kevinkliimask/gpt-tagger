from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware

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

@app.post("/")
async def get_tags(file: UploadFile, count: int = 5, model: str = "gpt-3.5-turbo"):
    if file.content_type != "text/csv":
        raise HTTPException(status_code=415, detail="Unsupported content-type")
    if not 3 <= count <= 10:
        raise HTTPException(status_code=400, detail="Count must be between 3 and 10")
    if not model in ["gpt-3.5-turbo", "gpt-4"]:
        raise HTTPException(status_code=400, detail="Model must be gpt-3.5-turbo or gpt-4")

    return await handle_tagging(file, count, model)
