from fastapi import APIRouter
from src.schemas.prompts import PromptCreate
from src.storage.memory_store import MemoryStore
from src.services.prompts_service import PromptsService

router = APIRouter(prefix="/prompts", tags=["prompts"])

store = MemoryStore()
service = PromptsService(store)


@router.get("")
def list_prompts():
    return {"data": service.list_prompts(), "error": None}


@router.post("", status_code=201)
def create_prompt(payload: PromptCreate):
    item = service.create_prompt(payload)
    return {"data": item, "error": None}
