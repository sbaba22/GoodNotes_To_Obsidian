from openai import OpenAI
from dotenv import load_dotenv

from image_utils import image_to_base64
from models import Page, Note
import json
from response_parser import parse_note

load_dotenv()


class AIClient:
    """Client responsible for converting page images into Markdown."""

    def __init__(self):
        self.client = OpenAI()

    def generate_markdown(
        self,
        page: Page,
        prompt: str,
    ) -> str:

        image_base64 = image_to_base64(page.image_path)

        response = self.client.responses.create(
            model="gpt-5.5",
            input=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "input_text",
                            "text": prompt,
                        }
                    ],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": "Convert the attached page into Markdown following the system instructions.",
                        },
                        {
                            "type": "input_image",
                            "image_url": f"data:image/png;base64,{image_base64}",
                        },
                    ],
                },
            ],
        )

        return parse_note(
            response.output_text
        )