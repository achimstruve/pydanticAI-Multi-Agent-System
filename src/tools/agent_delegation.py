from typing import Dict
from pydantic_ai import RunContext, ModelRetry
from src.utils import TaskResult, AgentRegistry

async def delegate_task_logic(
    ctx: RunContext[Dict[str, str]],
    task_description: str,
    preferred_agent: str,
    agent_registry: AgentRegistry
) -> TaskResult:
    """
    This tool delegates a task to an agent stored in the agent_registry.
    """
    print(f"\nDelegating task:'{task_description}'\n -> to agent: {preferred_agent}") 
    try:
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