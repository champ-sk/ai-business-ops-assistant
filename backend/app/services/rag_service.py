from app.services.llm_service import LLMService
from app.services.retrieval_service import RetrievalService
from app.services.memory_service import MemoryService
from app.core.logging import get_logger

logger = get_logger(__name__)

class RAGService:
    def __init__(self):
        self.retriever = RetrievalService()
        self.llm = LLMService()
        self.memory = MemoryService()

    def answer(self, question: str):

        logger.info("Received question: %s", question)

        # 1. Retrieve recent conversation history
        history = self.memory.get_recent()

        history_text = "\n".join(
            f"User: {h['question']}\nAssistant: {h['answer']}"
            for h in reversed(history)
        )

        # 2. Retrieve relevant document chunks
        contexts = self.retriever.retrieve(question)
        logger.info("Retrieved %d context chunks", len(contexts))

        if not contexts:
            answer = "I don't know based on the available documents."
            self.memory.save(question, answer)
            return {
                "answer": answer,
                "sources": []
            }

        context_text = "\n\n".join(
            f"[Source: {item['title']}]\n{item['chunk']}"
            for item in contexts
        )

        # 3. Build prompt with memory + context
        prompt = f"""
You are an assistant that answers questions strictly using the provided context.
Use conversation history only to resolve references like he, she, it, or they.
If the answer is not present in the context, say "I don't know".

Conversation history:
{history_text}

Context:
{context_text}

Question:
{question}

Answer:
"""

        # 4. Generate answer
        answer = self.llm.simple_chat(prompt)

        # 5. Save conversation to memory
        self.memory.save(question, answer)

        # 6. Extract unique source titles
        sources = list({item["title"] for item in contexts})
        
        logger.info("Generated answer with %d sources", len(sources))

        return {
            "answer": answer,
            "sources": sources
        }
