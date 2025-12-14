from agents import tutor,planner,debugger,motivator,research,memory

class PLXCore:
    def __init__(self):
        print("[PLX-Core] Initialized.")

    def route(self, user_input):
        user_input = user_input.lower()

        if "explain" in user_input:
            return tutor.handle(user_input)

        elif "plan" in user_input:
            return planner.handle(user_input)

        elif "error" in user_input:
            return debugger.handle(user_input)
        
        elif "motivate" in user_input:
            return motivator.handle(user_input)
        
        elif "define" in user_input:
            return research.handle(user_input)

        elif "who" in user_input or "name" in user_input or "weak" in user_input:
            return memory.handle(user_input)

        else:
            return self.default_response(user_input)
    def call_planner_agent(self, query):
        print("[Router] planner agent triggered.")
        return "plannerAgent: (placeholder response)"
    
    def call_tutor_agent(self, query):
        print("[Router] tutuor agent triggered.")
        return "tutorAgent: (placeholder response)"

    def call_debugger_agent(self, query):
        print("[Router] debugger agent triggered.")
        return "debuggerAgent: (placeholder response)"
    
    def call_motivater_agent(self, query):
        print("[Router] motivator agent triggered.")
        return "motivatorAgent: (placeholder response)"
    
    def call_research_agent(self, query):
        print("[Router] research agent triggered.")
        return "researchAgent: (placeholder response)"

    def default_response(self, query):
        print("[Router] Default fallback triggered.")
        return "PLX-Core: I don't understand that yet, but I'm learning!"

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