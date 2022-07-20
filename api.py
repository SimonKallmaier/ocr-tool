
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
async def say_hello():
    return {"greeting": "Hello!"}