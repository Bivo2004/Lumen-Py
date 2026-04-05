import requests
import json

class LocalAIHandler:
    def __init__(self, model_name: str = "llama3"):
        self.model_name = model_name
        self.url = "http://localhost:11434/api/generate"

    def generate_response(self, prompt: str) -> str:
        """The old method: waits for the full response."""
        payload = {"model": self.model_name, "prompt": prompt, "stream": False}
        response = requests.post(self.url, json=payload)
        return response.json().get("response", "")

    def generate_stream(self, prompt: str):
        """The new method: streams the response token by token."""
        payload = {"model": self.model_name, "prompt": prompt, "stream": True}
        try:
            with requests.post(self.url, json=payload, stream=True) as response:
                response.raise_for_status()
                for line in response.iter_lines():
                    if line:
                        data = json.loads(line.decode('utf-8'))
                        yield data.get("response", "")
        except Exception as e:
            yield f"\n[Error communicating with local AI: {e}]"