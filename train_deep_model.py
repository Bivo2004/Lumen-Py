from datasets import load_dataset
from deep_mapper import DeepKnowledgeMapper

def heuristic_labeler(code_str: str) -> str:
    """Labels the raw training data."""
    if 'class ' in code_str or '->' in code_str or 'yield ' in code_str or '@' in code_str:
        return "Senior"
    return "Junior"

def run_deep_training():
    print("Downloading dataset from Hugging Face...")
    # Pull a larger chunk so we have enough data to mine for "Senior" examples
    dataset = load_dataset("flytech/python-codes-25k", split="train[:5000]")
    
    X_train = []
    y_train = []
    
    junior_count = 0
    senior_count = 0
    max_per_class = 250 # We want exactly 250 of each (500 total)
    
    print("Mining and balancing data...")
    for item in dataset:
        code = item['output']
        label = heuristic_labeler(code)
        
        # Only add to our training list if we haven't hit our cap for that class
        if label == "Senior" and senior_count < max_per_class:
            X_train.append(code)
            y_train.append(label)
            senior_count += 1
        elif label == "Junior" and junior_count < max_per_class:
            X_train.append(code)
            y_train.append(label)
            junior_count += 1
            
        # Stop searching once we have a perfectly balanced dataset
        if junior_count == max_per_class and senior_count == max_per_class:
            break

    print(f"Dataset Balanced: {junior_count} Junior | {senior_count} Senior")
    
    mapper = DeepKnowledgeMapper()
    
    print("\nStarting Deep Learning Pipeline...")
    
    mapper.train(X_train, y_train, epochs=20)
    
    print("\n--- Live Inference Test ---")
    junior_script = "x = 10\ny = 20\nprint(x + y)"
    senior_script = "class Server:\n    def __init__(self):\n        self.active = True"
    
    print(f"Junior Test -> Classified as: {mapper.predict(junior_script)}")
    print(f"Senior Test -> Classified as: {mapper.predict(senior_script)}")
    print("---------------------------")

if __name__ == "__main__":
    run_deep_training()