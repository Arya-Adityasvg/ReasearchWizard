import os
from dotenv import load_dotenv
from pydantic import BaseModel, field_validator
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool, save_to_txt

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

    @field_validator("summary")
    def check_summary_length(cls, v: str) -> str:
        """Ensure at least 100 words in the summary"""
        if len(v.split()) < 100:
            raise ValueError("Summary must be at least 100 words.")
        return v

llm = ChatOpenAI(
    model="openai/gpt-oss-120b",
    openai_api_key=os.getenv("OPENAI_API_KEY"),   
    openai_api_base=os.getenv("OPENAI_API_BASE"), 
)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Ensure the summary is detailed (minimum 100 words) and structured with 
            bullet points or sections where appropriate. 
            Wrap the output in this format and provide no other text:
            {format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]

agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools,
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

query = input(" What can I help you research? ")

raw_response = agent_executor.invoke({"query": query})
print("\n--- Raw Agent Response ---\n", raw_response)

output_text = raw_response.get("output")

try:
    structured_response = parser.parse(output_text)
    print("\n Parsed Structured Response:\n", structured_response)

    save_to_txt(str(structured_response), topic=structured_response.topic)
    print("\n Research result saved with topic-based filename.")

except Exception as e:
    print("\n Could not parse structured output:", e)
    print("Output was:", output_text)

    save_to_txt(str(raw_response))
    print("\n Raw response saved to fallback file: research_output.txt")
