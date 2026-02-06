from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from utils.tools import get_tools

def build_agent(memory):

    # setup llm
    llm = ChatOllama(
        model="llama3.2:3b",
        temperature=0
    )

    # Tells the llm the role and operations which need to be performed.
    system_message = "You are a helpful assistant. You have acces to a search tool. If the user asks for facts or current events, YOU MUST use the search tool. Do not guess."

    # create the agent
    agent_executor = create_react_agent(
        model=llm,
        tools=get_tools(),
        checkpointer=memory,
        prompt=system_message
    )

    return agent_executor
