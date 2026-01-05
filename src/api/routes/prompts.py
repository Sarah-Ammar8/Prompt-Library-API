from fastapi import APIRouter
from src.schemas.prompts import PromptCreate
from src.storage.memory_store import MemoryStore

router = APIRouter(prefix="/prompts", tags=["prompts"])

store = MemoryStore()


@router.get("")
def list_prompts():
    return {"data": store.prompts, "error": None}


@router.post("", status_code=201)
def create_prompt(payload: PromptCreate):
    item = {"id": store.next_id, "title": payload.title, "content": payload.content}
    store.prompts.append(item)
    store.next_id += 1
    return {"data": item, "error": None}
