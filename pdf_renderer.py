import fitz

from pathlib import Path

from config import OUTPUT_DIR, RENDER_DPI
from models import Page


def render_pdf(pdf_path: Path):

    document = fitz.open(pdf_path)

    output_folder = OUTPUT_DIR / pdf_path.stem
    output_folder.mkdir(parents=True, exist_ok=True)

    zoom = RENDER_DPI / 72
    matrix = fitz.Matrix(zoom, zoom)

    pages = []

    for index in range(len(document)):

        page = document.load_page(index)

        pix = page.get_pixmap(
            matrix=matrix,
            alpha=False
        )

        image_path = output_folder / f"page_{index+1:03}.png"

        pix.save(image_path)

        pages.append(
            Page(
                number=index + 1,
                image_path=image_path
            )
        )

    document.close()

    return pages