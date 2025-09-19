# from typing import Dict, Any

# def fetch_leads(payload: Dict[str, Any]):
#     """
#         Simulate fetching job leads from external APIs.
#         In real implementation, call Upwork/Freelancer/LinkedIn APIs.
#     """
#     search_query = payload.get("query", "default search")
#     return [
#         {"title": "React Developer Needed", "platform": "Upwork", "query": search_query},
#         {"title": "Fast API Backend Project", "platform": "Freelancer", "query": search_query},
#     ]
from openai import tool
from app.core.openai_client import client


@tool
def fetch_lead_tool(query: str):
    """Fetch job leads from external sources based on a query."""
    return [
        {"title": "React Developer Needed", "platform": "Upwork", "query": query},
        {"title": "Fast API Backend Project", "platform": "Freelancer", "query": query},
    ]

def run_leads_agent_llm(query: str):
    # Create agent with access to tool
    agent = client.beta.agents.create(
        model="gpt-4.1",
        name="Lead Agent",
        instructions = "You are a lead generation agent. Use the fetch_lead_tool to get job leads based on user queries.",
        tools = [fetch_lead_tool],
    )

    response = client.beta.agents.resoinse.create(
        agent_id=agent.id,
        inputs=f"Find job leads for: {query}"
    )

    return response.output.parsed