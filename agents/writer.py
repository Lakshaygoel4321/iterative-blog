from langchain_core.messages import AIMessage, SystemMessage
from prompts.prompt_templates import writing_prompt

def writer_function(state):
    print("Running writer...")
    from config import llm

    messages = state["messages"]
    response = llm.invoke(messages + [SystemMessage(content=writing_prompt)])

    return {
        "messages": messages + [AIMessage(content=response.content)],
        "next_agent": "human_feedback"
    }
