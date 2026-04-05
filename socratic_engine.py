from abc import ABC, abstractmethod
from llm_handler import LocalAIHandler

# --- 1. The Strategy Interface ---
class TutorStrategy(ABC):
    """Abstract base class defining a tutoring strategy."""
    
    @abstractmethod
    def get_system_prompt(self) -> str:
        pass

# --- 2. Concrete Strategy ---
class SocraticStrategy(TutorStrategy):
    """A strict strategy that refuses to write code and only asks guiding questions."""
    
    def get_system_prompt(self) -> str:
        return (
            "You are Lumen, an expert Python Architect and strict Socratic tutor. "
            "YOUR PRIME DIRECTIVE: NEVER write code for the user. EVER. "
            "If the user asks for code, refuse politely. Instead, identify the core "
            "concept they are struggling with and ask ONE guiding question to help them "
            "figure it out themselves. Keep your responses short, analytical, and encouraging."
        )

# --- 3. The Context (Engine) ---
class SocraticEngine:
    """
    The main engine that uses a TutorStrategy and the LocalAIHandler 
    to process user requests.
    """
    def __init__(self, ai_handler: LocalAIHandler, strategy: TutorStrategy):
        self.ai_handler = ai_handler
        self.strategy = strategy

    def set_strategy(self, strategy: TutorStrategy):
        """Allows swapping the tutoring style at runtime."""
        self.strategy = strategy

    def ask_tutor(self, user_input: str) -> str:
        """Processes the user input through the current strategy."""
        system_prompt = self.strategy.get_system_prompt()
        return self.ai_handler.generate_response(
            prompt=user_input, 
            system_prompt=system_prompt
        )
    def ask_tutor_stream(self, prompt: str):
        """Passes the system prompt and yields the streamed response."""
        full_prompt = f"{self.strategy.get_system_prompt()}\n\nUser: {prompt}\nLumen:"
        return self.ai_handler.generate_stream(full_prompt)