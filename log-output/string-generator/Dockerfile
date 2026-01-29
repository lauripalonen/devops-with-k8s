FROM ghcr.io/astral-sh/uv:alpine

WORKDIR /usr/src/app

COPY . /usr/src/app

ENV UV_NO_DEV=1

ENV PYTHONUNBUFFERED=1

RUN uv sync --locked

CMD ["uv", "run", "main.py"]