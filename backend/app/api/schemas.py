from pydantic import BaseModel

class IngestRequest(BaseModel):
    title: str
    content: str
