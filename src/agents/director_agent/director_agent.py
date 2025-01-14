from pydantic_ai import RunContext, Agent, ModelRetry
from typing import Any, Dict
from .system_prompt import system_prompt
import json
from src.utils import TaskResult
from src.utils import AgentRegistry
from src.tools.agent_delegation import delegate_task_logic
from src.agents.task_manager_agent.task_manager_agent import TaskManagerAgent
from src.agents.result_handler_agent.result_handler_agent import ResultHandlerAgent

# Define the main agent
DirectorAgent = Agent(
    name="director_agent",
    model="openai:gpt-4o",
    system_prompt=system_prompt,
    result_type=TaskResult
)

# Define all the agents that can be used by the director agent
agent_registry = AgentRegistry()
agent_registry.register_agent(TaskManagerAgent)
agent_registry.register_agent(ResultHandlerAgent)

# Define a tool on the main agent that can delegate tasks to the task_handler_agent
@DirectorAgent.tool
async def delegate_task(
    ctx: RunContext[Dict[str, str]],
    task_description: str,
    preferred_agent: str
) -> TaskResult:
    """
    This tool delegates a task based on metadata from a stored registry.
    """
    return await delegate_task_logic(ctx, task_description, preferred_agent, agent_registry)


@DirectorAgent.tool
async def planning(ctx: RunContext[Any], task_description: str) -> str:
    """
    This tool is used to plan the next steps.
    Always break down the task into smaller steps, but not more than necessary.
    Think about where you are in the lined out planning process to do the next step.
    IT IS IMPORTANT THAT YOU ALWAYS LINE OUT ALL THE STEPS THAT ARE NECESSARY TO SOLVE THE TASK!
    """
    print(f"\n{DirectorAgent.name} is using the planning tool with task_description: {task_description}")
    return ctx.deps



