from knowledge_mapper import CodeLevelClassifier

def run_checkpoint_3():
    classifier = CodeLevelClassifier()
    
    # 1. Our Micro-Dataset
    X_train = [
        "global count\ncount = 0\ndef increment():\n global count\n count += 1", # Junior
        "x = 10\ny = 20\nprint(x+y)", # Junior
        "def do_stuff(data):\n for i in range(len(data)):\n  print(data[i])", # Junior
        "class Counter:\n def __init__(self):\n  self._count = 0\n def increment(self):\n  self._count += 1", # Senior
        "def calculate_total(prices: list[float]) -> float:\n return sum(prices)", # Senior
        "from dataclasses import dataclass\n@dataclass\nclass User:\n name: str" # Senior
    ]
    y_train = ["Junior", "Junior", "Junior", "Senior", "Senior", "Senior"]
    
    print("Training the ML classifier on the micro-dataset...")
    classifier.train(X_train, y_train)
    print("Training complete.\n")
    
    # 2. The Test: A user inputs a script heavily relying on global variables
    bad_practice_code = """
global db_connection
db_connection = None

def connect():
    global db_connection
    db_connection = "Connected"
"""
    
    print("Analyzing user's code snippet:\n", bad_practice_code)
    
    # 3. Predict
    prediction = classifier.predict(bad_practice_code)
    print(f"\n--- Knowledge Gap Detection ---")
    print(f"Classification: {prediction} Developer")
    print("-------------------------------")

if __name__ == "__main__":
    run_checkpoint_3()