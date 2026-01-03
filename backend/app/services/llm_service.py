from langchain_openai import ChatOpenAI
from app.core.config import settings


class LLMService:
    def __init__(self):
        self.llm = ChatOpenAI(
            model=settings.OPENAI_CHAT_MODEL,
            temperature=0.2
        )

    def simple_chat(self, message: str) -> str:
        response = self.llm.invoke(message)
        return response.content
