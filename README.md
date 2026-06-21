# FASTAPI-CRUD-SIMPLE-PROJECT
A simple fastapi project demonstrating GET, POST,PUT,PATCH ,and DELETE HTTP methods.

## Features
- Create data
- Read data
- Update data
- Delete data
- Interactive API documentation with Swagger UI

## Tech Stack
- Python
- FastAPI
- Uvicorn

## Run Locally

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

## API Docs

Swagger UI:
http://127.0.0.1:8000/docs

## Note

This project uses in-memory data storage. Data will be reset whenever the server is restarted.
