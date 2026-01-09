from app.services.rag_service import RAGService


def rag_tool(state):
    question = state["user_input"]
    rag = RAGService()
    result = rag.answer(question)

    return {
        "response": result["answer"]
    }


def email_draft_tool(state):
    prompt = state["user_input"]

    return {
        "response": f"(Email draft generated for: {prompt})"
    }


def task_creation_tool(state):
    task = state["user_input"]

    return {
        "response": f"(Task created successfully for: {task})"
    }
