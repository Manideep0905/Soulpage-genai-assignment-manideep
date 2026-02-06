import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from core.memory import init_memory
from utils.tools import get_tools

load_dotenv()

def build_agent():

    # setup llm
    llm = ChatOllama(
        model="llama3.2:3b",
        temperature=0
    )

    # get tools and memory
    tools = get_tools()
    memory = init_memory()

    # Tells the llm the role and operations which need to be performed.
    system_message = "You are a helpful assistant. You have acces to a search tool. If the user asks for facts or current events, YOU MUST use the search tool. Do not guess."

    # create the agent
    agent_executor = create_react_agent(
        model=llm,
        tools=tools,
        checkpointer=memory,
        prompt=system_message
    )

    return agent_executor
