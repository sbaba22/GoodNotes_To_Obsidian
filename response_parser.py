import json

from models import Note


def parse_note(response: str) -> Note:

    try:
        data = json.loads(response)

    except json.JSONDecodeError as e:

        print("\n========== INVALID GPT RESPONSE ==========\n")
        print(response)
        print("\n==========================================\n")

        raise RuntimeError(
            "GPT did not return valid JSON."
        ) from e

    return Note(
        title=data["title"],
        markdown=data["markdown"],
        links=data["links"],
    )