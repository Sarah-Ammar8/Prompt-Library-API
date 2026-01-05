from fastapi import APIRouter
from src.schemas.prompts import PromptCreate
from src.services.prompts_service import PromptsService


def build_prompts_router(service: PromptsService) -> APIRouter:
    router = APIRouter(prefix="/prompts", tags=["prompts"])

    @router.get("")
    def list_prompts():
        return {"data": service.list_prompts(), "error": None}

    @router.post("", status_code=201)
    def create_prompt(payload: PromptCreate):
        item = service.create_prompt(payload)
        return {"data": item, "error": None}

    return router
