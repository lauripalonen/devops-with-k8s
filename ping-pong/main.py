import os
import time
from contextlib import asynccontextmanager

import psycopg
from fastapi import FastAPI


def connect_to_database():
    return psycopg.connect(
        host=os.environ.get("POSTGRES_HOST", "localhost"),
        port=os.environ.get("POSTGRES_PORT", "5432"),
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        connect_timeout=3,
    )


def initialize_database():
    for attempt in range(15):
        try:
            with connect_to_database() as connection:
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS ping_counter (
                        id SMALLINT PRIMARY KEY CHECK (id = 1),
                        ping_count BIGINT NOT NULL
                    )
                    """
                )
                connection.execute(
                    """
                    INSERT INTO ping_counter (id, ping_count)
                    VALUES (1, 0)
                    ON CONFLICT (id) DO NOTHING
                    """
                )
            return
        except psycopg.OperationalError:
            if attempt == 14:
                raise
            time.sleep(2)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    initialize_database()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/pingpong")
def ping():
    with connect_to_database() as connection:
        result = connection.execute(
            """
            UPDATE ping_counter
            SET ping_count = ping_count + 1
            WHERE id = 1
            RETURNING ping_count
            """
        ).fetchone()
    if result is None:
        raise RuntimeError("PostgreSQL did not return the updated ping count")
    return f"pong {result[0]}"


@app.get("/pings")
def pings():
    with connect_to_database() as connection:
        result = connection.execute(
            "SELECT ping_count FROM ping_counter WHERE id = 1"
        ).fetchone()
    if result is None:
        raise RuntimeError("PostgreSQL did not return the ping count")
    return result[0]