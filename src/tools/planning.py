from pydantic_ai import RunContext
from typing import Any

async def planning_logic(ctx: RunContext[Any], task_description: str) -> str:
    """
    This tool is used to plan the next steps.
    Always break down the task into smaller steps, but not more than necessary.
    Think about where you are in the lined out planning process to do the next step.
    IT IS IMPORTANT THAT YOU ALWAYS LINE OUT ALL THE STEPS THAT ARE NECESSARY TO SOLVE THE TASK!
    """
    print(f"\nUsing the planning tool with task_description: {task_description}")
    return ctx.deps