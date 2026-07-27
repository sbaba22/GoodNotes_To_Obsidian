import base64
from pathlib import Path


def image_to_base64(image_path: Path) -> str:
    """
    Encode an image as a Base64 string.
    """

    with open(image_path, "rb") as image_file:
        return base64.b64encode(
            image_file.read()
        ).decode("utf-8")