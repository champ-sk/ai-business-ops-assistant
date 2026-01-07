from app.services.llm_service import LLMService
from app.services.retrieval_service import RetrievalService


class RAGService:
    def __init__(self):
        self.retriever = RetrievalService()
        self.llm = LLMService()

    def answer(self, question: str) -> str:
        contexts = self.retriever.retrieve(question)

        if not contexts:
            return {
                "answer": "I don't know based on the available documents.",
                "sources": []
            }
        context_text = "\n\n".join( f"[Source: {item['title']}]\n{item['chunk']}"
            for item in contexts)

        prompt = f"""
You are an assistant that answers questions strictly using the provided context.
If the answer is not in the context, say "I don't know".

Context:
{context_text}

Question:
{question}

Answer:
"""

        answer =  self.llm.simple_chat(prompt)
        sources = list({item["title"] for item in contexts})

        return {
            "answer": answer,
            "sources": sources
        }



