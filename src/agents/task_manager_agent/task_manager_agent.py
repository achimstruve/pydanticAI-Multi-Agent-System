from pydantic_ai import RunContext, Agent
from typing import Any, Dict
from .system_prompt import system_prompt
import json
from src.utils import TaskResult
from src.utils import AgentRegistry
from src.agents.secret_number_agent.secret_number_agent import SecretNumberAgent
from src.agents.secret_word_agent.secret_word_agent import SecretWordAgent

# Define the main agent
TaskManagerAgent = Agent(
    name="task_manager_agent",
    model="openai:gpt-4o",
    system_prompt=system_prompt,
    result_type=TaskResult
)

# Define all the agents that can be used by the director agent
agent_registry = AgentRegistry()
agent_registry.register_agent(SecretNumberAgent)
agent_registry.register_agent(SecretWordAgent)

# Define a tool on the main agent that can delegate tasks to the secret_knower_agent
@TaskManagerAgent.tool
async def delegate_task(ctx: RunContext[Dict[str, str]], task_description: str, preferred_agent: str) -> TaskResult:
    """
    This tool delegates a task based on metadata from a stored registry.
    """
    print(f"\n{TaskManagerAgent.name} is using the delegate_task tool with task_description: \n{task_description} \n to delegate to: {preferred_agent}")
    try:
        if preferred_agent in agent_registry.get_all_agents():
            active_agent = agent_registry.get_agent(preferred_agent)
            result_from_handler = await active_agent.run(task_description)
            return result_from_handler
        else:
            return f"Agent {preferred_agent} not found in registry."
    except Exception as e:
        return f"Error loading or using agent: {str(e)}"


@TaskManagerAgent.tool
async def planning(ctx: RunContext[Any], task_description: str) -> str:
    """
    This tool is used to plan the next steps.
    Always break down the task into smaller steps, but not more than necessary.
    Think about where you are in the lined out planning process to do the next step.
    Always report the information that you got from the specialist agents, such as the secret_knower_agent back to the director_agent.
    """
    print(f"\n{TaskManagerAgent.name} is using the planning tool with task_description: {task_description}")
    return ctx.deps



