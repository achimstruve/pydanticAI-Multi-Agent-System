from pydantic import BaseModel
from .system_prompt import system_prompt
from src.agents.multiagent import MultiAgent

class ResponseModel(BaseModel):
    """Structured response with metadata"""

    secret_number: int

SecretNumberAgent = MultiAgent(
    name="secret_number_agent",
    model="openai:gpt-4o",
    system_prompt=system_prompt,
    result_type=ResponseModel
)

