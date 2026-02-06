import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from core.memory import init_memory
from utils.tools import get_tools

load_dotenv()

def build_agent():
    llm = ChatOpenAI(
        model="gpt-4o-mini-2024-07-18",
        api_key=os.getenv("OPENAI_API_KEY")
    )

    tools = get_tools()
    memory = init_memory()

    agent_executor = create_react_agent(
        model=llm,
        tools=tools,
        checkpointer=memory
    )

    return agent_executor
