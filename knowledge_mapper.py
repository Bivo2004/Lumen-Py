from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from typing import List

class CodeLevelClassifier:
    """
    Classifies Python code snippets as 'Junior' or 'Senior' level 
    using Machine Learning to detect architectural knowledge gaps.
    """
    def __init__(self):
        # TF-IDF converts the code text into a matrix of token counts
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.classifier = LogisticRegression()
        self._is_trained = False

    def train(self, code_samples: List[str], labels: List[str]):
        """Trains the underlying ML model."""
        # Convert text to numeric features
        X_vectorized = self.vectorizer.fit_transform(code_samples)
        # Train the model
        self.classifier.fit(X_vectorized, labels)
        self._is_trained = True

    def predict(self, code_snippet: str) -> str:
        """Predicts the level of a given code snippet."""
        if not self._is_trained:
            raise RuntimeError("Classifier must be trained before predicting.")
        
        
        X_new = self.vectorizer.transform([code_snippet])
        return self.classifier.predict(X_new)[0]