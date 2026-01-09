from typing import TypedDict, Optional


class AgentState(TypedDict):
    user_input: str
    action: Optional[str]
    response: Optional[str]
