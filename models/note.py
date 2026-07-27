from dataclasses import dataclass, field
from typing import List


@dataclass
class Note:
    title: str
    markdown: str

    links: List[str] = field(default_factory=list)

    source: str = ""
    page: int = 0