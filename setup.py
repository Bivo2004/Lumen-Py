from setuptools import setup

setup(
    name="lumen-py",
    version="1.0.2", # The "Bug Fix" release
    description="An AI-powered, local, Object-Oriented coding mentor.",
    author="Bivo",
    # We list the individual files that make up your tool
    py_modules=["main", "deep_mapper", "llm_handler", "socratic_engine", "visualizer", "train_deep_model"],
    # These are the libraries pip will automatically install for the user
    install_requires=[
        "torch",
        "transformers",
        "datasets",
        "typer",
        "rich",
        "pyperclip",
        "requests"
    ],
    # This creates the global terminal command "lumen"
    entry_points={
        "console_scripts": [
            "lumen=main:app", 
        ],
    },
)