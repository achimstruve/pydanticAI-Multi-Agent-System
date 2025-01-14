from pydantic_ai import RunContext, Agent
from typing import Any, Dict
from .system_prompt import system_prompt
import json
from src.utils import TaskResult
from src.tools.agent_delegation import delegate_task_logic
from src.tools.planning import planning_logic
from src.utils import initialize_delegation_agents
from src.agents.task_manager_agent.task_manager_agent import TaskManagerAgent
from src.agents.result_handler_agent.result_handler_agent import ResultHandlerAgent


# Define the main agent
DirectorAgent = Agent(
    name="director_agent",
    model="openai:gpt-4o",
    system_prompt=system_prompt,
    result_type=TaskResult
)

# initialize the delegation agents
agent_registry = initialize_delegation_agents([TaskManagerAgent, ResultHandlerAgent])

# add the delegate_task tool to the director agent
@DirectorAgent.tool
async def delegate_task(
    ctx: RunContext[Dict[str, str]],
    task_description: str,
    preferred_agent: str
) -> TaskResult:
    return await delegate_task_logic(ctx, task_description, preferred_agent, agent_registry)

# add the planning tool to the director agent
@DirectorAgent.tool
async def planning(ctx: RunContext[Any], task_description: str) -> str:
    return await planning_logic(ctx, task_description)



