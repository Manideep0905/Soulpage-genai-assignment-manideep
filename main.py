from core.chatbot import build_agent

def main():
    print("CLI knowledge bot (Type 'q' to quit)")
    print("-------------------------")

    agent = build_agent()

    config = {
        "configurable": {"thread_id": "1"}
    }

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["q", "quit", "exit"]:
            print("Exited")
            break

        events = agent.stream(
            {"messages": [("user", user_input)]},
            config=config,
            stream_mode="values"
        )

        for event in events:
            last_message = event["messages"][-1]

            if last_message.type == "ai":
                print(f"Bot: {last_message.content}")


if __name__ == "__main__":
    main()

