# OCR Service

A simple OCR API built with **FastAPI**, **Tesseract OCR**, and **Docker**.

## Requirements

* Docker
* Docker Compose

## Run

```bash
docker compose up -d --build
```

The API runs on:

```text
http://localhost:8000
```

## API

### Health check

```bash
curl http://localhost:8000/health
```

### OCR

Send an image to `/ocr`:

```bash
curl -X POST \
  -F "file=@image.jpg" \
  http://localhost:8000/ocr
```

Response:

```json
{
  "text": "Extracted text..."
}
```

## License

MIT
