from langgraph.graph import StateGraph, END
from app.agents.state import AgentState
from app.agents.decision import decide_action
from app.agents.tools import rag_tool, email_draft_tool, task_creation_tool


def build_agent():
    graph = StateGraph(AgentState)

    # Nodes
    graph.add_node("decide", decide_action)
    graph.add_node("rag", rag_tool)
    graph.add_node("email", email_draft_tool)
    graph.add_node("task", task_creation_tool)

    # Flow
    graph.set_entry_point("decide")

    graph.add_conditional_edges(
        "decide",
        lambda state: state["action"],
        {
            "rag": "rag",
            "email": "email",
            "task": "task"
        }
    )

    graph.add_edge("rag", END)
    graph.add_edge("email", END)
    graph.add_edge("task", END)

    return graph.compile()
