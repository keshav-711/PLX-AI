# plx_core.py

class PLXCore:
    def __init__(self):
        print("[PLX-Core] Initialized.")

    def route(self, user_input):
        """
        Basic router that decides which agent to call.
        For now, this is just placeholder logic.
        """
        user_input = user_input.lower()

        if "weather" in user_input:
            return self.call_weather_agent(user_input)

        elif "news" in user_input:
            return self.call_news_agent(user_input)

        elif "joke" in user_input:
            return self.call_joke_agent(user_input)

        else:
            return self.default_response(user_input)

    # -----------------------------
    # Placeholder Agent Calls
    # -----------------------------

    def call_weather_agent(self, query):
        print("[Router] Weather agent triggered.")
        return "WeatherAgent: (placeholder response)"

    def call_news_agent(self, query):
        print("[Router] News agent triggered.")
        return "NewsAgent: (placeholder response)"

    def call_joke_agent(self, query):
        print("[Router] Joke agent triggered.")
        return "JokeAgent: (placeholder response)"

    def default_response(self, query):
        print("[Router] Default fallback triggered.")
        return "PLX-Core: I don't understand that yet, but I'm learning!"

# -----------------------------
# Input Loop
# -----------------------------

if __name__ == "__main__":
    core = PLXCore()

    print("\n=== PLX-AI Core Running ===")
    print("Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Shutting down PLX-Core...")
            break

        response = core.route(user_input)
        print("PLX:", response)