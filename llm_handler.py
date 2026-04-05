import ollama
from typing import List, Dict, Optional

class LocalAIHandler:
    """
    Handles communication with the local Ollama instance.
    Encapsulates the connection to adhere to the Single Responsibility Principle.
    """
    
    def __init__(self, model_name: str = "llama3"):
        self._model_name = model_name

    def generate_response(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """
        Sends a prompt to the local model and returns the response string.
        """
        messages: List[Dict[str, str]] = []
        
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
            
        messages.append({"role": "user", "content": prompt})

        try:
            # Synchronous call to the local Ollama daemon
            response = ollama.chat(model=self._model_name, messages=messages)
            return response.get('message', {}).get('content', "")
            
        except Exception as e:
            return f"[System Error] Failed to communicate with Ollama: {e}\n" \
                   f"Please ensure the Ollama application is running."