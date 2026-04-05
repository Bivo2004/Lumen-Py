import torch
import torch.nn as nn
import torch.optim as optim
from transformers import RobertaTokenizer, RobertaModel
import os

class CodeLevelNN(nn.Module):
    """A PyTorch Feedforward Neural Network to classify architectural maturity."""
    def __init__(self, input_dim: int = 768, hidden_dim: int = 128):
        super(CodeLevelNN, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),           
            
            nn.Dropout(0.2),     
            nn.Linear(hidden_dim, 2) 
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.network(x)

class DeepKnowledgeMapper:
    """Handles the PyTorch classifier and the CodeBERT embedding pipeline."""
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = CodeLevelNN(input_dim=768).to(self.device)
        self.tokenizer = RobertaTokenizer.from_pretrained("microsoft/codebert-base")
        self.codebert = RobertaModel.from_pretrained("microsoft/codebert-base").to(self.device)
        self.weights_path = "lumen_brain.pth"
        
        
        for param in self.codebert.parameters():
            param.requires_grad = False
            
        
        for param in self.codebert.encoder.layer[-2:].parameters():
            param.requires_grad = True

        if os.path.exists(self.weights_path):
            checkpoint = torch.load(self.weights_path, map_location=self.device, weights_only=False)
            if isinstance(checkpoint, dict) and 'model_state_dict' in checkpoint:
                self.model.load_state_dict(checkpoint['model_state_dict'])
                self.codebert.load_state_dict(checkpoint['codebert_state_dict'])
            else:
                self.model.load_state_dict(checkpoint)
            self._is_trained = True
        else:
            self._is_trained = False

    def get_embedding(self, code_snippet: str) -> torch.Tensor:
        """Translates raw Python code into a 768-number semantic vector."""
        tokens = self.tokenizer(code_snippet, return_tensors="pt", truncation=True, max_length=512)
        input_ids = tokens['input_ids'].to(self.device)
        attention_mask = tokens['attention_mask'].to(self.device)

        
        outputs = self.codebert(input_ids=input_ids, attention_mask=attention_mask)
            
        return outputs.last_hidden_state[:, 0, :]

    def train(self, code_samples: list[str], labels: list[str], epochs: int = 25, batch_size: int = 32):
        """Trains end-to-end, updating the un-frozen CodeBERT layers and Neural Network."""
        print(f"\nStep 1: Tokenizing {len(code_samples)} scripts...")
        
        label_map = {"Junior": 0, "Senior": 1}
        
        # Tokenize everything and keep on CPU to save VRAM
        tokens = self.tokenizer(code_samples, padding=True, truncation=True, max_length=512, return_tensors="pt")
        X_input_ids = tokens['input_ids']
        X_attention_mask = tokens['attention_mask']
        Y = torch.tensor([label_map[l] for l in labels], dtype=torch.long)

        print("\nStep 2: Training the Neural Network alongside CodeBERT...")
        
        trainable_params = list(self.model.parameters()) + \
                           list(filter(lambda p: p.requires_grad, self.codebert.parameters()))
                           
        # We drop the learning rate (e.g., 1e-4) to make sure we don't destroy CodeBERT's weights
        optimizer = optim.Adam(trainable_params, lr=1e-4)
        criterion = nn.CrossEntropyLoss()
        
        self.model.train() 
        self.codebert.train() 
        
        dataset_size = len(code_samples)

        for epoch in range(epochs):
            permutation = torch.randperm(dataset_size)
            epoch_loss = 0
            steps = 0

            # Process in batches
            for i in range(0, dataset_size, batch_size):
                indices = permutation[i:i+batch_size]
                
                # Move batches to device during loop execution
                batch_input_ids = X_input_ids[indices].to(self.device)
                batch_attention_mask = X_attention_mask[indices].to(self.device)
                batch_y = Y[indices].to(self.device)

                optimizer.zero_grad()
                
                # Forward pass through CodeBERT then MLP
                outputs = self.codebert(input_ids=batch_input_ids, attention_mask=batch_attention_mask)
                cls_tokens = outputs.last_hidden_state[:, 0, :]
                logits = self.model(cls_tokens)
                
                loss = criterion(logits, batch_y)
                loss.backward()
                optimizer.step()
                
                epoch_loss += loss.item()
                steps += 1

            if (epoch + 1) % 5 == 0 or epoch == 0:
                print(f"Epoch {epoch+1:02d}/{epochs} | Avg Loss: {epoch_loss/steps:.4f}")

        # Save both state_dicts
        torch.save({
            'model_state_dict': self.model.state_dict(),
            'codebert_state_dict': self.codebert.state_dict(),
        }, self.weights_path)
        self._is_trained = True
        print(f"\n✅ Neural Network and CodeBERT weights saved to {self.weights_path}!")

    def predict(self, code_snippet: str) -> str:
        """Predicts the level of a new piece of code."""
        if not self._is_trained:
            return "Unknown (Model untrained)"
            
        self.model.eval()
        self.codebert.eval()
        with torch.no_grad():
            embedding = self.get_embedding(code_snippet)
            output = self.model(embedding)
            prediction_idx = torch.argmax(output, dim=1).item()

        return "Senior" if prediction_idx == 1 else "Junior"