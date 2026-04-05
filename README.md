```markdown
# Lumen-Py 🧠

An AI-powered, local, Object-Oriented coding mentor that actively fights "AI Brain Rot." 

Instead of writing the code for you, Lumen-Py uses a fine-tuned PyTorch Deep Learning model to analyze your architectural maturity and a local Socratic LLM to guide you to the answers yourself.

## 🌟 Features
* **Deep Learning Code Classifier:** Uses a locally fine-tuned Hugging Face `CodeBERT` model to classify Python scripts as "Junior" or "Senior" architecture.
* **Socratic Engine:** Integrates with local LLMs via Ollama to review code and ask targeted, Socratic questions instead of just printing the solution.
* **Mermaid.js Visualizer:** Automatically translates architectural concepts into flowchart code that goes straight to your clipboard.

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Bivo2004/Lumen-Py.git](https://github.com/Bivo2004/Lumen-Py.git)
   cd Lumen-Py
   ```

2. **Install the dependencies:**
   ```bash
   pip install torch transformers datasets typer rich pyperclip
   ```

3. **Install Ollama:**
   Ensure you have [Ollama](https://ollama.com/) installed and running locally with your preferred model (the default for this tool is `llama3`).

## 🧠 Training the Brain (Required First Step)
To keep the GitHub repository lightweight and fast, the compiled neural network weights (`lumen_brain.pth`) are ignored by Git. **You must train the brain locally before running a code review.**

Run the training pipeline. This script downloads a dataset, tokenizes it via CodeBERT, and trains the PyTorch model on your machine:
```bash
python train_deep_model.py
```
*Note: This will take a few moments and will generate a local `lumen_brain.pth` file in your directory. Do not delete this file.*

## 🚀 Usage

**1. Start the Interactive Mentor:**
Boot up the terminal chat interface for general Socratic mentoring or architecture diagram generation.
```bash
python main.py start
```
*(Pro-tip: Try typing `diagram: the connection between Python, web development, data analysis, and automation` to see the Mermaid visualizer in action!)*

**2. Run a Socratic Code Review:**
Point Lumen at a specific file on your machine. It will analyze the architectural maturity and initiate a targeted Socratic review.
```bash
python main.py review path/to/your/script.py
```

## 🏗️ Architecture & Stack
* **Language:** Python 3
* **Deep Learning:** PyTorch, Hugging Face Transformers (`microsoft/codebert-base`), Datasets
* **CLI & UI:** Typer, Rich
* **LLM Integration:** Ollama
```