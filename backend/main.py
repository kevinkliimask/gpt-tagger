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
async def get_tags(file: UploadFile, count: int = 5):
    if file.content_type != "text/csv":
        raise HTTPException(status_code=415, detail="Unsupported content-type")

    return await handle_tagging(file, count)
