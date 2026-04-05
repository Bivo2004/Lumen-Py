# Lumen-Py 🧠

An AI-powered, local, Object-Oriented coding mentor designed to fight "AI Brain Rot." 

Instead of writing the code for you and making you dependent, Lumen-Py uses a locally fine-tuned PyTorch Deep Learning model to analyze your architectural maturity, and a local Socratic LLM to guide you to the answers yourself.

## 🌟 What It Offers (Features)
* **System-Level Architecture Scanning:** Point Lumen at an entire project directory. It will crawl your files, map your dependencies, and critique your overall system design (e.g., pointing out tightly coupled classes or poor separation of concerns).
* **Deep Learning Code Classifier:** Uses a locally fine-tuned Hugging Face `CodeBERT` model to mathematically classify your Python scripts as "Junior" or "Senior" architecture.
* **Socratic Sledgehammer:** Integrates with local LLMs via Ollama to review code and ask targeted, Socratic questions instead of just printing the solution.
* **Real-Time Token Streaming:** A seamless, matrix-style terminal UI that streams the AI's responses character-by-character, complete with live Markdown rendering.
* **Mermaid.js Visualizer:** Automatically translates architectural concepts into flowchart code that copies straight to your clipboard.

## ⚙️ Installation & Setup

**1. Clone the repository:**
```bash
git clone [https://github.com/Bivo2004/Lumen-Py.git](https://github.com/Bivo2004/Lumen-Py.git)
cd Lumen-Py
```

**2. Install the Python dependencies:**
```bash
pip install torch transformers datasets typer rich pyperclip requests
```

**3. Install Ollama:**
Ensure you have [Ollama](https://ollama.com/) installed and running locally on your machine with your preferred model (the default for this tool is `llama3`).

## 🧠 Training the Brain (Required First Step)
To keep the GitHub repository fast and lightweight, the compiled neural network weights (`lumen_brain.pth`) are ignored by Git. **You must train the PyTorch brain locally before running a code review.**

Run the training pipeline. This script downloads a dataset, tokenizes it via CodeBERT, and trains the PyTorch model directly on your machine:
```bash
python train_deep_model.py
```
*Note: This will take a few moments and will generate a local `lumen_brain.pth` file in your directory. Do not delete this file.*

## 🚀 How to Use Lumen-Py

Lumen-Py is operated entirely through the terminal using its custom CLI.

### 1. The Interactive Mentor
Boot up the terminal chat interface for general Socratic mentoring or to brainstorm architectures.
```bash
python main.py start
```
*(Pro-tip: Inside the chat, try typing `diagram: how a REST API connects to a database` to see the Mermaid visualizer automatically build a flowchart and copy it to your clipboard!)*

### 2. Single-File Socratic Review
Point Lumen at a specific file on your machine. It will analyze the architectural maturity of that script and initiate a targeted Socratic review.
```bash
python main.py review path/to/your/script.py
```

### 3. System-Level Architecture Review
Point Lumen at an entire project folder. It will scan all `.py` files, ignore your virtual environments, and critique how your files and classes interact with one another.
```bash
python main.py review path/to/your/project_folder/
```

## 🏗️ Architecture & Stack
* **Language:** Python 3
* **Deep Learning:** PyTorch, Hugging Face Transformers (`microsoft/codebert-base`), Datasets
* **CLI & UI:** Typer, Rich (with Live Token Streaming)
* **LLM Integration:** Ollama (Local/Offline)