from app.services.llm_service import LLMService
from app.services.retrieval_service import RetrievalService


class RAGService:
    def __init__(self):
        self.retriever = RetrievalService()
        self.llm = LLMService()

    def answer(self, question: str) -> str:
        contexts = self.retriever.retrieve(question)

        if not contexts:
            return "No relevant information found in the documents."

        context_text = "\n\n".join(contexts)

        prompt = f"""
You are an assistant that answers questions strictly using the provided context.
If the answer is not in the context, say "I don't know".

Context:
{context_text}

Question:
{question}

Answer:
"""

        return self.llm.simple_chat(prompt)
