from langchain_openai import ChatOpenAI
from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger(__name__)


class LLMService:
    def __init__(self):
        self.llm = ChatOpenAI(
            model=settings.OPENAI_CHAT_MODEL,
            temperature=0.2
        )

    def simple_chat(self, message: str) -> str:
        try:
            response = self.llm.invoke(message)
            return response.content
        except Exception as e:
            logger.error("LLM error: %s", str(e))
            return "Sorry, Internal error encountered."
        
