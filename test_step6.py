from deep_mapper import DeepKnowledgeMapper
import torch

def run_checkpoint_6():
    print("Initializing PyTorch Neural Network...\n")
    
    # We will assume our code embeddings will be 768 numbers long 
    # (this is the standard size for models like CodeBERT)
    mapper = DeepKnowledgeMapper(input_dimension=768)
    
    print("--- Neural Network Architecture ---")
    print(mapper.get_model_summary())
    print("-----------------------------------")
    
    print(f"\nHardware Check: Running on {mapper.device.type.upper()}")

if __name__ == "__main__":
    run_checkpoint_6()