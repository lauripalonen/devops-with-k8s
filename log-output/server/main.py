from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.responses import FileResponse
from pathlib import Path

file_path = Path('/usr/src/app/files/logs.txt')
file_path.parent.mkdir(exist_ok=True, parents=True)

app = FastAPI()

@app.get("/", response_class=FileResponse)
async def root():
    return FileResponse(path=file_path, media_type="text/plain")