# GoodNotes to Obsidian

Convert GoodNotes PDF exports into Markdown notes for Obsidian and catalogues them using GPT-5.5 Vision.


## Installation

```bash
git clone https://github.com/YOUR_USERNAME/GoodnotesConverter.git

cd GoodnotesConverter

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## Configuration

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

Edit `config.py` to set:

- `INPUT_DIR`
- `OBSIDIAN_VAULT`

Requires some way of cloud syncing. Some hardare is incompatible with certain clouds(eg: google drive on apple), tested using icloud. 
To use make an input folder and create an obsidian vault inside the cloud, when needed upload notes to input and run script.

## Usage

1. Export a PDF from GoodNotes.
2. Place it in the input folder.
3. Run:

```bash
python convert_notes.py
```

The converter will:

- render every PDF page
- generate Markdown with GPT-5.5 Vision
- save the notes directly into your Obsidian vault
- catalogue the page with links to related concepts
- delete the processed PDF after a successful conversion

