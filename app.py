import streamlit as st
from langgraph.checkpoint.memory import MemorySaver
from core.chatbot import build_agent

st.set_page_config(page_title="Conversational Knowledge Bot")
st.title("Conversational Knowledge Bot")

if "checkpointer" not in st.session_state:
    st.session_state.checkpointer = MemorySaver()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = "user_session_1"

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Ask me anything."):
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.write("Thinking..")

        try:
            agent = build_agent(st.session_state.checkpointer)

            config = {"configurable": {"thread_id": st.session_state.thread_id}}

            final_response = ""

            for event in agent.stream(
                {"messages": [("user", prompt)]},
                config=config,
                stream_mode="values"
            ):
                last_message = event["messages"][-1]

                if last_message.type == "ai":
                    final_response = last_message.content

            message_placeholder.write(final_response)

            st.session_state.messages.append({"role": "assistant", "content": final_response})
        except Exception as e:
            message_placeholder.error(f"Error: {str(e)}")
