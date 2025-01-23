import json
from pathlib import Path


def load_chat_history(file_path: str) -> list:
    """Load chat history from JSON file"""
    path = Path(file_path)
    if path.exists():
        with open(file_path, 'r') as f:
            return json.load(f)
    # Create empty file if it doesn't exist
    path.parent.mkdir(parents=True, exist_ok=True)
    save_chat_history([], file_path)
    return []

def save_chat_history(history: list, file_path: str) -> None:
    """Save chat history to JSON file"""
    with open(file_path, 'w') as f:
        json.dump(history, f, indent=2)
