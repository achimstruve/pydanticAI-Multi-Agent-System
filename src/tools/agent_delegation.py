from typing import Dict
from pydantic_ai import RunContext, ModelRetry
from src.utils import TaskResult
from src.agents.multiagent import MultiAgent

async def delegate_task_logic(
    agent: MultiAgent,
    ctx: RunContext[Dict[str, str]],
    task_description: str,
    preferred_agent: str,
) -> TaskResult:
    """
    This tool delegates a task to an agent stored in the agent_registry.
    """
    print(f"\nDelegating task:'{task_description}'\n -> to agent: {preferred_agent}")
    sub_agents = agent.get_sub_agents()
    try:
        if preferred_agent in sub_agents.keys():
            active_agent = sub_agents[preferred_agent]
            result_from_handler = await active_agent.run(task_description)
            return result_from_handler
        else:
            raise ModelRetry(
                f"Agent {preferred_agent} not found in registry. \n"
                f"Available agents: {sub_agents.keys()}"
            )
    except Exception as e:
        raise ModelRetry(
            f"Error loading or using agent: {str(e)}"
        )