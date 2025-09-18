from typing import Dict, Any

def fetch_leads(payload: Dict[str, Any]):
    """
        Simulate fetching job leads from external APIs.
        In real implementation, call Upwork/Freelancer/LinkedIn APIs.
    """
    search_query = payload.get("query", "default search")
    return [
        {"title": "React Developer Needed", "platform": "Upwork", "query": search_query},
        {"title": "Fast API Backend Project", "platform": "Freelancer", "query": search_query},
    ]
