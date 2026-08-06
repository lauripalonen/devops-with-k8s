from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
import httpx2

str_file_path = Path('/usr/src/app/files/logs.txt')
str_file_path.parent.mkdir(exist_ok=True, parents=True)

#pongs_file_path = Path('/usr/src/app/files/pongs.txt')
#pongs_file_path.parent.mkdir(exist_ok=True, parents=True)

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
       async with httpx2.AsyncClient() as client:
            response = await client.get("http://pingpong-svc:2345/pings")
            pong_count = response.text.strip()
    except Exception as e:
        pong_count = f"Error fetching pong count: {e}"


    html_content = f"""
    <html>
        <body>
            <p>{timestamp_str}</p>
            <p>Ping / Pongs: {pong_count}</p>
        </body>
    </html>
    """

    return HTMLResponse(content=html_content, status_code=200)