from dataclasses import dataclass
from pathlib import Path


@dataclass
class Page:
    """Represents a single rendered PDF page."""

    number: int
    image_path: Path
    markdown: str = ""