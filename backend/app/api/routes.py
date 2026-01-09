from fastapi import APIRouter
from app.services.llm_service import LLMService
from app.api.schemas import IngestRequest
from app.services.ingestion_service import IngestionService
from app.services.rag_service import RAGService
from app.api.schemas import QuestionRequest
from app.agents.graph import build_agent





router = APIRouter(prefix="/api")

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/test-llm")
def test_llm(prompt: str):
    llm = LLMService()
    output = llm.simple_chat(prompt)
    return {"response": output}

@router.post("/ingest")
def ingest_document(request: IngestRequest):
    ingestion_service = IngestionService()
    result = ingestion_service.ingest_document(title = request.title, content=request.content)
    return result



@router.post("/ask")
def ask_question(request: QuestionRequest):
    rag = RAGService()
    answer = rag.answer(request.question)
    return {"answer": answer}



@router.post("/agent")
def agent_entry(request: QuestionRequest):
    agent = build_agent()

    state = {
        "user_input": request.question,
        "action": None,
        "response": None
    }

    result = agent.invoke(state)

    return {
        "action": result.get("action"),
        "response": result.get("response")
    }
