from pathlib import Path

from config import OUTPUT_DIR, OBSIDIAN_VAULT
from models import Note


def write_note(note: Note) -> Path:
    """
    Save a Note as a Markdown file.
    """

    destination = OBSIDIAN_VAULT if OBSIDIAN_VAULT is not None else OUTPUT_DIR

    destination.mkdir(
        parents=True,
        exist_ok=True,
    )

    filename = f"{note.title}.md"

    # Replace invalid filename characters.
    for c in r'\/:*?"<>|':
        filename = filename.replace(c, "_")

    output_path = destination / filename

    frontmatter = "---\n"

    if note.subject:
        frontmatter += f"subject: {note.subject}\n"

    if note.course:
        frontmatter += f"course: {note.course}\n"

    frontmatter += f"source: {note.source}\n"
    frontmatter += f"page: {note.page}\n"

    if note.tags:
        frontmatter += "tags:\n"
        for tag in note.tags:
            frontmatter += f"  - {tag}\n"

    frontmatter += "---\n\n"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(frontmatter)
        f.write(note.markdown)

    return output_path