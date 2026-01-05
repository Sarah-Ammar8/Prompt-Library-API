from fastapi import FastAPI

app = FastAPI(title="Prompt Library API")

@app.get("/health")
def health():
    return {"data": {"status": "ok"}, "error": None}
