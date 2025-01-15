from src.agents.multiagent import MultiAgent
from .system_prompt import system_prompt

ResultHandlerAgent = MultiAgent(
    name="result_handler_agent",
    model="openai:gpt-4o",
    system_prompt=system_prompt,
    result_type=str
)

