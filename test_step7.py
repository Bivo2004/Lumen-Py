from deep_mapper import DeepKnowledgeMapper

def run_checkpoint_7():
    print("Booting up the Deep Learning Engine...\n")
    mapper = DeepKnowledgeMapper()
    
    sample_code = """
class DatabaseManager:
    def __init__(self):
        self.connected = False
        
    def connect(self):
        self.connected = True
        print("Connected to DB")
    """
    
    print("Sending code through CodeBERT for translation...")
    
    # Generate the embedding
    embedding_tensor = mapper.get_embedding(sample_code)
    
    print("\n--- Translation Results ---")
    print(f"Hardware Device: {embedding_tensor.device}")
    print(f"Tensor Shape: {embedding_tensor.shape}")
    print(f"First 5 numbers of the embedding:\n{embedding_tensor[0][:5].cpu().numpy()}")
    print("---------------------------")

if __name__ == "__main__":
    run_checkpoint_7()