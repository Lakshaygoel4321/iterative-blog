from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from tools.tavily_tool import tavily_search_tool
from prompts.prompt_templates import analysis_prompt_template

def analysis_function(state):
    print("Running analysis...")
    from config import llm

    messages = state["messages"]
    topic = next((msg.content for msg in reversed(messages) if isinstance(msg, HumanMessage)), "general topic")
    search_results = tavily_search_tool(topic)

    prompt = analysis_prompt_template.format(search_results=search_results)
    response = llm.invoke(messages + [SystemMessage(content=prompt)])

    return {
        "messages": messages + [AIMessage(content=response.content)],
        "next_agent": "writer"
    }
