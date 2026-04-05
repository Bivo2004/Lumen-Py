from llm_handler import LocalAIHandler

def run_checkpoint_1():
    print("Initializing LocalAIHandler...")
    # Instantiate the handler
    handler = LocalAIHandler(model_name="llama3")

    system_instruction = "You are a Senior Python Architect. Keep your answer to exactly one sentence."
    user_prompt = "Explain why Object-Oriented Programming is useful."

    print(f"Sending prompt to Ollama (llama3)...\n")
    
    # Generate response
    response = handler.generate_response(
        prompt=user_prompt, 
        system_prompt=system_instruction
    )

    print("--- AI Response ---")
    print(response)
    print("-------------------")

if __name__ == "__main__":
    run_checkpoint_1()