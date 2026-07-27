from config import INPUT_DIR

from pdf_renderer import render_pdf


def main():

    pdfs = sorted(INPUT_DIR.glob("*.pdf"))

    if not pdfs:
        print("No PDF found.")
        return

    for pdf in pdfs:

        pages = render_pdf(pdf)

        print(f"{pdf.name}")

        print(f"Pages: {len(pages)}")

        for page in pages:

            print(page)


if __name__ == "__main__":

    main()