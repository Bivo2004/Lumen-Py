class SocraticStrategy:
    def __init__(self, mode: str = "mentor"):
        self.mode = mode.lower()

    def get_system_prompt(self) -> str:
        if self.mode == "strict":
            return (
                "You are a strict Socratic coding mentor. "
                "NEVER give the user direct code solutions. "
                "Always respond with a guiding question to make them think."
            )
        elif self.mode == "direct":
            return (
                "You are a helpful Senior Software Engineer. "
                "Provide the direct answer, including the exact code needed. "
                "Keep your explanations concise, professional, and clear."
            )
        else: # Default Mentor mode
            return (
                "You are a balanced AI coding mentor. "
                "If the user asks a conceptual question, explain it clearly. "
                "If they are stuck on code, provide partial snippets or pseudo-code to help, "
                "but do not write the entire script for them unless they specifically ask. "
                "Be encouraging and direct."
            )

class SocraticEngine:
    def __init__(self, ai_handler, mode="mentor"):
        self.ai_handler = ai_handler
        self.strategy = SocraticStrategy(mode)
        self.history = []  # <-- NEW: The Memory Bank

    def ask_tutor(self, prompt: str) -> str:
        # Add user prompt to memory
        self.history.append(f"User: {prompt}")
        
        # Keep only the last 6 messages so the context window doesn't overflow
        if len(self.history) > 6:
            self.history = self.history[-6:]
            
        history_text = "\n".join(self.history)
        full_prompt = f"{self.strategy.get_system_prompt()}\n\n{history_text}\nLumen:"
        
        response = self.ai_handler.generate_response(full_prompt)
        
        # Save Lumen's answer to memory
        self.history.append(f"Lumen: {response}")
        return response

    def ask_tutor_stream(self, prompt: str):
        # Add user prompt to memory
        self.history.append(f"User: {prompt}")
        
        # Keep only the last 6 messages
        if len(self.history) > 6:
            self.history = self.history[-6:]
            
        history_text = "\n".join(self.history)
        full_prompt = f"{self.strategy.get_system_prompt()}\n\n{history_text}\nLumen:"
        
        response_buffer = ""
        # Stream the response back to the user, but also save it locally
        for chunk in self.ai_handler.generate_stream(full_prompt):
            response_buffer += chunk
            yield chunk
            
        # Save Lumen's final answer into the memory bank
        self.history.append(f"Lumen: {response_buffer}")