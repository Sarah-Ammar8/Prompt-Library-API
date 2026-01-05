from fastapi import FastAPI
from src.api.routes.health import router as health_router
from src.api.routes.prompts import build_prompts_router
from src.storage.memory_store import MemoryStore
from src.services.prompts_service import PromptsService

app = FastAPI(title="Prompt Library API")

# wiring (composition root)
store = MemoryStore()
prompts_service = PromptsService(store)

# routes
app.include_router(health_router)
app.include_router(build_prompts_router(prompts_service))
