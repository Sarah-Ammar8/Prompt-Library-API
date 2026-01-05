from src.schemas.prompts import PromptCreate
from src.storage.memory_store import MemoryStore


class PromptsService:
    def __init__(self, store: MemoryStore):
        self.store = store

    def list_prompts(self):
        return self.store.prompts

    def create_prompt(self, payload: PromptCreate):
        item = {"id": self.store.next_id, "title": payload.title, "content": payload.content}
        self.store.prompts.append(item)
        self.store.next_id += 1
        return item
