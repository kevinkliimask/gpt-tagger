from fastapi import FastAPI, UploadFile, HTTPException

from chatgpt_service import handle_tagging

app = FastAPI()

@app.post("/")
async def get_tags(file: UploadFile):
    if file.content_type != "text/csv":
        raise HTTPException(status_code=415, detail="Unsupported content-type")

    tags = await handle_tagging(file)
    return {"tags": tags}
