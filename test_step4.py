from llm_handler import LocalAIHandler
from visualizer import MermaidVisualizer

def run_checkpoint_4():
    print("Initializing Visualizer...")
    handler = LocalAIHandler(model_name="llama3")
    visualizer = MermaidVisualizer(ai_handler=handler)

    # The concept we want to visualize
    architecture_concept = "A Car class that has a composition relationship with an Engine class."
    
    print(f"Requesting diagram for: '{architecture_concept}'\n")
    print("Drawing on the whiteboard...\n")
    
    mermaid_code = visualizer.generate_class_diagram(architecture_concept)
    
    print("--- Mermaid.js Output ---")
    print(mermaid_code)
    print("-------------------------")
    
    print("\nTip: You can copy the output and paste it into [https://mermaid.live](https://mermaid.live) to see the drawing!")

if __name__ == "__main__":
    run_checkpoint_4()