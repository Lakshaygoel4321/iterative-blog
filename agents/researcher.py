from langchain_core.messages import AIMessage, SystemMessage
from prompts.prompt_templates import research_prompt

def research_function(state):
    print("Running researcher...")
    from config import llm  # avoid circular import

    messages = state["messages"]
    response = llm.invoke(messages + [SystemMessage(content=research_prompt)])
    
    return {
        "messages": messages + [AIMessage(content=response.content)],
        "next_agent": "analysis"
    }
