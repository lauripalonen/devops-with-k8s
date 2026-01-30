from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

str_file_path = Path('/usr/src/app/files/logs.txt')
str_file_path.parent.mkdir(exist_ok=True, parents=True)

pongs_file_path = Path('/usr/src/app/files/pongs.txt')
pongs_file_path.parent.mkdir(exist_ok=True, parents=True)

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    timestamp_str = ""
    pong_count = ""

    try:
        timestamp_str = str_file_path.read_text().strip()
    except FileNotFoundError:
        timestamp_str = "No log data available."

    try:
        pong_count = pongs_file_path.read_text().strip()
    except FileNotFoundError:
        pong_count = "Pongs: 0"


    html_content = f"""
    <html>
        <body>
            <p>{timestamp_str}</p>
            <p>{pong_count}</p>
        </body>
    </html>
    """

    return HTMLResponse(content=html_content, status_code=200)