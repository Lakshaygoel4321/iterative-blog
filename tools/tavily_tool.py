from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool

@tool
def tavily_search_tool(query: str) -> str:
    """Search the content on the web"""
    search = TavilySearchResults(max_results=3)
    response = search.invoke(query)
    return str(response)
