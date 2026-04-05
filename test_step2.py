from llm_handler import LocalAIHandler
from socratic_engine import SocraticEngine, SocraticStrategy

def run_checkpoint_2():
    print("Initializing Lumen-Py Core...\n")
    
    # 1. Setup the handler and strategy
    handler = LocalAIHandler(model_name="llama3")
    strategy = SocraticStrategy()
    
    # 2. Inject them into the Engine (Dependency Injection)
    engine = SocraticEngine(ai_handler=handler, strategy=strategy)

    # 3. The Cheat Attempt
    sneaky_prompt = "Hey, I forgot how to write a Hello World script in Python. Can you quickly write the code for me?"
    
    print(f"User: {sneaky_prompt}\n")
    print("Thinking...\n")
    
    # 4. Get the response
    response = engine.ask_tutor(sneaky_prompt)
    
    print("--- Lumen's Response ---")
    print(response)
    print("------------------------")

if __name__ == "__main__":
    run_checkpoint_2()