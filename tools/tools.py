from langchain.tools import tool

from core.GetLinks import GetLinks
from core.GatherData import GetData
from core.MainModel import Model
from core.SendMail import Mail

@tool
def extract_links() -> dict:#dict because tools cannot return tuples
    """Extract article links from already provided websites and return the links as lists"""
    links1, links2 = GetLinks().get_links()
    return {"links1" : links1, "links2" : links2}

@tool
def gather_content(links1 : list[str], links2: list[str]) -> dict:
    """Visit the provided article and misc links and extract the textual content. Returns a dictionary mapping links to their content."""
    return GetData().get_data(links1, links2)

@tool
def use_model(articles : dict) -> dict:
    """Loads the LLM model, prepares the prompt for the llm, summarizes the articles and return a dictionary of articles and links"""
    return Model().model(articles)

@tool
def mailing(articles : dict) -> str:
    """Sends an email containing summarized articles.
    The dictionary should have links as keys and summaries as values."""
    Mail(articles).mail()
    return "Email Sent Successfully"

