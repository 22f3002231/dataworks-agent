from fastapi import FastAPI, HTTPException
import os
import subprocess
from pathlib import Path

app = FastAPI()

# Security validation
def validate_path(path: str):
    resolved = Path(path).resolve()
    if not str(resolved).startswith('/data'):
        raise HTTPException(400, "Path access violation")

@app.post("/run")
async def run_task(task: str):
    try:
        # Task handling logic here
        return {"status": "Task completed"}
    except Exception as e:
        raise HTTPException(500, str(e))

@app.get("/read")
async def read_file(path: str):
    validate_path(path)
    if not Path(path).exists():
        raise HTTPException(404)
    return {"content": Path(path).read_text()}
