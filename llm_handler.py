import requests
import json

class LocalAIHandler:
    def __init__(self, model_name: str = "llama3"):
        self.model_name = model_name
        self.url = "http://localhost:11434/api/generate"

    def generate_response(self, prompt: str, system_prompt: str = "") -> str:
        """Updated to handle optional system prompts."""
        payload = {
            "model": self.model_name, 
            "prompt": prompt, 
            "system": system_prompt, # Tell Ollama how to behave
            "stream": False
        }
        try:
            response = requests.post(self.url, json=payload)
            return response.json().get("response", "")
        except Exception as e:
            return f"Error: {e}"

    def generate_stream(self, prompt: str, system_prompt: str = ""):
        """Updated to handle optional system prompts in the stream."""
        payload = {
            "model": self.model_name, 
            "prompt": prompt, 
            "system": system_prompt, 
            "stream": True
        }
        try:
            with requests.post(self.url, json=payload, stream=True) as response:
                response.raise_for_status()
                for line in response.iter_lines():
                    if line:
                        data = json.loads(line.decode('utf-8'))
                        yield data.get("response", "")
        except Exception as e:
            yield f"\n[Error communicating with local AI: {e}]"