from sqlalchemy import text
from app.db.session import engine
from app.services.embedding_service import EmbeddingService


class RetrievalService:
    def __init__(self):
        self.embedder = EmbeddingService()

    def retrieve(self, query: str, top_k: int = 3) -> list[str]:
        query_embedding = self.embedder.embed_text([query])[0]

        with engine.connect() as conn:
            results = conn.execute(
                text("""
                    SELECT chunk_text
                    FROM document_embeddings
                    ORDER BY embedding <-> (:query_embedding)::vector(3072)
                    LIMIT :top_k
                """),
                {
                    "query_embedding": query_embedding,
                    "top_k": top_k
                }
            ).fetchall()

        return [row[0] for row in results]
