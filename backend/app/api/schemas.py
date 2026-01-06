from pydantic import BaseModel

class IngestRequest(BaseModel):
    title: str
    content: str

class QuestionRequest(BaseModel):
    question: str

