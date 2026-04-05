# Lumen-Py 🧠

An AI-powered, local, Object-Oriented coding mentor designed to fight "AI Brain Rot." 

Instead of writing the code for you and making you dependent, Lumen-Py uses a locally fine-tuned PyTorch Deep Learning model to analyze your architectural maturity, and a local Socratic LLM to guide you to the answers yourself.

## 🌟 What It Offers (Features)
* **System-Level Architecture Scanning:** Point Lumen at an entire project directory. It will crawl your files, map your dependencies, and critique your overall system design (e.g., pointing out tightly coupled classes or poor separation of concerns).
* **Deep Learning Code Classifier:** Uses a locally fine-tuned Hugging Face `CodeBERT` model to mathematically classify your Python scripts as "Junior" or "Senior" architecture.
* **Socratic Sledgehammer (3 Modes):** Integrates with local LLMs via Ollama to review code and ask targeted, Socratic questions. Features a **Rolling Memory Bank** for continuous context, and allows you to choose between Strict, Mentor, or Direct teaching modes.
* **Lumen Academy:** Generate a structured, 3-step syllabus and enter an interactive tutoring loop to learn any tech concept from absolute zero.
* **Real-Time Token Streaming:** A seamless, matrix-style terminal UI that streams the AI's responses character-by-character, complete with live Markdown rendering.
* **Mermaid.js Visualizer:** Automatically translates architectural concepts into flowchart code that copies straight to your clipboard.

## ⚙️ Installation & Setup

**Option 1: Global Install via PyPI (Recommended)**
```bash
pip install lumen-py
```

**Option 2: Install from Source**
```bash
git clone [https://github.com/Bivo2004/Lumen-Py.git](https://github.com/Bivo2004/Lumen-Py.git)
cd Lumen-Py
pip install -e .
```

**Install Ollama (Required for both):**
Ensure you have [Ollama](https://ollama.com/) installed and running locally with your preferred model (the default for this tool is `llama3`).

## 🧠 Training the Brain (Required First Step)
To keep the GitHub repository fast and lightweight, the compiled neural network weights (`lumen_brain.pth`) are ignored by Git. **You must train the PyTorch brain locally before running a code review.**

Run the training pipeline. This script downloads a dataset, tokenizes it via CodeBERT, and trains the PyTorch model directly on your machine:
```bash
python train_deep_model.py
```
*Note: This will take a few moments and will generate a local `lumen_brain.pth` file in your directory. Do not delete this file.*

## 🚀 How to Use Lumen-Py

Because Lumen-Py is installed globally, you can run it from any terminal window using the `lumen` command!

### 1. The Interactive Mentor
Boot up the terminal chat interface for general Socratic mentoring or to brainstorm architectures. You can choose your mode!
```bash
lumen start --mode mentor
```
*(Pro-tip: Inside the chat, try typing `diagram: how a REST API connects to a database` to see the Mermaid visualizer automatically build a flowchart and copy it to your clipboard!)*

### 2. Lumen Academy (Interactive Learning)
Tell Lumen what you want to learn and your current skill level, and it will build a custom syllabus and tutor you step-by-step.
```bash
lumen teach "FastAPI" --level "beginner"
```

### 3. Codebase & Architecture Review
Point Lumen at a specific file or an entire project folder. It will scan your `.py` files, analyze the architectural maturity, and initiate a targeted review.
```bash
lumen review "path/to/your/project_folder" --mode direct
```

## 🛠️ The Architecture (Script Breakdown)
Lumen-Py is built with modularity in mind. Here is what drives the engine under the hood:
* **`main.py`**: The Typer CLI entry point. It routes user commands (`start`, `review`, `teach`) and handles the beautiful terminal UI using Rich.
* **`llm_handler.py`**: The communication layer. It securely interfaces with your local Ollama models to generate streaming text and handle system prompts.
* **`socratic_engine.py`**: The "Brain" of the mentor. It manages the rolling memory bank, enforces the teaching personas (Strict/Mentor/Direct), and guides the conversation flow.
* **`visualizer.py`**: The Diagram Architect. Uses aggressive regex cleaning to force the LLM to output perfectly formatted Mermaid.js graph code without breaking the parser.
* **`deep_mapper.py`**: The PyTorch neural engine. Loads the `CodeBERT` model to analyze your actual Python code and classify its architectural maturity level.
* **`train_deep_model.py`**: The training script used to fine-tune the CodeBERT model on local data to recognize junior vs. senior coding patterns.

## 🏗️ Stack
* **Language:** Python 3
* **Deep Learning:** PyTorch, Hugging Face Transformers (`microsoft/codebert-base`), Datasets
* **CLI & UI:** Typer, Rich
* **LLM Integration:** Ollama