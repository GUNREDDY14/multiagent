# main.py
from agents import MessengerAgent, CoderAgent

def main():
    coder_agent = CoderAgent()
    messenger_agent = MessengerAgent(coder_agent)

    print("Welcome to LangChain Duo! (Type 'exit' to quit)")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        output = messenger_agent.handle_user_request(user_input)
        print("\nGenerated Code:\n")
        print(output)

if __name__ == "__main__":
    main()
