# Prompt Library API
A clean RESTful backend service for managing reusable AI prompt templates, demonstrating structured API design, validation, and Dockerized execution.
A minimal FastAPI backend that manages a simple in-memory Prompt Library (list/create), built incrementally with a clean folder structure: routes → schemas → services → storage.

## Features (current)
- Health check endpoint
- Prompts:
  - List prompts
  - Create prompt (validated)
- Unified error responses (consistent `data/error` envelope)

## Tech Stack
- Python
- FastAPI
- Uvicorn


## Project Structure

Prompt-Library-API/
├─ src/
│  ├─ main.py                 # Application entry point (composition root)
│  ├─ api/
│  │  ├─ errors.py             # Global error handlers (unified responses)
│  │  └─ routes/
│  │     ├─ health.py          # GET /health
│  │     └─ prompts.py         # /prompts routes (HTTP only; calls service)
│  ├─ schemas/
│  │  └─ prompts.py            # Pydantic request models (validation)
│  ├─ services/
│  │  └─ prompts_service.py    # Business logic (list/create)
│  └─ storage/
│     └─ memory_store.py       # In-memory store (prompts, next_id)
├─ requirements.txt
└─ README.md

## Why this structure?

routes/: HTTP concerns only (request/response, status codes)
schemas/: validation models (Pydantic) separated from routing
services/: business logic (clean and testable)
storage/: data storage abstraction (currently in-memory, replaceable later)
main.py: wiring/composition root (builds services and mounts routers)


## Setup & Run (Windows)
1) Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate

2) Install dependencies
pip install -r requirements.txt

3) Run the server
uvicorn src.main:app --reload --port 8000
Open:
Swagger UI: http://127.0.0.1:8000/docs
Health: http://127.0.0.1:8000/health


## API Endpoints

# Health
GET /health
Response:
{"data":{"status":"ok"},"error":null}

# Prompts
List prompts
GET /prompts
Response:
{"data":[],"error":null}

# Create prompt
POST /prompts
Request body:
{
  "title": "My Prompt",
  "content": "Write a short summary about ..."
}
Response (201):
{
  "data": {
    "id": 1,
    "title": "My Prompt",
    "content": "Write a short summary about ..."
  },
  "error": null
}

# Error Response Format (Unified)
All errors return a consistent envelope:
{
  "data": null,
  "error": {
    "message": "Validation failed",
    "details": []
  }
}
Example: send an invalid POST body to /prompts (missing required fields) and check the response in Swagger.

## Notes / Next Improvements
Add GET /prompts/{id}, PATCH, DELETE
Persist data using a database (SQLite/Postgres)
Add tests for services and routes
Add Docker setup
