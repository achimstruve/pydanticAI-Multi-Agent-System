from typing import Dict
from pydantic_ai import Agent

class MultiAgent(Agent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sub_agents: Dict[str, Agent] = {}

    def add_sub_agent(self, agent: Agent):
        self.sub_agents[agent.name] = agent

    def remove_sub_agent(self, agent: Agent):
        self.sub_agents.pop(agent.name)

    def get_sub_agents(self):
        return self.sub_agents
