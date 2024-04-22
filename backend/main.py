from fastapi import FastAPI, UploadFile, HTTPException

from openai_service import handle_tagging


app = FastAPI()

@app.post("/")
async def get_tags(file: UploadFile, count: int = 5):
    if file.content_type != "text/csv":
        raise HTTPException(status_code=415, detail="Unsupported content-type")

    return await handle_tagging(file, count)
