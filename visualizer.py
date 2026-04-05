from llm_handler import LocalAIHandler

class MermaidVisualizer:
    """
    Translates architectural concepts or Python code into Mermaid.js diagram strings.
    """
    def __init__(self, ai_handler: LocalAIHandler):
        self.ai_handler = ai_handler
        self._system_prompt = (
            "You are an expert Software Architect. Your ONLY job is to generate "
            "valid Mermaid.js diagram code. "
            "DO NOT include any conversational text, explanations, or Markdown formatting. "
            "Return strictly the raw Mermaid syntax.\n\n"
            "CRITICAL SYNTAX RULES:\n"
            "1. For Concepts/Flows: Use `graph TD`. Define nodes: `A[\"Name\"]` and links: `A -->|label| B`.\n"
            "2. For OOP Classes: Use `classDiagram`. Define classes: `class Car { +start() }` and links: `Car --> Engine : contains`.\n"
            "3. NEVER mix flowchart syntax (`graph`) with OOP syntax (`classDiagram`)."
        )

    def generate_class_diagram(self, concept_or_code: str) -> str:
        """
        Generates a UML class diagram based on a concept or code snippet.
        """
        prompt = (
            f"Generate the most appropriate Mermaid diagram (either `graph TD` for concepts or `classDiagram` for strict code) "
            f"for the following:\n\n{concept_or_code}"
        )
        
        # We pass our strict system prompt to the handler
        raw_mermaid = self.ai_handler.generate_response(
            prompt=prompt, 
            system_prompt=self._system_prompt
        )
        
        # Safety filter to remove accidental markdown blocks
        clean_mermaid = raw_mermaid.replace("```mermaid", "").replace("```", "").strip()
        
        return clean_mermaid