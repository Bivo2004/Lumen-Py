import typer
import pyperclip
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from pathlib import Path

from llm_handler import LocalAIHandler
from socratic_engine import SocraticEngine, SocraticStrategy
from visualizer import MermaidVisualizer
from deep_mapper import DeepKnowledgeMapper  # <-- Bring in the brain!

app = typer.Typer()
console = Console()

@app.command()
def start(model: str = typer.Option("llama3", help="The Ollama model to use.")):
    """
    Start the Lumen-Py AI Mentor terminal session.
    """
    console.print(Panel.fit("[bold green]Welcome to Lumen-Py[/bold green]\nYour Anti-Dependency AI Mentor.", border_style="green"))
    console.print("[dim]Type 'exit' to quit, or 'diagram: <concept>' to generate an architecture map.[/dim]\n")

    with console.status("[bold cyan]Booting neural engines...", spinner="dots"):
        handler = LocalAIHandler(model_name=model)
        strategy = SocraticStrategy()
        engine = SocraticEngine(ai_handler=handler, strategy=strategy)
        visualizer = MermaidVisualizer(ai_handler=handler)

    while True:
        try:
            user_input = console.input("\n[bold blue]You:[/bold blue] ")
            
            if user_input.lower() in ['exit', 'quit']:
                console.print("[bold green]Lumen:[/bold green] Keep coding cleanly. Goodbye!")
                break
                
            if "diagram" in user_input.lower():
                concept = user_input.lower().replace("diagram", "").strip()
                with console.status("[bold magenta]Drawing on the whiteboard...", spinner="bouncingBar"):
                    mermaid_code = visualizer.generate_class_diagram(concept)
                
                pyperclip.copy(mermaid_code)
                console.print("\n[bold magenta]Lumen (Diagram):[/bold magenta]")
                console.print(Panel(mermaid_code, title="Mermaid.js", border_style="magenta"))
                console.print("[bold green]✅ Raw code automatically copied to your clipboard![/bold green]")
                console.print("[dim]Just go to https://mermaid.live and press Ctrl+V / Cmd+V[/dim]")
                continue

            with console.status("[bold yellow]Lumen is thinking...", spinner="dots"):
                response = engine.ask_tutor(user_input)
            
            console.print("\n[bold green]Lumen:[/bold green]")
            console.print(Markdown(response))

        except KeyboardInterrupt:
            console.print("\n[bold green]Lumen:[/bold green] Session terminated. Goodbye!")
            break

# --- THE NEW CODE REVIEWER COMMAND ---
@app.command()
def review(file_path: Path, model: str = typer.Option("llama3", help="The Ollama model to use.")):
    """
    Review a Python file and initiate a Socratic mentoring session.
    """
    if not file_path.is_file():
        console.print(f"[bold red]Error:[/bold red] Could not find file at {file_path}")
        raise typer.Exit()

    with open(file_path, "r", encoding="utf-8") as f:
        code_content = f.read()

    console.print(Panel.fit(f"[bold green]Lumen-Py Code Reviewer[/bold green]\nAnalyzing: {file_path.name}", border_style="green"))
    
    with console.status("[bold cyan]Booting neural engines and loading CodeBERT (This takes a moment)...", spinner="dots"):
        handler = LocalAIHandler(model_name=model)
        mapper = DeepKnowledgeMapper()
        
    with console.status("[bold yellow]Analyzing code architecture...", spinner="dots"):
        # The ML Brain makes its prediction
        level = mapper.predict(code_content)
        
    console.print(f"[bold blue]Architectural Maturity Detected:[/bold blue] {level} Level\n")

    # Boot the Socratic Engine
    strategy = SocraticStrategy()
    engine = SocraticEngine(ai_handler=handler, strategy=strategy)
    
    # We construct a hidden prompt that combines the code, the ML prediction, and Socratic instructions
    hidden_prompt = (
        f"I have written the Python code below. Your ML model classified my architecture "
        f"as {level}-level. Review it as a strict Socratic tutor. Do NOT give me the answers or rewrite "
        f"the code. Ask me exactly ONE targeted question to help me improve its architecture.\n\n"
        f"CODE:\n{code_content}"
    )
    
    with console.status("[bold yellow]Lumen is reading your code...", spinner="dots"):
        response = engine.ask_tutor(hidden_prompt)
        
    console.print("[bold green]Lumen:[/bold green]")
    console.print(Markdown(response))

if __name__ == "__main__":
    app()