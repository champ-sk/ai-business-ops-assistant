from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)#Engine is the actual connection point to your database.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
