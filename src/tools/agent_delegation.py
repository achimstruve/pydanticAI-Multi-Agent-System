from typing import Dict
from pydantic_ai import RunContext, ModelRetry, Agent
from src.utils import TaskResult, AgentRegistry

async def delegate_task_logic(
    ctx: RunContext[Dict[str, str]],
    task_description: str,
    preferred_agent: str,
    agent_registry: AgentRegistry
) -> TaskResult:
    """
    This function implements the shared logic for delegating a task.
    """
    print(f"\nRunning delegate_task_logic with task_description: \n{task_description}\n to delegate to: {preferred_agent}")
    try:
        # Assume you have a global agent_registry or pass it in explicitly
        if preferred_agent in agent_registry.get_all_agents():
            active_agent = agent_registry.get_agent(preferred_agent)
            result_from_handler = await active_agent.run(task_description)
            return result_from_handler
        else:
            raise ModelRetry(
                f"Agent {preferred_agent} not found in registry. \n"
                f"Available agents: {agent_registry.get_agent_names()}"
            )
    except Exception as e:
        raise ModelRetry(
            f"Error loading or using agent: {str(e)}"
        )