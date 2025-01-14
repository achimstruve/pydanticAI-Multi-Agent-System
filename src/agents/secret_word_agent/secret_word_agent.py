from pydantic_ai import Agent
from pydantic import BaseModel
from .system_prompt import system_prompt

class ResponseModel(BaseModel):
    """Structured response with metadata"""

    secret_word: str

SecretWordAgent = Agent(
    name="secret_word_agent",
    model="openai:gpt-4o",
    system_prompt=system_prompt,
    result_type=ResponseModel
)

