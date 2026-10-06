from fastapi import FastAPI, UploadFile, File
import pytesseract
from PIL import Image
import io

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ocr")
async def ocr(file: UploadFile = File(...)):
    data = await file.read()

    image = Image.open(io.BytesIO(data))

    text = pytesseract.image_to_string(
        image,
        lang="eng"
    )

    return {
        "text": text
    }
