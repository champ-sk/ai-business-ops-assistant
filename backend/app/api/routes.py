from fastapi import APIRouter
from app.services.llm_service import LLMService


router = APIRouter(prefix="/api")

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/test-llm")
def test_llm(prompt: str):
    llm = LLMService()
    output = llm.simple_chat(prompt)
    return {"response": output}
