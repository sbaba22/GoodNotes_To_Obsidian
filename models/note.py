from dataclasses import dataclass, field
from typing import List


@dataclass
class Note:
    title: str
    markdown: str

    subject: str = ""
    course: str = ""

    tags: List[str] = field(default_factory=list)
    links: List[str] = field(default_factory=list)

    source: str = ""
    page: int = 0