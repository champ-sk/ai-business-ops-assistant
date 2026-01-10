import uuid
from sqlalchemy import text
from app.db.session import engine

class UsageService:
    def log(self, tokens: int, cost_usd: float):
        with engine.begin() as conn:
            conn.execute(
                text("""
                    INSERT INTO llm_usage (id, tokens, cost_usd)
                    VALUES (:id, :tokens, :cost)
                """),
                {
                    "id": uuid.uuid4(),
                    "tokens": tokens,
                    "cost": cost_usd
                }
            )
