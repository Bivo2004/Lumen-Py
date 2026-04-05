# visualizer.py
import re

class MermaidVisualizer:
    def __init__(self, ai_handler):
        self.ai_handler = ai_handler
        self._system_prompt = (
            "You are a strict Mermaid.js architect. "
            "Rules:\n"
            "1. Start ONLY with 'graph TD'.\n"
            "2. Use ONLY single-letter IDs (A, B, C) for nodes.\n"
            "3. Format: A[Label Text] --> B[Label Text]\n"
            "4. One arrow per line.\n"
            "5. NO markdown (```), NO talk, ONLY code."
        )

    def generate_class_diagram(self, concept: str) -> str:
        prompt = f"Draw a hierarchy for: {concept}"
        
        raw_mermaid = self.ai_handler.generate_response(
            prompt=prompt,
            system_prompt=self._system_prompt
        )

        # --- THE CLEANING PIPELINE ---
        
        # 1. Strip markdown backticks
        clean = raw_mermaid.replace("```mermaid", "").replace("```", "").strip()
        
        # 2. Fix the 'Sticky Header'
        if clean.startswith("graphTD"):
            clean = clean.replace("graphTD", "graph TD\n", 1)
        
        # 3. THE SPACE KILLER (Regex)
        # This looks for any text BEFORE a '[' and removes spaces from it.
        # Example: 'Machine Learning[Label]' becomes 'MachineLearning[Label]'
        def fix_ids(match):
            return match.group(0).replace(" ", "")
            
        clean = re.sub(r'[^ \n\-\>]+(?=\[)', fix_ids, clean)
        
        # 4. Ensure it starts with graph TD
        if not clean.startswith("graph"):
            clean = "graph TD\n" + clean
             
        return clean