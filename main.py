from pydantic_ai import Agent
from typing import Any, Dict
import json
import os
from src.agents.director_agent.director_agent import DirectorAgent

# Example of using the main agent to delegate a task
async def main():
    # Simulate a query that would require delegation
    usr_msg = "What is the secret number and the secret word?"
    print(f"Enter your message: {usr_msg}")
    result = await DirectorAgent.run(usr_msg)
    print(f"Result: {result.data.result}")
    while usr_msg != "stop":
        usr_msg = input("Enter your message: ")
        result = await DirectorAgent.run(usr_msg, message_history=result.all_messages())
        print(f"Result: {result.data.result}")

# Run our example
import asyncio
asyncio.run(main())