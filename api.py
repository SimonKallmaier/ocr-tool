import os

from fastapi import FastAPI
from pydantic import BaseModel, BaseSettings

from src.ocr_tool import OcrTextExtractor


class Path(BaseModel):
    path: str

class Settings(BaseSettings):
    GOOGLE_APPLICATION_CREDENTIALS: str = "/home/simon/.keys/ocr-tool-356915-1efb434cb118.json"


settings = Settings()
app = FastAPI()


@app.get("/")
async def say_hello():
    return {"greeting": "Hello"}


@app.post("/image/")
async def ocr_result(path: Path):
    ocr_text_extractor = OcrTextExtractor(path=path.path)
    ocr_text = ocr_text_extractor.run()
    return {"text": ocr_text}
