from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/prompts", tags=["prompts"])

# تخزين مؤقت في الذاكرة (مؤقتًا)
_PROMPTS = []
_NEXT_ID = 1


class PromptCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    content: str = Field(min_length=1, max_length=10000)


@router.get("")
def list_prompts():
    return {"data": _PROMPTS, "error": None}


@router.post("", status_code=201)
def create_prompt(payload: PromptCreate):
    global _NEXT_ID
    item = {"id": _NEXT_ID, "title": payload.title, "content": payload.content}
    _PROMPTS.append(item)
    _NEXT_ID += 1
    return {"data": item, "error": None}
