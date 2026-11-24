import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
import httpx2

str_log_file_path = Path('/usr/src/app/files/logs.txt')
str_log_file_path.parent.mkdir(exist_ok=True, parents=True)

str_information_file_path = Path('/usr/src/app/files/information.txt')
str_information_file_path.parent.mkdir(exist_ok=True, parents=True)

#pongs_file_path = Path('/usr/src/app/files/pongs.txt')
#pongs_file_path.parent.mkdir(exist_ok=True, parents=True)

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    information_str = ""
    msg_env = os.getenv("MESSAGE", "MESSAGE env variable not set.") 
    timestamp_str = ""
    pong_count = ""

    try:
        timestamp_str = str_log_file_path.read_text().strip()
        information_str = str_information_file_path.read_text().strip()
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
            <p>file content: {information_str}</p>
            <p>env variable: {msg_env}</p>
            <p>{timestamp_str}</p>
            <p>Ping / Pongs: {pong_count}</p>
        </body>
    </html>
    """

    return HTMLResponse(content=html_content, status_code=200)