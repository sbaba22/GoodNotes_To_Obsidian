from pathlib import Path

from config import PROMPT_DIR


def load_prompt() -> str:
    """Load the system prompt used for transcription."""

    prompt_path = PROMPT_DIR / "prompt.txt"

    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()