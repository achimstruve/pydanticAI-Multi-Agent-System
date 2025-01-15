from pydantic_ai import Agent
from typing import Any, Dict
import json
import os
from src.agents.director_agent.director_agent import DirectorAgent
from src.agents.task_manager_agent.task_manager_agent import TaskManagerAgent
from src.agents.secret_number_agent.secret_number_agent import SecretNumberAgent
from src.agents.secret_word_agent.secret_word_agent import SecretWordAgent
from src.agents.result_handler_agent.result_handler_agent import ResultHandlerAgent
from src.utils import initialize_agent_hierarchy

# define the agent hierarchy
# the first agent is the main agent that the user interacts with
# every next list element in the list contains the delegating agent followed by the respective sub agent
# this is how you can link agents to each other

agent_hierarchy = [
    DirectorAgent,
    [DirectorAgent, TaskManagerAgent],
    [DirectorAgent, ResultHandlerAgent],
    [TaskManagerAgent, SecretNumberAgent],
    [TaskManagerAgent, SecretWordAgent],
]

# initialize the agent hierarchy
initialize_agent_hierarchy(agent_hierarchy)

async def main():
    # Define the initialuser message
    usr_msg = "What is the secret number and the secret word?"

    # First response from the main agent
    print(f"Enter your message: {usr_msg}")
    result = await agent_hierarchy[0].run(usr_msg)
    print(f"Result: {result.data.result}")
    
    # Create a loop to continue the conversation
    while usr_msg != "stop":
        usr_msg = input("Enter your message: ")
        result = await agent_hierarchy[0].run(usr_msg, message_history=result.all_messages())
        print(f"Result: {result.data.result}")

# Run the main function
import asyncio
asyncio.run(main())