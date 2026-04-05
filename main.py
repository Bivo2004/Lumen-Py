import typer
import pyperclip
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from pathlib import Path
from rich.live import Live
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

            console.print("\n[bold green]Lumen:[/bold green]")
            full_response = ""
            # The Live display updates the Markdown rendering in real-time
            with Live(Markdown(""), console=console, refresh_per_second=15) as live:
                for chunk in engine.ask_tutor_stream(user_input):
                    full_response += chunk
                    live.update(Markdown(full_response))

        except KeyboardInterrupt:
            console.print("\n[bold green]Lumen:[/bold green] Session terminated. Goodbye!")
            break


@app.command()
def review(target_path: Path, model: str = typer.Option("llama3", help="The Ollama model to use.")):
    """
    Review a single Python file OR an entire project directory.
    """
    if not target_path.exists():
        console.print(f"[bold red]Error:[/bold red] Could not find {target_path}")
        raise typer.Exit()

    # --- THE SYSTEM SCANNER ---
    code_content = ""
    file_count = 0
    
    with console.status("[bold cyan]Scanning file system...", spinner="dots"):
        if target_path.is_file():
            # Single file logic
            with open(target_path, "r", encoding="utf-8") as f:
                code_content = f"--- FILE: {target_path.name} ---\n{f.read()}\n\n"
            file_count = 1
            console.print(Panel.fit(f"[bold green]Lumen Code Reviewer[/bold green]\nAnalyzing File: {target_path.name}", border_style="green"))
            
        elif target_path.is_dir():
            # Directory logic: Crawl the folder
            console.print(Panel.fit(f"[bold green]Lumen System Architect[/bold green]\nAnalyzing Project: {target_path.name}/", border_style="green"))
            
            # Define folders to ignore
            ignore_dirs = {".venv", "venv", "env", "__pycache__", ".git", "build", "dist"}
            
            for filepath in target_path.rglob("*.py"):
                # Skip ignored directories
                if any(ignored in filepath.parts for ignored in ignore_dirs):
                    continue
                    
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    code_content += f"--- FILE: {filepath.name} ---\n{f.read()}\n\n"
                file_count += 1
                
        if file_count == 0:
            console.print("[bold red]Error:[/bold red] No valid Python files found.")
            raise typer.Exit()

    console.print(f"[dim]Successfully loaded {file_count} file(s) into memory.[/dim]\n")

    # --- THE REVIEW PIPELINE ---
    with console.status("[bold cyan]Booting neural engines and loading CodeBERT...", spinner="dots"):
        handler = LocalAIHandler(model_name=model)
        mapper = DeepKnowledgeMapper()
        
    with console.status("[bold yellow]Analyzing system architecture...", spinner="dots"):
        
        level = mapper.predict(code_content[:2000]) 
        
    console.print(f"[bold blue]Overall Architectural Maturity:[/bold blue] {level} Level\n")

    strategy = SocraticStrategy()
    engine = SocraticEngine(ai_handler=handler, strategy=strategy)
    
    hidden_prompt = (
        f"I have provided the code for a Python project below. Your ML model classified the overall architecture "
        f"as {level}-level. Review it as a strict Socratic software architect. Do NOT rewrite "
        f"the code. Look at how the files interact. Ask me exactly ONE targeted question about my project's "
        f"design patterns, separation of concerns, or scalability.\n\n"
        f"PROJECT CODE:\n{code_content}"
    )
    
    
    console.print("\n[bold green]Lumen:[/bold green]")
    full_response = ""
    
    # The Live display updates the Markdown rendering in real-time
    with Live(Markdown(""), console=console, refresh_per_second=15) as live:
        for chunk in engine.ask_tutor_stream(hidden_prompt):
            full_response += chunk
            live.update(Markdown(full_response))
if __name__ == "__main__":
    app()