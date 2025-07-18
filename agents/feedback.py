from langchain.types import interrupt, Command
from langchain_core.messages import HumanMessage

def human_feedback_function(state):
    print("Awaiting human feedback...")

    user_feedback = interrupt({
        "message": "Your feedback (or 'done' to finish): "
    })

    if user_feedback.lower().strip() == "done":
        return Command(update={"messages": state["messages"] + [HumanMessage(content="finalize")]}, goto="end_node")
    
    return Command(update={"messages": state["messages"] + [HumanMessage(content=user_feedback)]}, goto="writer")
