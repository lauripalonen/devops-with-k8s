from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

class Pongs:
    def __init__(self):
        self.count = 0

pongs = Pongs()

@app.get("/pingpong")
async def ping():
    pongs.count += 1
    return f"pong {pongs.count}"