from pydantic_ai import Agent
from typing import Any, Dict
import json
import os
from src.agents.director_agent.director_agent import DirectorAgent

async def main():
    # Define the initialuser message
    usr_msg = "What is the secret number and the secret word?"

    # First response from the main agent
    print(f"Enter your message: {usr_msg}")
    result = await DirectorAgent.run(usr_msg)
    print(f"Result: {result.data.result}")
    
    # Create a loop to continue the conversation
    while usr_msg != "stop":
        usr_msg = input("Enter your message: ")
        result = await DirectorAgent.run(usr_msg, message_history=result.all_messages())
        print(f"Result: {result.data.result}")

# Run the main function
import asyncio
asyncio.run(main())