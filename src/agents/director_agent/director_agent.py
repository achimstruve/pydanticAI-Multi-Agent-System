from pydantic_ai import RunContext
from typing import Any, Dict
from .system_prompt import system_prompt

from src.agents.multiagent import MultiAgent
from src.utils import TaskResult
from src.tools.agent_delegation import delegate_task_logic
from src.tools.planning import planning_logic

# Define the main agent
DirectorAgent = MultiAgent(
    name="director_agent",
    model="openai:gpt-4o",
    system_prompt=system_prompt,
    result_type=TaskResult
)

# add the delegate_task tool to the director agent
@DirectorAgent.tool
async def delegate_task(
    ctx: RunContext[Dict[str, str]],
    task_description: str,
    preferred_agent: str
) -> TaskResult:
    return await delegate_task_logic(DirectorAgent, ctx, task_description, preferred_agent)

# add the planning tool to the director agent
@DirectorAgent.tool
async def planning(ctx: RunContext[Any], task_description: str) -> str:
    return await planning_logic(ctx, task_description)



