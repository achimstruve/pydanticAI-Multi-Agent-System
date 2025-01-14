from pydantic_ai import RunContext, Agent
from typing import Any, Dict
from .system_prompt import system_prompt
import json
from src.utils import TaskResult
from src.tools.agent_delegation import delegate_task_logic
from src.tools.planning import planning_logic
from src.utils import initialize_delegation_agents
from src.agents.secret_number_agent.secret_number_agent import SecretNumberAgent
from src.agents.secret_word_agent.secret_word_agent import SecretWordAgent

# Define the main agent
TaskManagerAgent = Agent(
    name="task_manager_agent",
    model="openai:gpt-4o",
    system_prompt=system_prompt,
    result_type=TaskResult
)

# initialize the delegation agents
agent_registry = initialize_delegation_agents([SecretNumberAgent, SecretWordAgent])

# add the delegate_task tool to the task manager agent
@TaskManagerAgent.tool
async def delegate_task(
    ctx: RunContext[Dict[str, str]],
    task_description: str,
    preferred_agent: str
) -> TaskResult:
    return await delegate_task_logic(ctx, task_description, preferred_agent, agent_registry)

# add the planning tool to the task manager agent
@TaskManagerAgent.tool
async def planning(ctx: RunContext[Any], task_description: str) -> str:
    return await planning_logic(ctx, task_description)



