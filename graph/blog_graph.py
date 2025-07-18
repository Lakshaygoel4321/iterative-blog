from langgraph.graph import StateGraph, END
from langgraph.types import Command
from typing import List, Annotated, TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from agents.researcher import research_function
from agents.analysis import analysis_function
from agents.writer import writer_function
from agents.feedback import human_feedback_function

class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]
    next_agent: str

def build_blog_graph(end_node_fn):
    graph = StateGraph(AgentState)
    graph.add_node("researcher", research_function)
    graph.add_node("analysis", analysis_function)
    graph.add_node("writer", writer_function)
    graph.add_node("human_feedback", human_feedback_function)
    graph.add_node("end_node", end_node_fn)

    graph.set_entry_point("researcher")
    graph.add_edge("researcher", "analysis")
    graph.add_edge("analysis", "writer")
    graph.add_edge("writer", "human_feedback")
    graph.add_edge("human_feedback", "writer")
    graph.add_edge("end_node", END)

    return graph
