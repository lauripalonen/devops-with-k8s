from fastapi import FastAPI
from pathlib import Path

app = FastAPI()

file_path = Path('/usr/src/app/files/pongs.txt')
file_path.parent.mkdir(exist_ok=True, parents=True)

class Pongs:
    def __init__(self):
        self.count = 0

pongs = Pongs()

@app.get("/pingpong")
async def ping():
    pongs.count += 1
    with open(file_path, "w") as f:
        f.write(f'Pongs: {pongs.count}')
    return f"pong {pongs.count}"