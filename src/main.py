from fastapi import FastAPI
from src.api.routes.health import router as health_router
from src.api.routes.prompts import router as prompts_router

app = FastAPI(title="Prompt Library API")

app.include_router(health_router)
app.include_router(prompts_router)
