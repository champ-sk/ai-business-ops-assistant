import uuid
from sqlalchemy import text
from app.db.session import engine


class MemoryService:
    def save(self, question: str, answer: str):
        with engine.begin() as conn:
            conn.execute(
                text("""
                    INSERT INTO conversations (id, question, answer)
                    VALUES (:id, :question, :answer)
                """),
                {
                    "id": uuid.uuid4(),
                    "question": question,
                    "answer": answer
                }
            )

    def get_recent(self, limit: int = 5):
        with engine.connect() as conn:
            rows = conn.execute(
                text("""
                    SELECT question, answer
                    FROM conversations
                    ORDER BY created_at DESC
                    LIMIT :limit
                """),
                {"limit": limit}
            ).fetchall()

        return [
            {"question": r[0], "answer": r[1]}
            for r in rows
        ]
