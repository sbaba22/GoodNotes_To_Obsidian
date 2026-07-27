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
    frontmatter += f"source: {note.source}\n"
    frontmatter += f"page: {note.page}\n"
    frontmatter += "---\n\n"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(frontmatter)
        f.write(note.markdown)

        if note.links:
            f.write("\n\n---\n\n")
            f.write("## Related notes\n\n")

            for link in note.links:
                f.write(f"- {link}\n")

    return output_path