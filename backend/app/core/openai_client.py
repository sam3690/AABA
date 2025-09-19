from openai import OpenAI

client = OpenAI()

def create_agent(**kwargs):
    """Wrapper for OpenAI Agents SDK - agent creation"""
    return client.beta.agents.create(**kwargs)

def run_agent(agent_id: str, input_text: str):
    """Wrapper for running an agent"""
    return client.beta.agents.responses.create(
        agent_id=agent_id,
        inputs=input_text
    )