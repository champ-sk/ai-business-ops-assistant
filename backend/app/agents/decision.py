from app.services.llm_service import LLMService


def decide_action(state):
    llm = LLMService()

    prompt = f"""
You are an AI assistant that decides what action to take.

Available actions:
- rag : if the user asks a question about stored documents
- email : if the user wants to draft an email
- task : if the user wants to create a task

User input:
{state['user_input']}

Respond with only one word: rag, email, or task.
"""

    action = llm.simple_chat(prompt).strip().lower()

    if action not in ["rag", "email", "task"]:
        action = "rag"

    return {"action": action}
