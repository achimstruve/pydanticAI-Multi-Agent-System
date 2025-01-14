from pydantic_ai import Agent
from .system_prompt import system_prompt

ResultHandlerAgent = Agent(
    name="result_handler_agent",
    model="openai:gpt-4o",
    system_prompt=system_prompt,
    result_type=str
)

