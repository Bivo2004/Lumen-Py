from datasets import load_dataset
from knowledge_mapper import CodeLevelClassifier

def heuristic_labeler(code_str: str) -> str:
    """
    Weak Supervision: Automatically labels real code based on heuristics.
    In a Deep Learning pipeline, you would use a pre-trained model for this step.
    """
    # Senior indicators: OOP, type hinting, generators
    if 'class ' in code_str or '->' in code_str or 'yield ' in code_str:
        return "Senior"
    
    # Junior indicators: explicit globals, or lacking functions
    if 'global ' in code_str or 'def ' not in code_str:
        return "Junior"
        
    return "Junior" # Fallback for basic scripts

def run_real_training():
    print("Downloading 500 real Python scripts from Hugging Face...")
    
    # Load a free dataset of Python code instructions
    dataset = load_dataset("flytech/python-codes-25k", split="train[:500]")
    
    X_train = []
    y_train = []
    
    print("Auto-labeling data...")
    for item in dataset:
        code = item['output'] # Extract the actual Python code from the dataset
        X_train.append(code)
        y_train.append(heuristic_labeler(code))

    # Initialize and train our OOP classifier
    classifier = CodeLevelClassifier()
    print(f"Training ML model on {len(X_train)} real files...")
    classifier.train(X_train, y_train)
    print("Training complete.\n")
    
    # Test 1: A raw script
    junior_test = "x = [1, 2, 3]\nfor i in x:\n print(i)"
    
    # Test 2: An OOP class
    senior_test = "class Database:\n def __init__(self):\n  self.connected = True"

    print("--- Real Data Model Predictions ---")
    print(f"Junior Test Script -> {classifier.predict(junior_test)}")
    print(f"Senior Test Script -> {classifier.predict(senior_test)}")
    print("-----------------------------------")

if __name__ == "__main__":
    run_real_training()