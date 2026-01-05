import uuid
from sqlalchemy import text
from app.db.session import engine
from app.services.chunking_service import ChunkingService
from app.services.embedding_service import EmbeddingService


class IngestionService:
    def __init__(self):
        self.chunking_service = ChunkingService()
        self.embedding_service = EmbeddingService()

    def ingest_document(self, title: str, content: str):
        doc_id = uuid.uuid4()

        chunks = self.chunking_service.chunk_text(content)
        embeddings = self.embedding_service.embed_text(chunks)

        with engine.begin() as conn:
            # Insert document
            conn.execute(
                text("""
                INSERT INTO documents (id, title, content)
                VALUES (:id, :title, :content)
                """),
                {"id": doc_id, "title": title, "content": content}
            )

            # Insert embeddings
            for chunk, embedding in zip(chunks, embeddings):
                conn.execute(
                    text("""
                    INSERT INTO document_embeddings
                    (id, document_id, chunk_text, embedding)
                    VALUES (:id, :document_id, :chunk_text, :embedding)
                    """),
                    {
                        "id": uuid.uuid4(),
                        "document_id": doc_id,
                        "chunk_text": chunk,
                        "embedding": embedding
                    }
                )
        return {"document_id": str(doc_id), "num_chunks": len(chunks)}