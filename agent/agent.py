# agent.py

from pydantic import BaseModel
from typing import Dict, Optional, List
from langgraph.graph import StateGraph, END
from tools.tools import extract_links, gather_content, use_model, mailing


# 1. Define the state model
class State(BaseModel):
    links: Optional[Dict[str, List[str]]] = None
    articles: Optional[Dict[str, str]] = None
    summaries: Optional[Dict[str, str]] = None
    confirmation: Optional[str] = None


# 2. Build the state graph
builder = StateGraph(State)


# 3. Define nodes
def get_links_node(state):
    links = extract_links.invoke({})
    return {"links": links}
builder.add_node("get_links", get_links_node)


def gather_data_node(state):
    articles = gather_content.invoke(state.links)
    return {"articles": articles}
builder.add_node("gather_data", gather_data_node)


def model_node(state):
    summaries = use_model.invoke({"articles" : state.articles})
    return {"summaries": summaries}
builder.add_node("summarize", model_node)


def mail_node(state):
    confirmation = mailing.invoke({"articles" : state.summaries})
    return {"confirmation": confirmation}
builder.add_node("send_mail", mail_node)


# 4. Define the flow
builder.set_entry_point("get_links")
builder.add_edge("get_links", "gather_data")
builder.add_edge("gather_data", "summarize")
builder.add_edge("summarize", "send_mail")
builder.add_edge("send_mail", END)

graph = builder.compile()


# 5. Run the agent
if __name__ == "__main__":
    final_output = graph.invoke({})
    print("Workflow completed. Result: ")
    #print(final_output)
