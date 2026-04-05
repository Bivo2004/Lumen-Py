# Lumen-Py 🧠

Lumen-Py is an open-source, "Anti-Dependency" AI Mentor. It is designed to combat "AI Brain Rot" by acting as a Socratic S/W Architect. It refuses to write code for you, instead guiding you through Python OOP, Data Structures, and Clean Code principles using your local LLM.

## Features
* **100% Local Privacy:** Powered by [Ollama](https://ollama.com/) (Llama 3).
* **The Socratic Filter:** Refuses "write this for me" prompts via Strategy Patterns.
* **Architecture Visualization:** Generates Mermaid.js UML and flowcharts on demand.
* **Knowledge Mapping (WIP):** Uses scikit-learn to classify user code as Junior/Senior to adapt its teaching style.

## Installation
1. Install [Ollama](https://ollama.com/) and run `ollama run llama3`.
2. Clone this repository.
3. Install requirements: `pip install -r requirements.txt` (ollama, scikit-learn, datasets, typer, rich).
4. Run the mentor: `python main.py`

## Usage
* Normal chat: Ask for architectural advice or OOP concepts.
* Diagrams: Type `diagram: <concept>` to get Mermaid code.