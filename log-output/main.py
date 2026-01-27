import datetime
import uuid
import asyncio
import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse

logger = logging.getLogger("uvicorn.error")
logs = []

async def log_task():
    while True:
        curr_time = datetime.datetime.now().isoformat()
        output_str = uuid.uuid4()
        log = f"{curr_time}: {output_str}"
        logs.append(log)
        logger.info(log)
        await asyncio.sleep(5)

@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(log_task())
    yield
    task.cancel()

app = FastAPI(lifespan=lifespan)

@app.get("/", response_class=HTMLResponse)
async def root():
    return logs[-1] if logs else "No logs yet"