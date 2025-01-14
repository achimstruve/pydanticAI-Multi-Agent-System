from pydantic import BaseModel
from typing import Dict, List
from pydantic_ai import Agent

# Define a simple model for the result of the task delegation
class TaskResult(BaseModel):
    task_description: str
    result: str


class AgentRegistry:
    def __init__(self):
        self.agents: Dict[str, Agent] = {}

    def register_agent(self, agent: Agent):
        self.agents[agent.name] = agent

    def get_agent(self, name: str) -> Agent:
        return self.agents.get(name)
    
    def get_all_agents(self) -> Dict[str, Agent]:
        return self.agents
    
    def get_agent_names(self) -> List[str]:
        return list(self.agents.keys())

