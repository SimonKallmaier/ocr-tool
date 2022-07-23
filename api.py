import logging
import os

from fastapi import FastAPI
from pydantic import BaseModel, BaseSettings

from src.ocr_tool import OcrTextExtractor

logging.basicConfig(level=logging.INFO)


class Path(BaseModel):
    path: str

class Settings(BaseSettings):
    GOOGLE_APPLICATION_CREDENTIALS: str = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")


settings = Settings()
app = FastAPI()


@app.get("/")
async def say_hello():
    logging.info("greeting")
    return {"greeting": "Hello"}


@app.post("/image/")
async def ocr_result(path: Path):
    ocr_text_extractor = OcrTextExtractor(path=path.path)
    ocr_text = ocr_text_extractor.run()
    logging.info(f"Ocr text: {ocr_text}")
    return {"text": ocr_text}
