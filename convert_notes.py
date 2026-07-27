from ai_client import AIClient
from pdf_renderer import render_pdf
from config import INPUT_DIR
from prompt_loader import load_prompt
from markdown_writer import write_note


def main():
    client = AIClient()
    prompt = load_prompt()

    for pdf in INPUT_DIR.glob("*.pdf"):

        try:

            pages = render_pdf(pdf)

            for page in pages:

                note = client.generate_markdown(
                    page,
                    prompt
                )

                note.source = pdf.name
                note.page = page.number

                path = write_note(note)

                print(f"Saved: {path}")

            pdf.unlink()
            print(f"Deleted: {pdf.name}")

        except Exception as e:

            print(
                f"Failed processing {pdf.name}: {e}"
            )


if __name__ == "__main__":
    main()