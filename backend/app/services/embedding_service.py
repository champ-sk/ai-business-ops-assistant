from langchain_openai.embeddings import OpenAIEmbeddings
from app.core.config import settings


class EmbeddingService:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(model = settings.OPENAI_EMBEDDING_MODEL)

    def embed_text(self, text:list[str]) -> list[list[float]]:
        return self.embeddings.embed_documents(text)     