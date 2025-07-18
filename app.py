from graph.blog_graph import build_blog_graph
from config import config
from utils.memory import memory
from langchain_core.messages import HumanMessage
from langgraph.types import Command,interrupt
import uuid

def end_node_function(state):
    print("\n✅ Final Blog Output:\n")
    print(state["messages"][-1].content)
    return {"messages": state["messages"]}

def main():
    graph = build_blog_graph(end_node_function)
    app = graph.compile(checkpointer=memory)

    topic = input("📝 Enter blog post topic: ")
    initial_state = {
        "messages": [HumanMessage(content=topic)],
        "next_agent": ""
    }

    for chunk in app.stream(initial_state, stream_mode="updates", config=config):
        for node_id, value in chunk.items():
            if node_id == "__interrupt__":
                while True:
                    u_input = input("🔁 Your feedback (or 'done' to finish): ")
                    app.invoke(Command(resume=u_input), config=config)
                    if u_input.lower().strip() == "done":
                        break

if __name__ == "__main__":
    main()
