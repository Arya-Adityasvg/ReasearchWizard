from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime
import os

# Function to save research results
def save_to_txt(data: str, topic: str = None, filename: str = None):
    """
    Save research data to a text file.
    - If topic is provided, saves as <topic>_research.txt
    - If filename is provided, saves with that filename
    - Otherwise defaults to research_output.txt
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if topic:
        safe_topic = "".join(c if c.isalnum() or c in (" ", "_") else "_" for c in topic)
        filename = f"{safe_topic}_research.txt"
    elif not filename:
        filename = "research_output.txt"

    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {os.path.abspath(filename)}"

# Expose save_to_txt as a tool
save_tool = Tool(
    name="save_text_to_file",
    func=lambda text: save_to_txt(text),   # tool gets plain text input
    description="Saves structured research data to a text file. Pass the final report as input.",
)

# Search tool
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for information",
)

# Wikipedia tool
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=1000)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
